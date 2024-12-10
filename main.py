import tkinter as tk
from arbol_rojinegro import ArbolRojinegro
from interfaz import InterfazGrafica

def buscar_palabra():
    # Implementar la lógica para buscar una palabra en el árbol
    pass

def mostrar_palabras_ordenadas():
    # Implementar la lógica para mostrar las palabras ordenadas
    pass

def mostrar_arbol():
    # Implementar la lógica para mostrar el árbol rojinegro
    pass

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Ordenador de Palabras - Árbol Rojinegro")
    ventana.geometry("500x500")
    ventana.configure(bg="white")

    arbol = ArbolRojinegro()

    frame = tk.Frame(ventana, bg="white", padx=10, pady=10, relief="ridge")
    frame.pack(fill=tk.X, pady=10)

    boton_buscar = tk.Button(frame, text="Buscar palabra", font=("Arial", 12),
                             bg="#4682b4", fg="white", command=buscar_palabra)
    boton_buscar.grid(row=2, column=5, padx=5, pady=5)

    entrada_palabra = tk.Entry(frame, font=("Arial", 12))
    entrada_palabra.grid(row=1, column=5, padx=5, pady=5)

    boton_cargar = tk.Button(frame, text="Cargar archivo", font=("Arial", 12))
    boton_cargar.grid(row=3, column=5, padx=5, pady=5)

    boton_ordenadas = tk.Button(frame, text="Mostrar palabras ordenadas", font=("Arial", 12),
                                bg="#FF748B", fg="white", command=mostrar_palabras_ordenadas)
    boton_ordenadas.grid(row=4, column=5, columnspan=2, pady=5)

    resultado_palabras = tk.Label(frame, text="Palabras ordenadas:", font=("Arial", 12),
                                  bg="white", fg="black", justify="left", anchor="w")
    resultado_palabras.grid(row=5, column=5, columnspan=2, pady=5)

    boton_arbol = tk.Button(frame, text="Mostrar árbol rojinegro", font=("Arial", 12),
                            bg="#FF2929", fg="white", command=mostrar_arbol)
    boton_arbol.grid(row=6, column=5, columnspan=2, pady=5)

    resultado_arbol = tk.Label(frame, text="Árbol Rojinegro:", font=("Arial", 12),
                               bg="white", fg="black", justify="left", anchor="w")
    resultado_arbol.grid(row=7, column=5, columnspan=2, pady=5)

    ventana.mainloop()