import tkinter as tk
from tkinter import filedialog, messagebox

class NodoRB:
    
    def __init__(self, palabra):

        self.palabra = palabra # 1 
        self.color = 'rojo'  # 1
        self.izquierda = None # 1
        self.derecha = None # 1
        self.padre = None # 1
        #0(n) = 1 + 1 + 1 + 1 + 1 = 0 (1) Complejidad Constante

class ArbolRojinegro:

    def __init__(self):
        self.NIL = NodoRB(None)  # 1
        self.NIL.color = 'negro'  # 1
        self.raiz = self.NIL  # 1

        #0(n) = 1 + 1 + 1 = 0 (1) Complejidad Constante

    def insertar(self, palabra):

        nuevo_nodo = NodoRB(palabra) #1
        nodo_actual = self.raiz  #1
        padre = None # O(n)= 1
        while nodo_actual != self.NIL:  # O(log n)
            padre = nodo_actual # O(1)
            
            if palabra < nodo_actual.palabra: # O(1)
                nodo_actual = nodo_actual.izquierda # O(1)
            else:
                nodo_actual = nodo_actual.derecha # O(1)
        
        # Asignar el padre del nuevo nodo
        nuevo_nodo.padre = padre # O(1)
        if padre is None: # O(1)
            self.raiz = nuevo_nodo  # O(1)

        else:

            if palabra < padre.palabra: # O(1)
                padre.izquierda = nuevo_nodo # O(1)

            elif palabra > padre.palabra:# O(1)
                padre.derecha = nuevo_nodo# O(1)

            else: 
                print("no cumple")

        nuevo_nodo.izquierda = self.NIL # O(1)
        nuevo_nodo.derecha = self.NIL # O(1)
        nuevo_nodo.color = 'rojo' # O(1)

        # Si el nuevo nodo es la raíz, se asegura que sea negro
        if nuevo_nodo.padre is None:# O(1)
            nuevo_nodo.color = 'negro' # O(1)
            return
        
        # Balanceo del árbol después de insertar el nodo
        self._balancear_insercion(nuevo_nodo)  # O(log n)
        
        #0(n) = 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 + (log n) =  O(log n)
  
    def _balancear_insercion(self, nodo):
        while nodo.padre.color == 'rojo': # O(log n) # Mientras el padre sea rojo
            if nodo.padre == nodo.padre.padre.izquierda:# O(1)
                tio = nodo.padre.padre.derecha  # O(1) # El tío del nodo
                if tio.color == 'rojo': # O(1)
                    # Caso 1: El tío es rojo, se hace recoloreo
                    nodo.padre.color = 'negro'# O(1)
                    tio.color = 'negro'# O(1)
                    nodo.padre.padre.color = 'rojo' # O(1)
                    nodo = nodo.padre.padre # O(1)
                    print("nodo" + str(nodo))# O(1)

                elif tio.color == 'negro': #caso 2 # O(1)

                    if nodo == nodo.padre.derecha: # O(1)
                        nodo = nodo.padre # O(1)
                        self._rotacion_izquierda(nodo)   # O(1)
                    
                    elif nodo == nodo.padre.izquierda: #caso 3 # O(1)
                        nodo.padre.color = 'negro' # O(1)
                        nodo.padre.padre.color = 'rojo' # O(1)
                        self._rotacion_derecha(nodo.padre.padre) # O(1)
                
            elif nodo.padre == nodo.padre.padre.derecha: # O(1)

                tio = nodo.padre.padre.izquierda # O(1) # El tío del nodo
                if tio.color == 'rojo': # O(1)
                    # Caso 1: El tío es rojo, se hace recoloreo
                    nodo.padre.color = 'negro' ## O(1)
                    tio.color = 'negro' # O(1)
                    nodo.padre.padre.color = 'rojo' # O(1)
                    nodo = nodo.padre.padre # O(1)

                elif tio.color == 'negro': #caso 2# O(1)

                    if nodo == nodo.padre.izquierda:# O(1)
                        nodo = nodo.padre.padre.derecha # O(1)
                        self._rotacion_derecha(nodo) # O(1) # Rotación derecha

                    elif nodo == nodo.padre.derecha: #caso 3 # O(1)
                        nodo.padre.color = 'negro' # O(1)
                        nodo.padre.padre.color = 'rojo' # O(1)
                        self._rotacion_izquierda(nodo.padre.padre) # O(1)
            if nodo == self.raiz: # O(1)
                break
        self.raiz.color = 'negro' # O(1) # La raíz siempre debe ser negra
        
         # 0(n)= log(n)+ 1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1 = 0(log n) 
 # Todo es  # 0(1)
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
# Todo es  # 0(1)
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
        nodo_actual = self.raiz # O(1)
        comparaciones = 0  # O(1)
        while nodo_actual != self.NIL:  # O(log n)
            comparaciones += 1
            if palabra == nodo_actual.palabra:  # O(1)
                return True, comparaciones
            elif palabra < nodo_actual.palabra:  # O(1)
                nodo_actual = nodo_actual.izquierda # O(1)
            else:
                nodo_actual = nodo_actual.derecha  # O(1)
        return False, comparaciones # O(1)
    # 0(n) = 1+1+ log(n) + 1+1+1+1+1 = 0(log n)

    def recorrido_inorden(self):
        palabras = []  # O(1)
        self._recorrido_inorden_recursivo(self.raiz, palabras)  # O(1)
        return palabras

    def _recorrido_inorden_recursivo(self, nodo, palabras):
        if nodo != self.NIL: # O(1)
            self._recorrido_inorden_recursivo(nodo.izquierda, palabras) # O(n/2)
            palabras.append(nodo.palabra)  # O(1)
            self._recorrido_inorden_recursivo(nodo.derecha, palabras) # O(n/2)
    # 0(n) = 1+ n/2 + 1 + n/2 = 0(n)    
            

