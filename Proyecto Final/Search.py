class Nodo():
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

class Frontera():
    def __init__(self):
        self.frontera =[]

    def empty(self):
        return (len(self.frontera) == 0)

    def add(self, nodo):
        self.frontera.append(nodo)

    def eliminar(self):
        # LIFO o FIFO
        pass

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

class Pila(Frontera):
    def eliminar(self):
        # Termina la busqueda si la frontera esta vacia
        if self.empty():
            raise Exception("Frontera vacia")
        else:
            # Guardamos el ultimo item en la lista
            # (el cual es el nodo recientemente añadido)
            nodo = self.frontera[-1]
            # Guardamos todos los items excepto el
            # ultimo (eliminamos)
            self.frontera = self.frontera[:-1]
            return nodo

class Cola(Frontera):
    def eliminar(self):
        # Termina la busqueda si la frontera esta vacia
        if self.empty():
            raise Exception("Frontera vacia")
        else:
            # Guardamos el primer item en la lista
            # (el cual es el nodo añadido de primero)
            nodo = self.frontera[0]
            # Guardamos todos los items excepto el
            # primero (eliminamos)
            self.frontera = self.frontera[1:]
            return nodo

class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(self.state)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq
        # return self.seq.pop(0)

    def update_state(self, state, percept):
        raise NotImplementedError

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, problem):
        raise NotImplementedError