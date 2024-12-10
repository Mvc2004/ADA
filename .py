import tkinter as tk
from tkinter import filedialog, messagebox

class NodoRB:
    def __init__(self, palabra):
        self.palabra = palabra #hola rojo
        self.color = 'rojo'  # Color inicial (rojo por defecto)
        self.izquierda = None
        self.derecha = None
        self.padre = None

class ArbolRojinegro:
    def __init__(self):
        self.NIL = NodoRB(None)  # Nodo NIL (vacío), que es negro
        self.NIL.color = 'negro'  # El nodo NIL es negro
        self.raiz = self.NIL  # La raíz del árbol es inicialmente NIL

    def insertar(self, palabra):
        nuevo_nodo = NodoRB(palabra) # Crear un nuevo nodo con la palabra
        print(str(nuevo_nodo))
        print(self.raiz)
        nodo_actual = self.raiz
        print(nodo_actual)
        padre = None
        print("padre" + str(padre))
        
        # Buscar el lugar donde insertar el nuevo nodo
        while nodo_actual != self.NIL:
            padre = nodo_actual
            print("padre actualizado" + str(padre))
            if palabra < nodo_actual.palabra:
                nodo_actual = nodo_actual.izquierda
                print("ndoo actual izq" + str(nodo_actual))
            else:
                nodo_actual = nodo_actual.derecha
                print("ndoo actual der" + str(nodo_actual))
        
        # Asignar el padre del nuevo nodo
        nuevo_nodo.padre = padre
        print("nuevo nodo padre" + str(nuevo_nodo.padre))
        if padre is None:
            self.raiz = nuevo_nodo 
            print("raiz" + str(self.raiz))
        elif padre == self.raiz:
            padre = nuevo_nodo 
            print("padre" + str(padre))
        elif palabra < padre.palabra:
            padre.izquierda = nuevo_nodo
            print("padre izq" + str(padre.izquierda))
        else:
            padre.derecha = nuevo_nodo
            print("padre der" + str(padre.derecha))
        
        nuevo_nodo.izquierda = self.NIL
        nuevo_nodo.derecha = self.NIL
        
        # Si el nuevo nodo es la raíz, se asegura que sea negro
        if nuevo_nodo.padre is None:
            print("nuevo nodo padre" + str(nuevo_nodo.padre) + " " + str(nuevo_nodo.color))
            nuevo_nodo.color = 'negro'
            print("nuevo nodo padre" + str(nuevo_nodo.padre) +" "+ str(nuevo_nodo.color))
            return
        
        # Balanceo del árbol después de insertar el nodo
        self._balancear_insercion(nuevo_nodo)

    def _balancear_insercion(self, nodo):
        print("nodo" + str(nodo))
        print("nodo padre color" + str(nodo.padre.color))
        while nodo.padre.color == 'rojo':  # Mientras el padre sea rojo
            if nodo.padre == nodo.padre.padre.izquierda:
                print("nodo padre" + str(nodo.padre))
                print("nodo padreádre iz" + str(nodo.padre.padre.izquierda))
                print("nodo padrepadre" + str(nodo.padre.padre.derecha))
                tio = nodo.padre.padre.derecha  # El tío del nodo
                print("tio" + str(nodo.padre.padre.derecha) + str(tio.color))
                if tio.color == 'rojo':
                    # Caso 1: El tío es rojo, se hace recoloreo
                    nodo.padre.color = 'negro'
                    tio.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    nodo = nodo.padre.padre
                    print("nodo" + str(nodo))
                else:
                    print("nodo padre der" + nodo.padre.derecha)
                    if nodo == nodo.padre.derecha:
                        nodo = nodo.padre
                        print("nodo " + str(nodo.padre))
                        ##self._rotacion_izquierda(nodo)  # Rotación izquierda
                    nodo.padre.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    #self._rotacion_derecha(nodo.padre.padre)  # Rotación derecha
            else:
                tio = nodo.padre.padre.izquierda
                if tio.color == 'rojo':
                    # Caso 2: El tío es rojo, se hace recoloreo
                    nodo.padre.color = 'negro'
                    tio.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    nodo = nodo.padre.padre
                else:
                    if nodo == nodo.padre.izquierda:
                        nodo = nodo.padre
                        self._rotacion_derecha(nodo)  # Rotación derecha
                    nodo.padre.color = 'negro'
                    nodo.padre.padre.color = 'rojo'
                    self._rotacion_izquierda(nodo.padre.padre)  # Rotación izquierda
            if nodo == self.raiz:
                break
        self.raiz.color = 'negro'  # La raíz siempre debe ser negra

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

    def mostrar_arbol(self, nodo, nivel=0):
        if nodo != self.NIL:
            self.mostrar_arbol(nodo.derecha, nivel + 1)
            print("   " * nivel + f"{nodo.palabra} ({nodo.color})")
            self.mostrar_arbol(nodo.izquierda, nivel + 1)


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