# Funciones de la GUI
def cargar_y_llenar_arbol():

    archivo = filedialog.askopenfilename(title="Seleccionar archivo de texto", filetypes=[("Text files", "*.txt")]) # O(1)
    if archivo:
        
        with open(archivo, 'r') as f: # O(n)
            palabras = [linea.strip() for linea in f.readlines() if linea.strip()] # O(1)
            for palabra in palabras: # O(n)
                arbol.insertar(palabra) # O(n log n)
        messagebox.showinfo("Carga completa", "Archivo cargado correctamente y árbol llenado.") 
    # 0(n) =  O(1) + O(n) + O(1) + O(n) + O(n log n) + O(1) = 0(n log n)
def mostrar_palabras_ordenadas():
    palabras_ordenadas = arbol.recorrido_inorden() # O(n)
    resultado_palabras.config(text="Palabras ordenadas:\n" + "\n".join(filter(None, palabras_ordenadas))) #O(1)
    # 0(n) = O(n) + O(1) = 0(n)

def buscar_palabra():
    palabra = entrada_palabra.get() # O(1)
    encontrado, comparaciones = arbol.buscar(palabra) # O(log n)
    if encontrado:
        resultado_busqueda.config(text=f"Palabra '{palabra}' encontrada en {comparaciones} comparaciones.")    #O(1)
    else:
        resultado_busqueda.config(text=f"Palabra '{palabra}' no encontrada después de {comparaciones} comparaciones.") #O(1)
# 0(n) = O(1) + O(log n) + O(1) + O(1) = 0(log n)

def mostrar_arbol():
    if arbol.raiz == arbol.NIL: # O(1)
        resultado_arbol.config(text="El árbol está vacío.")
    else:
        estructura = generar_estructura_arbol(arbol.raiz, "", True)  # O(n)
        resultado_arbol.config(text=estructura) #O(1)
# 0(n) = O(1) + O(n) + O(1) = 0(n)

def generar_estructura_arbol(nodo, prefijo, es_izquierdo):
    if nodo == arbol.NIL: # O(1)
        return ""
    resultado = (
        prefijo
        + ("└── " if es_izquierdo else "├── ")
        + f"{nodo.palabra} ({nodo.color})\n"
    ) # O(1)
    if nodo.izquierda != arbol.NIL or nodo.derecha != arbol.NIL: # O(1)
        resultado += generar_estructura_arbol(
            nodo.izquierda, prefijo + ("    " if es_izquierdo else "│   "), True
        ) # O(n/2)
        resultado += generar_estructura_arbol(
            nodo.derecha, prefijo + ("    " if es_izquierdo else "│   "), False
        ) # O(n/2)
    return resultado
# 0(n) = O(1) + O() + O(1) + O(1) + O(1) + O(n/2) + O(n/2) = 0(n)

# GUI con Tkinter
ventana = tk.Tk()
ventana.title("Ordenador de Palabras - Árbol Rojinegro")
ventana.geometry("430x500")
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