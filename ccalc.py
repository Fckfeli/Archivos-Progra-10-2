import tkinter as tk

def agregar_caracter(caracter):
    # Añade el carácter a la pantalla
    pantalla.insert(tk.END, caracter)

def limpiar_pantalla():
    # Borra la pantalla
    pantalla.delete(0, tk.END)

def calcular_resultado():
    try:
        # Obtiene la expresión de la pantalla
        expresion = pantalla.get()
        # Evalúa la expresión y muestra el resultado
        resultado = eval(expresion) # Usa eval() con precaución para expresiones simples
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Widget de pantalla
pantalla = tk.Entry(ventana, width=20, font=('Arial', 16),)
pantalla.grid(row=0, column=0, columnspan=4)

# Botones de números y operadores
botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', ',', '+'
]

# Crea y ubica los botones
fila = 1
columna = 0
for boton_texto in botones:
    tk.Button(ventana, text=boton_texto, width=5, height=2, command=lambda b=boton_texto: agregar_caracter(b)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botón de limpiar (C)
tk.Button(ventana, text='C', width=5, height=2, command=limpiar_pantalla).grid(row=fila, column=0)
tk.Button(ventana, text='=', width=5, height=2, command=calcular_resultado).grid(row=fila, column=1)
# Botón para calcular (se puede asignar a '=')
# El "=" ya está incluido en el bucle, asumiendo que la lógica para '=' está en agregar_caracter
# Para una lógica de "=" distinta, necesitarías otro botón y su comando.

# Inicia el bucle principal de la aplicación
ventana.mainloop()
