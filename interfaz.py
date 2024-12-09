import tkinter as tk
from tkinter import filedialog

class InterfazGrafica:
    def __init__(self, raiz):
        self.raiz = raiz  # Instancia del árbol
        self.ventana = tk.Tk()
        self.ventana.title("Árbol Binario de Búsqueda")

        # Crear la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Entrada para búsqueda de palabras
        self.etiqueta_buscar = tk.Label(self.ventana, text="Buscar palabra:")
        self.etiqueta_buscar.pack()

        self.entrada_buscar = tk.Entry(self.ventana)
        self.entrada_buscar.pack()

        self.boton_buscar = tk.Button(self.ventana, text="Buscar", command=self.buscar_palabra)
        self.boton_buscar.pack()

        self.boton_insertar = tk.Button(self.ventana, text="Insertar palabra", command=self.insertar_palabra)
        self.boton_insertar.pack()

        self.boton_cargar = tk.Button(self.ventana, text="Cargar desde archivo", command=self.cargar_archivo)
        self.boton_cargar.pack()

        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar árbol ordenado", command=self.mostrar_arbol)
        self.boton_mostrar.pack()

        self.resultado = tk.Text(self.ventana, height=10, width=50)
        self.resultado.pack()

    def insertar_palabra(self):
        palabra = self.entrada_buscar.get()
        if palabra:
            self.raiz.insertar(palabra)
            self.resultado.insert(tk.END, f"Palabra '{palabra}' insertada.\n")
        else:
            self.resultado.insert(tk.END, "Por favor, ingresa una palabra.\n")

    def buscar_palabra(self):
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
        palabras_ordenadas = self.raiz.recorrido_inorden()
        self.resultado.insert(tk.END, "Palabras ordenadas:\n")
        for palabra in palabras_ordenadas:
            self.resultado.insert(tk.END, f"{palabra}\n")

    def iniciar(self):
        self.ventana.mainloop()
