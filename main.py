from arbol import ArbolBinarioBusqueda
from interfaz import InterfazGrafica

if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()  # Crear una instancia del árbol
    app = InterfazGrafica(arbol)    # Crear la interfaz gráfica
    app.iniciar()                   # Iniciar la GUI
