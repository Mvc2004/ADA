class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierda = None
        self.derecha = None

class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None

    def insertar(self, palabra):
        if not self.raiz: #si es vacia pañabra se convierte en la raiz
            self.raiz = Nodo(palabra)
        else:
            self._insertar_nodo(self.raiz, palabra)

    def _insertar_nodo(self, nodo, palabra):
        if palabra < nodo.palabra:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(palabra)
            else:
                self._insertar_nodo(nodo.izquierda, palabra)
        elif palabra > nodo.palabra:
            if nodo.derecha is None:
                nodo.derecha = Nodo(palabra)
            else:
                self._insertar_nodo(nodo.derecha, palabra)

    def recorrido_inorden(self):
        return self._recorrido_inorden(self.raiz)

    def _recorrido_inorden(self, nodo):
        palabras = []
        if nodo:
            palabras.extend(self._recorrido_inorden(nodo.izquierda))
            palabras.append(nodo.palabra)
            palabras.extend(self._recorrido_inorden(nodo.derecha))
        return palabras

    def buscar(self, palabra):
        return self._buscar(self.raiz, palabra, 0)

    def _buscar(self, nodo, palabra, comparaciones):
        if nodo is None:
            return False, comparaciones
        comparaciones += 1
        if palabra == nodo.palabra:
            return True, comparaciones
        elif palabra < nodo.palabra:
            return self._buscar(nodo.izquierda, palabra, comparaciones)
        else:
            return self._buscar(nodo.derecha, palabra, comparaciones)
