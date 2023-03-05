class Sentence():

    def evaluate(self, model):
        """Evalúa la sentencia lógica."""

        raise Exception("nothing to evaluate")

    def formula(self):
        """Devuelve una cadena de la formula que representa una sentencia lógica."""

        return ""

    def symbols(self):
        """Devuelve un conjunto de todos los símbolos de la sentencia lógica."""

        return set()

    @classmethod
    def validate(cls, sentence):
        """Valida que la sentencia sea una instancia de la clase Sentence"""

        if not isinstance(sentence, Sentence):
            raise TypeError("Debe ser una secuencia lógica")

    @classmethod
    def parenthesize(cls, s):
        """Pone entre paréntesis una expresión si no está ya entre paréntesis."""

        def balanced(s):
            """Comprueba si una cadena tiene paréntesis equilibrados."""

            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    if count <= 0:
                        return False
                    count -= 1
            return count == 0
        if not len(s) or s.isalpha() or (
                s[0] == "(" and s[-1] == ")" and balanced(s[1:-1])
        ):
            return s
        else:
            return f"({s})"


class Symbol(Sentence):

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Symbol) and self.name == other.name

    def __hash__(self):
        return hash(("symbol", self.name))

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        try:
            return bool(model[self.name])
        except KeyError:
            raise EvaluationException(f"variable {self.name} no se encuentra en el modelo")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}


class Not(Sentence):
    """Operador NOT"""

    def __init__(self, operand):
        Sentence.validate(operand)
        self.operand = operand

    def __eq__(self, other):
        return isinstance(other, Not) and self.operand == other.operand

    def __hash__(self):
        return hash(("not", hash(self.operand)))

    def __repr__(self):
        return f"Not({self.operand})"

    def evaluate(self, model):
        return not self.operand.evaluate(model)

    def formula(self):
        return "¬" + Sentence.parenthesize(self.operand.formula())

    def symbols(self):
        return self.operand.symbols()


class And(Sentence):
    """Operador AND"""

    def __init__(self, *conjuncts):
        for conjunct in conjuncts:
            Sentence.validate(conjunct)
        self.conjuncts = list(conjuncts)

    def __eq__(self, other):
        return isinstance(other, And) and self.conjuncts == other.conjuncts

    def __hash__(self):
        return hash(
            ("and", tuple(hash(conjunct) for conjunct in self.conjuncts))
        )

    def __repr__(self):
        conjunctions = ", ".join(
            [str(conjunct) for conjunct in self.conjuncts]
        )
        return f"And({conjunctions})"

    def add(self, conjunct):
        Sentence.validate(conjunct)
        self.conjuncts.append(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return " ∧ ".join([Sentence.parenthesize(conjunct.formula())
                           for conjunct in self.conjuncts])

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])


class Or(Sentence):
    """Operador OR"""

    def __init__(self, *disjuncts):
        for disjunct in disjuncts:
            Sentence.validate(disjunct)
        self.disjuncts = list(disjuncts)

    def __eq__(self, other):
        return isinstance(other, Or) and self.disjuncts == other.disjuncts

    def __hash__(self):
        return hash(
            ("or", tuple(hash(disjunct) for disjunct in self.disjuncts))
        )

    def __repr__(self):
        disjuncts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjuncts})"

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return " ∨  ".join([Sentence.parenthesize(disjunct.formula())
                            for disjunct in self.disjuncts])

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])

class Biconditional(Sentence):
    """Operador BICONDICIONAL"""

    def __init__(self, left, right):
        Sentence.validate(left)
        Sentence.validate(right)
        self.left = left
        self.right = right

    def __eq__(self, other):
        return (isinstance(other, Biconditional)
                and self.left == other.left
                and self.right == other.right)

    def __hash__(self):
        return hash(("biconditional", hash(self.left), hash(self.right)))

    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"

    def evaluate(self, model):
        return ((self.left.evaluate(model)
                 and self.right.evaluate(model))
                or (not self.left.evaluate(model)
                    and not self.right.evaluate(model)))

    def formula(self):
        left = Sentence.parenthesize(str(self.left))
        right = Sentence.parenthesize(str(self.right))
        return f"{left} <=> {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())


def model_check(knowledge, query):
    """Comprueba si la base de conocimientos implica una consulta."""

    def check_all(knowledge, query, symbols, model):
        """Comprueba si la base de conocimientos implica una consulta, dado un modelo concreto."""

        # Si el modelo tiene una asignación para cada símbolo
        if not symbols:

            # Si la base de conocimientos es verdadera en el modelo, la consulta también debe serlo.
            if knowledge.evaluate(model):
                return query.evaluate(model)
            return True
        else:

            # Elija uno de los símbolos restantes no utilizados
            remaining = symbols.copy()
            p = remaining.pop()

            # Crear un modelo en el que el símbolo sea verdadero
            model_true = model.copy()
            model_true[p] = True

            # Crear un modelo en el que el símbolo sea falso
            model_false = model.copy()
            model_false[p] = False

            # Garantizar que la vinculación se cumple en ambos modelos
            return (check_all(knowledge, query, remaining, model_true) and
                    check_all(knowledge, query, remaining, model_false))

    # Obtener todos los símbolos tanto en el conocimiento como en la consulta
    symbols = set.union(knowledge.symbols(), query.symbols())

    # Comprobar que el conocimiento implica consulta
    return check_all(knowledge, query, symbols, dict())
