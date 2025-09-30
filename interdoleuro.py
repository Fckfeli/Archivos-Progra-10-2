import tkinter as tk












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








ventana.mainloop()