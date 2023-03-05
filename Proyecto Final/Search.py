class Nodo():
    """Elemento mínimo para la construcción de un grafo."""

    def __init__(self, estado, padre, accion):
        """Inicialización de un Nodo"""
        self.estado = estado
        self.padre = padre
        self.accion = accion

class Frontera():
    """Digase de el conjunto de Nodos que están siendo explorados"""

    def __init__(self):
        """Se inicia con una frontera vacía"""

        self.frontera =[]

    def empty(self):
        """Evalua en booleano si la frontera se encuentra vacía"""
        return (len(self.frontera) == 0)

    def add(self, nodo):
        """Agrega un nodo a la frontera"""
        self.frontera.append(nodo)

    def eliminar(self):
        """Función sin implementar, no es necesaria para el proyecto"""

        # LIFO o FIFO
        pass

    def contiene_estado(self, estado):
        """
        Evalua en booleano si el estado indicado se encuentra en alguno
        de los nodo de frontera.
        """

        return any(nodo.estado == estado for nodo in self.frontera)

class Pila(Frontera):
    """Implementación de una pila o stack"""

    def eliminar(self):
        """Elimina un elemento de la pila"""

        # Termina la busqueda si la frontera esta vacía
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
    """Implementación de una cola o queue"""

    def eliminar(self):
        """Elimina un elemento de la cola"""

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
