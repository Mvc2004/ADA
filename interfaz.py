import tkinter as tk
from tkinter import filedialog


class InterfazGrafica:
    def __init__(self, arbol):
        self.arbol = arbol
        self.ventana = tk.Tk()
        self.ventana.title("Árbol Rojinegro")

        self.crear_widgets()

    def crear_widgets(self):
        self.etiqueta_buscar = tk.Label(self.ventana, text="Buscar palabra:")
        self.etiqueta_buscar.pack()

        self.entrada_buscar = tk.Entry(self.ventana)
        self.entrada_buscar.pack()

        self.boton_buscar = tk.Button(self.ventana, text="Buscar", command=self.buscar_palabra)
        self.boton_buscar.pack()

        self.boton_cargar = tk.Button(self.ventana, text="Cargar desde archivo", command=self.cargar_archivo)
        self.boton_cargar.pack()

        self.boton_mostrar = tk.Button(self.ventana, text="Mostrar palabras ordenadas", command=self.mostrar_arbol)
        self.boton_mostrar.pack()

        self.resultado = tk.Text(self.ventana, height=10, width=50)
        self.resultado.pack()

    def buscar_palabra(self):
        palabra = self.entrada_buscar.get()
        if palabra:
            encontrado, comparaciones = self.arbol.buscar(palabra)
            if encontrado:
                self.resultado.insert(tk.END, f"'{palabra}' encontrada en {comparaciones} comparaciones.\n")
            else:
                self.resultado.insert(tk.END, f"'{palabra}' no encontrada. Comparaciones: {comparaciones}.\n")
        else:
            self.resultado.insert(tk.END, "Por favor, ingresa una palabra.\n")

    def cargar_archivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            with open(archivo, 'r', encoding="utf-8") as f:
                for palabra in f:
                    self.arbol.insertar(palabra.strip())
            self.resultado.insert(tk.END, f"Archivo cargado correctamente.\n")

    def mostrar_arbol(self):
        palabras = self.arbol.recorrido_inorden()
        self.resultado.insert(tk.END, "Palabras ordenadas:\n")
        self.resultado.insert(tk.END, "\n".join(palabras) + "\n")

    def iniciar(self):
        self.ventana.mainloop()
