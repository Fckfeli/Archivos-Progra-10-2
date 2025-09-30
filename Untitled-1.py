from tkinter import *

# Dimensiones
PIXEL_SIZE = 50

# Matriz para formar la letra "F"
F_SHAPE = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
]

# Crear ventana
root = Tk()
root.title("Pixel Art - Letra F")

# Colores
COLOR_ON = "blue"
COLOR_OFF = "white"

# Recorrer la matriz y dibujar
for row in range(len(F_SHAPE)):
    for col in range(len(F_SHAPE[row])):
        frame = Frame(
            root,
            width=PIXEL_SIZE,
            height=PIXEL_SIZE,
            bg=COLOR_ON if F_SHAPE[row][col] == 1 else COLOR_OFF,
            highlightbackground="black",  # Opcional: bordes
            highlightthickness=1
        )
        frame.grid(row=row, column=col)

# Iniciar ventana
root.mainloop()
