import tkinter as tk
from tkinter import filedialog, messagebox

# Nodo del árbol rojinegro
class NodoRB:
    def __init__(self, palabra, color="rojo"):
        self.palabra = palabra
        self.color = color
        self.izquierda = None
        self.derecha = None
        self.padre = None

# Árbol rojinegro
class ArbolRojinegro:
    def __init__(self):
        self.NIL = NodoRB(None, color="negro")  # Nodo hoja NIL
        self.raiz = self.NIL

    def insertar(self, palabra):
        nuevo_nodo = NodoRB(palabra)
        nuevo_nodo.izquierda = self.NIL
        nuevo_nodo.derecha = self.NIL

        nodo_actual = self.raiz
        padre = None

        while nodo_actual != self.NIL:
            padre = nodo_actual
            if palabra < nodo_actual.palabra:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        nuevo_nodo.padre = padre
        if padre is None:
            self.raiz = nuevo_nodo
        elif palabra < padre.palabra:
            padre.izquierda = nuevo_nodo
        else:
            padre.derecha = nuevo_nodo

        self._balancear_insercion(nuevo_nodo)

    def _balancear_insercion(self, nodo):
        while nodo.padre and nodo.padre.color == "rojo":
            abuelo = nodo.padre.padre
            if nodo.padre == abuelo.izquierda:
                tio = abuelo.derecha
                if tio.color == "rojo":  # Caso 1
                    nodo.padre.color = "negro"
                    tio.color = "negro"
                    abuelo.color = "rojo"
                    nodo = abuelo
                else:
                    if nodo == nodo.padre.derecha:  # Caso 2
                        nodo = nodo.padre
                        self._rotar_izquierda(nodo)
                    nodo.padre.color = "negro"  # Caso 3
                    abuelo.color = "rojo"
                    self._rotar_derecha(abuelo)
            else:
                tio = abuelo.izquierda
                if tio.color == "rojo":  # Caso 1
                    nodo.padre.color = "negro"
                    tio.color = "negro"
                    abuelo.color = "rojo"
                    nodo = abuelo
                else:
                    if nodo == nodo.padre.izquierda:  # Caso 2
                        nodo = nodo.padre
                        self._rotar_derecha(nodo)
                    nodo.padre.color = "negro"  # Caso 3
                    abuelo.color = "rojo"
                    self._rotar_izquierda(abuelo)

        self.raiz.color = "negro"

    def _rotar_izquierda(self, nodo):
        y = nodo.derecha
        nodo.derecha = y.izquierda
        if y.izquierda != self.NIL:
            y.izquierda.padre = nodo
        y.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = y
        elif nodo == nodo.padre.izquierda:
            nodo.padre.izquierda = y
        else:
            nodo.padre.derecha = y
        y.izquierda = nodo
        nodo.padre = y

    def _rotar_derecha(self, nodo):
        y = nodo.izquierda
        nodo.izquierda = y.derecha
        if y.derecha != self.NIL:
            y.derecha.padre = nodo
        y.padre = nodo.padre
        if nodo.padre is None:
            self.raiz = y
        elif nodo == nodo.padre.derecha:
            nodo.padre.derecha = y
        else:
            nodo.padre.izquierda = y
        y.derecha = nodo
        nodo.padre = y

    def recorrido_inorden(self):
        palabras = []
        self._recorrido_inorden_recursivo(self.raiz, palabras)
        return palabras

    def _recorrido_inorden_recursivo(self, nodo, palabras):
        if nodo != self.NIL:
            self._recorrido_inorden_recursivo(nodo.izquierda, palabras)
            palabras.append(nodo.palabra)
            self._recorrido_inorden_recursivo(nodo.derecha, palabras)

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

# Funciones de la GUI
def cargar_y_llenar_arbol():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Text files", "*.txt")])
    if archivo:
        with open(archivo, 'r') as f:
            palabras = [linea.strip() for linea in f.readlines()]
            for palabra in palabras:
                arbol.insertar(palabra)
        messagebox.showinfo("Carga completa", "Archivo cargado correctamente y árbol llenado.")

def mostrar_palabras_ordenadas():
    palabras_ordenadas = arbol.recorrido_inorden()
    resultado_palabras.config(text="Palabras ordenadas:\n" + "\n".join(filter(None, palabras_ordenadas)))

def buscar_palabra():
    palabra = entrada_palabra.get()
    encontrado, comparaciones = arbol.buscar(palabra)
    if encontrado:
        resultado_busqueda.config(text=f"Palabra '{palabra}' encontrada en {comparaciones} comparaciones.")
    else:
        resultado_busqueda.config(text=f"Palabra '{palabra}' no encontrada después de {comparaciones} comparaciones.")

def mostrar_arbol():
    if arbol.raiz == arbol.NIL:
        resultado_arbol.config(text="El árbol está vacío.")
    else:
        estructura = generar_estructura_arbol(arbol.raiz, "", True)
        resultado_arbol.config(text=estructura)

def generar_estructura_arbol(nodo, prefijo, es_izquierdo):
    if nodo == arbol.NIL:
        return ""
    resultado = (
        prefijo
        + ("└── " if es_izquierdo else "├── ")
        + f"{nodo.palabra} ({nodo.color})\n"
    )
    if nodo.izquierda != arbol.NIL or nodo.derecha != arbol.NIL:
        resultado += generar_estructura_arbol(
            nodo.izquierda, prefijo + ("    " if es_izquierdo else "│   "), True
        )
        resultado += generar_estructura_arbol(
            nodo.derecha, prefijo + ("    " if es_izquierdo else "│   "), False
        )
    return resultado

# GUI con Tkinter
ventana = tk.Tk()
ventana.title("Ordenador de Palabras - Árbol Rojinegro")

arbol = ArbolRojinegro()

frame = tk.Frame(ventana)
frame.pack(padx=10, pady=10)

boton_cargar = tk.Button(frame, text="Cargar archivo", command=cargar_y_llenar_arbol)
boton_cargar.grid(row=0, column=0, padx=5, pady=5)

entrada_palabra = tk.Entry(frame)
entrada_palabra.grid(row=1, column=0, padx=5, pady=5)

boton_buscar = tk.Button(frame, text="Buscar palabra", command=buscar_palabra)
boton_buscar.grid(row=1, column=1, padx=5, pady=5)

resultado_busqueda = tk.Label(frame, text="Resultado de la búsqueda:")
resultado_busqueda.grid(row=2, column=0, columnspan=2, pady=5)

boton_ordenadas = tk.Button(frame, text="Mostrar palabras ordenadas", command=mostrar_palabras_ordenadas)
boton_ordenadas.grid(row=3, column=0, columnspan=2, pady=5)

resultado_palabras = tk.Label(frame, text="Palabras ordenadas:", justify="left", anchor="w")
resultado_palabras.grid(row=4, column=0, columnspan=2, pady=5)

boton_arbol = tk.Button(frame, text="Mostrar árbol rojinegro", command=mostrar_arbol)
boton_arbol.grid(row=5, column=0, columnspan=2, pady=5)

resultado_arbol = tk.Label(frame, text="Árbol Rojinegro:", justify="left", anchor="w")
resultado_arbol.grid(row=6, column=0, columnspan=2, pady=5)

ventana.mainloop()
