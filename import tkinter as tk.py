import tkinter as tk
from tkinter import simpledialog, messagebox

def agregar_caracter(caracter):
    pantalla.insert(tk.END, caracter)

def limpiar_pantalla():
    pantalla.delete(0, tk.END)

def calcular_resultado():
    try:
        expresion = pantalla.get().replace(',', '.')  # Reemplaza coma decimal por punto para evaluar
        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, str(resultado))
    except Exception:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def calcular_intercambio():
    try:
        monto_str = pantalla.get().replace(',', '.')
        monto = float(monto_str)
        tasa_str = simpledialog.askstring("Tasa de cambio", "Ingrese la tasa de cambio:")
        if tasa_str is None:
            return  # Si el usuario cancela el input, no hacer nada
        tasa = float(tasa_str.replace(',', '.'))
        resultado = monto * tasa
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, f"{resultado:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos para monto y tasa.")
    except Exception:
        messagebox.showerror("Error", "Ocurrió un error inesperado.")

# Configuración ventana
ventana = tk.Tk()
ventana.title("Calculadora con Intercambio de Moneda")

pantalla = tk.Entry(ventana, width=20, font=('Arial', 16))
pantalla.grid(row=0, column=0, columnspan=4, pady=10)

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', ',', '+'
]

fila = 1
columna = 0
for texto in botones:
    tk.Button(ventana, text=texto, width=5, height=2, command=lambda t=texto: agregar_caracter(t)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

tk.Button(ventana, text='C', width=5, height=2, command=limpiar_pantalla).grid(row=fila, column=0)
tk.Button(ventana, text='=', width=5, height=2, command=calcular_resultado).grid(row=fila, column=1)
tk.Button(ventana, text='CH', width=5, height=2, command=calcular_intercambio).grid(row=fila, column=2)

ventana.mainloop()
