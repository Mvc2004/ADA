import tkinter as tk
from tkinter import filedialog, messagebox

class NodoRB:
    def __init__(self, palabra):
        self.palabra = palabra
        self.color = 'rojo'  # Color inicial (rojo por defecto)
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolRojinegro:
    def __init__(self):
        self.NIL = NodoRB(None)  # Nodo NIL (vacío)
        self.NIL.color = 'negro'  # El nodo NIL es negro
        self.raiz = self.NIL  # La raíz del árbol es inicialmente NIL

    def insertar(self, palabra):
        nuevo_nodo = NodoRB(palabra)
        nuevo_nodo.izquierda = self.NIL
        nuevo_nodo.derecha = self.NIL
        nodo_actual = self.raiz
        padre = None

        # Buscar dónde insertar el nodo
        while nodo_actual != self.NIL:
            padre = nodo_actual
            if palabra < nodo_actual.palabra:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha

        # Insertar el nodo en el lugar correcto
        nuevo_nodo.padre = padre
        if padre is None:
            self.raiz = nuevo_nodo
        elif palabra < padre.palabra:
            padre.izquierda = nuevo_nodo
        else:
            padre.derecha = nuevo_nodo

        # Balancear el árbol después de la inserción
        self._balancear_insercion(nuevo_nodo)

    def _balancear_insercion(self, nodo):
        while nodo.padre and nodo.padre.color == 'rojo':
            if nodo.padre == nodo.padre.padre.izquierda:
                tio = nodo.padre.padre.derecha
                if tio.color == 'rojo':  # Caso 1
                    nodo.padre.color = 'negro'
                    tio.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.derecha:  # Caso 2
                        nodo = nodo.padre
                        self._rotacion_izquierda(nodo)
                    nodo.padre.color = 'negro'  # Caso 3
                    nodo.padre.padre.color = 'rojo'
                    self._rotacion_derecha(nodo.padre.padre)
            else:
                tio = nodo.padre.padre.izquierda
                if tio.color == 'rojo':  # Caso 1
                    nodo.padre.color = 'negro'
                    tio.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:  # Caso 2
                        nodo = nodo.padre
                        self._rotacion_derecha(nodo)
                    nodo.padre.color = 'negro'  # Caso 3
                    nodo.padre.padre.color = 'rojo'
                    self._rotacion_izquierda(nodo.padre.padre)

            if nodo == self.raiz:
                break
        self.raiz.color = 'negro'

    def _rotacion_izquierda(self, x):
        y = x.derecha
        x.derecha = y.izquierda
        if y.izquierda != self.NIL:
            y.izquierda.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.izquierda:
            x.padre.izquierda = y
        else:
            x.padre.derecha = y
        y.izquierda = x
        x.padre = y

    def _rotacion_derecha(self, x):
        y = x.izquierda
        x.izquierda = y.derecha
        if y.derecha != self.NIL:
            y.derecha.padre = x
        y.padre = x.padre
        if x.padre is None:
            self.raiz = y
        elif x == x.padre.derecha:
            x.padre.derecha = y
        else:
            x.padre.izquierda = y
        y.derecha = x
        x.padre = y

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

    def recorrido_inorden(self):
        palabras = []
        self._recorrido_inorden_recursivo(self.raiz, palabras)
        return palabras

    def _recorrido_inorden_recursivo(self, nodo, palabras):
        if nodo != self.NIL:
            self._recorrido_inorden_recursivo(nodo.izquierda, palabras)
            palabras.append(nodo.palabra)
            self._recorrido_inorden_recursivo(nodo.derecha, palabras)

    def validar_balanceo_negro(self, nodo):
        if nodo == self.NIL:
            return 1  # Nodo NIL cuenta como negro
        altura_izq = self.validar_balanceo_negro(nodo.izquierda)
        altura_der = self.validar_balanceo_negro(nodo.derecha)
        if altura_izq != altura_der or altura_izq == -1:
            return -1
        return altura_izq + (1 if nodo.color == 'negro' else 0)

    def validar_arbol(self):
        if self.raiz.color != 'negro':
            return "La raíz no es negra."
        if self.validar_balanceo_negro(self.raiz) == -1:
            return "Violación en el balanceo de nodos negros."
        return "El árbol cumple con las propiedades de un Árbol Rojinegro."

    def mostrar_arbol(self, nodo, nivel=0):
        if nodo != self.NIL:
            self.mostrar_arbol(nodo.derecha, nivel + 1)
            print("   " * nivel + f"{nodo.palabra} ({nodo.color})")
            self.mostrar_arbol(nodo.izquierda, nivel + 1)


# Aquí se puede incluir la GUI mencionada anteriormente para interactuar con el árbol.



# Funciones de la GUI
def cargar_y_llenar_arbol():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Text files", "*.txt")])
    if archivo:
        
        with open(archivo, 'r') as f:
            palabras = [linea.strip() for linea in f.readlines() if linea.strip()]
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
ventana.geometry("500x500")
ventana.configure(bg="white")

arbol = ArbolRojinegro()

frame = tk.Frame(ventana,bg="white", padx=10, pady=10, relief="ridge")
frame.pack(fill=tk.X, pady=10)

boton_buscar = tk.Button(frame, text="Buscar palabra",font=("Arial", 12),
            bg="#4682b4", fg="white", command=buscar_palabra)
boton_buscar.grid(row=2, column=5, padx=5, pady=5)

entrada_palabra = tk.Entry(frame,font=("Arial", 12))
entrada_palabra.grid(row=1, column=5, padx=5, pady=5)

boton_cargar = tk.Button(frame, text="Cargar archivo", font=("Arial", 12),
            bg="#ff8c00", fg="white", command=cargar_y_llenar_arbol)
boton_cargar.grid(row=0, column=5, padx=5, pady=5)

resultado_busqueda = tk.Label(frame, text="Resultado de la búsqueda:", font=("Arial", 12), bg="white", fg="black")
resultado_busqueda.grid(row=3, column=5, columnspan=2, pady=5)

boton_ordenadas = tk.Button(frame, text="Mostrar palabras ordenadas", font=("Arial", 12),
bg="#FF748B", fg="white", command=mostrar_palabras_ordenadas)
boton_ordenadas.grid(row=4, column=5, columnspan=2, pady=5)

resultado_palabras = tk.Label(frame, text="Palabras ordenadas:", font=("Arial", 12), bg="white", fg="black", justify="left", anchor="w")
resultado_palabras.grid(row=5, column=5, columnspan=2, pady=5)

boton_arbol = tk.Button(frame, text="Mostrar árbol rojinegro", font=("Arial", 12),
bg="#FF2929", fg="white", command=mostrar_arbol)
boton_arbol.grid(row=6, column=5, columnspan=2, pady=5)

resultado_arbol = tk.Label(frame, text="Árbol Rojinegro:",font=("Arial", 12),
            bg="white", fg="black", justify="left", anchor="w")
resultado_arbol.grid(row=7, column=5, columnspan=2, pady=5)
ventana.mainloop()