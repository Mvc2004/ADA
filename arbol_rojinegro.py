class NodoRN:
    def __init__(self, palabra, color="rojo"): # O(n)= 1
        self.palabra = palabra # O(n)= 1
        self.color = color  # Puede ser "rojo" o "negro" # O(n)= 1
        self.izquierda = None  # Hijo izquierdo # O(n)= 1
        self.derecha = None  # Hijo derecho # O(n)= 1
        self.padre = None  # Referencia al nodo padre # O(n)= 1


class ArbolRojinegro:
    def __init__(self):
        self.NIL = NodoRN(None, color="negro")  # Nodo hoja NIL # O(n)= 1
        self.raiz = self.NIL # O(n)= 1

    def insertar(self, palabra):
        nuevo_nodo = NodoRN(palabra) # O(n)= 1
        nuevo_nodo.izquierda = self.NIL # O(n)= 1
        nuevo_nodo.derecha = self.NIL # O(n)= 1
        self._insertar_nodo(self.raiz, nuevo_nodo) # O(n)= 1
        self._balancear_insercion(nuevo_nodo) # O(n)= 1

    def _insertar_nodo(self, raiz, nuevo_nodo):
        nodo_actual = raiz # O(n)= 1
        padre = None # O(n)= 1
        while nodo_actual != self.NIL:  # O(log n)
            padre = nodo_actual # O(n)= 1
            if nuevo_nodo.palabra < nodo_actual.palabra: # O(n)= 1
                nodo_actual = nodo_actual.izquierda # O(n)= 1
            else:
                nodo_actual = nodo_actual.derecha # O(n)= 1

        nuevo_nodo.padre = padre # O(n)= 1
        if padre is None:  # Árbol vacío # O(n)= 1
            self.raiz = nuevo_nodo # O(n)= 1
        elif nuevo_nodo.palabra < padre.palabra: # O(n)= 1
            padre.izquierda = nuevo_nodo # O(n)= 1
        else:
            padre.derecha = nuevo_nodo # O(n)= 1

        nuevo_nodo.color = "rojo"   # O(n)= 1 # Nuevo nodo siempre rojo

    def _balancear_insercion(self, nodo):
        while nodo != self.raiz and nodo.padre.color == "rojo":
            abuelo = nodo.padre.padre
            if nodo.padre == abuelo.izquierda:  # Caso A: Nodo padre es hijo izquierdo
                tio = abuelo.derecha
                if tio.color == "rojo":  # Caso 1: El tío es rojo
                    nodo.padre.color = "negro"
                    tio.color = "negro"
                    abuelo.color = "rojo"
                    nodo = abuelo
                else:
                    if nodo == nodo.padre.derecha:  # Caso 2: Nodo es hijo derecho
                        nodo = nodo.padre
                        self._rotar_izquierda(nodo)
                    nodo.padre.color = "negro"  # Caso 3: Nodo es hijo izquierdo
                    abuelo.color = "rojo"
                    self._rotar_derecha(abuelo)
            else:  # Caso B: Nodo padre es hijo derecho
                tio = abuelo.izquierda
                if tio.color == "rojo":  # Caso 1: El tío es rojo
                    nodo.padre.color = "negro"
                    tio.color = "negro"
                    abuelo.color = "rojo"
                    nodo = abuelo
                else:
                    if nodo == nodo.padre.izquierda:  # Caso 2: Nodo es hijo izquierdo
                        nodo = nodo.padre
                        self._rotar_derecha(nodo)
                    nodo.padre.color = "negro"  # Caso 3: Nodo es hijo derecho
                    abuelo.color = "rojo"
                    self._rotar_izquierda(abuelo)
        self.raiz.color = "negro"

    def _rotar_izquierda(self, nodo):
        derecho = nodo.derecha
        nodo.derecha = derecho.izquierda
        if derecho.izquierda != self.NIL:
            derecho.izquierda.padre = nodo
        derecho.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = derecho
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = derecho
        else:
            nodo.padre.derecha = derecho
        derecho.izquierda = nodo
        nodo.padre = derecho

    def _rotar_derecha(self, nodo):
        izquierdo = nodo.izquierda
        nodo.izquierda = izquierdo.derecha
        if izquierdo.derecha != self.NIL:
            izquierdo.derecha.padre = nodo
        izquierdo.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = izquierdo
        elif nodo == nodo.padre.derecha:
            nodo.padre.derecha = izquierdo
        else:
            nodo.padre.izquierda = izquierdo
        izquierdo.derecha = nodo
        nodo.padre = izquierdo

    def recorrido_inorden(self, nodo=None, palabras=None):
        if palabras is None:
            palabras = []
        if nodo is None:
            nodo = self.raiz
        if nodo != self.NIL:
            self.recorrido_inorden(nodo.izquierda, palabras)
            if nodo.palabra is not None:
                palabras.append(nodo.palabra)
            self.recorrido_inorden(nodo.derecha, palabras)
        return palabras

    def buscar(self, palabra):
        nodo_actual = self.raiz
        comparaciones = 0
        while nodo_actual != self.NIL:
            comparaciones += 1
            if palabra == nodo_actual.palabra:
                return True, comparaciones
            elif palabra < nodo_actual.palabra:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
        return False, comparaciones
