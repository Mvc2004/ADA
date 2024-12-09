import tkinter as tk
from tkinter import filedialog

class InterfazGrafica:

    def __init__(self, raiz):
        self.raiz = raiz  # Instancia del árbol
        self.ventana = tk.Tk()
        self.ventana.title("Árbol Binario de Búsqueda")
        self.ventana.geometry("600x400")
        self.ventana.configure(bg="white")  # Fondo claro para la ventana principal

        # Crear los widgets y organizarlos
        self.crear_widgets()

    def crear_widgets(self):
        # Título principal
        titulo = tk.Label(
            self.ventana, text="Árbol Binario de Búsqueda",
            font=("Arial", 16, "bold"), bg="white", fg="#00008b"
        )
        titulo.pack(pady=10)

        # Frame superior para las acciones principales
        frame_superior = tk.Frame(self.ventana, bg="white", padx=10, pady=10, relief="ridge")
        frame_superior.pack(fill=tk.X, pady=10)

        # Entrada de búsqueda
        tk.Label(frame_superior, text="Buscar palabra:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entrada_buscar = tk.Entry(frame_superior, font=("Arial", 12))
        self.entrada_buscar.grid(row=0, column=1, padx=5, pady=5)

        self.boton_buscar = tk.Button(
            frame_superior, text="Buscar", font=("Arial", 12),
            bg="#4682b4", fg="white", command=self.buscar_palabra
        )
        self.boton_buscar.grid(row=0, column=2, padx=5, pady=5)

        # Botón para insertar palabra
        

        # Frame inferior para otras acciones
        frame_inferior = tk.Frame(self.ventana, bg="white", padx=10, pady=10, relief="ridge")
        frame_inferior.pack(fill=tk.BOTH, expand=True, pady=10)

        self.boton_insertar = tk.Button(
            frame_inferior, text="Insertar palabra", font=("Arial", 12),
            bg="#32cd32", fg="white", command=self.insertar_palabra
        )
        self.boton_insertar.pack(padx=5)
        #self.boton_insertar.grid(row=1, column=0, columnspan=3, pady=5)

        # Botón para cargar archivo
        self.boton_cargar = tk.Button(
            frame_inferior, text="Cargar desde archivo", font=("Arial", 12),
            bg="#ff8c00", fg="white", command=self.cargar_archivo
        )
        self.boton_cargar.pack(pady=5)

        # Botón para mostrar árbol
        self.boton_mostrar = tk.Button(
            frame_inferior, text="Mostrar árbol ordenado", font=("Arial", 12),
            bg="#4682b4", fg="white", command=self.mostrar_arbol
        )
        self.boton_mostrar.pack(pady=5)

        scrollbar = tk.Scrollbar(frame_inferior)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Área de texto para mostrar resultados
        self.resultado = tk.Text(frame_inferior, height=10, width=60, font=("Courier", 10), bg="#f5f5f5", relief="solid", yscrollcommand=scrollbar.set)
        self.resultado.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=self.resultado.yview)

    def insertar_palabra(self):
        palabra = self.entrada_buscar.get()
        if palabra:
            self.raiz.insertar(palabra)
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, f"Palabra '{palabra}' insertada.\n")
            with open("palabras.txt", "a") as paI:
             paI.write(palabra + "\n")
        else:
            self.resultado.insert(tk.END, "Por favor, ingresa una palabra.\n")

    def buscar_palabra(self):
        self.resultado.delete(1.0, tk.END)
        palabra = self.entrada_buscar.get()
        if palabra:
            encontrado, comparaciones = self.raiz.buscar(palabra)
            if encontrado:
                
                self.resultado.insert(tk.END, f"Palabra '{palabra}' encontrada en {comparaciones} comparaciones.\n")
            else:
                self.resultado.insert(tk.END, f"Palabra '{palabra}' no encontrada. Comparaciones realizadas: {comparaciones}.\n")
        else:
            self.resultado.insert(tk.END, "Por favor, ingresa una palabra.\n")

    def cargar_archivo(self):
        self.resultado.delete(1.0, tk.END)
        archivo = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'r', encoding="utf-8") as f:
                palabras = f.readlines()
                for palabra in palabras:
                    self.raiz.insertar(palabra.strip())
            self.resultado.insert(tk.END, f"Archivo '{archivo}' cargado.\n")
        else:
            self.resultado.insert(tk.END, "No se seleccionó un archivo.\n")

    def mostrar_arbol(self):
        self.resultado.delete(1.0, tk.END)
        palabras_ordenadas = self.raiz.recorrido_inorden()
        self.resultado.insert(tk.END, "Palabras ordenadas:\n")
        for palabra in palabras_ordenadas:
            self.resultado.insert(tk.END, f"{palabra}\n")

    def iniciar(self):
        self.ventana.mainloop()
