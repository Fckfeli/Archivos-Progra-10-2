from tkinter import *
root = Tk()

cuadro = Frame()
cuadro1 = Frame()
cuadro2 = Frame()
cuadro3 = Frame()
cuadro4 = Frame()

cuadro6 = Frame()
cuadro7 = Frame()
cuadro8 = Frame()
cuadro.config(width=150, height=150, bg="red")
cuadro.grid(row=0, column=0)

cuadro1.config(width=150, height=150, bg="blue")
cuadro1.grid(row=1, column=0)

cuadro2.config(width=150, height=150, bg="purple")
cuadro2.grid(row=2,column=0)
cuadro3.config(width=150, height=150, bg="cyan")
cuadro3.grid(row=0,column=1)
cuadro4.config(width=150, height=150, bg="yellow")
cuadro4.grid(row=0,column=3)

cuadro6.config(width=150, height=150, bg="red")
cuadro6.grid(row=0, column=0)
cuadro7.config(width=150, height=150, bg="red")
cuadro7.grid(row=4, column=0)
cuadro8.config(width=150, height=150, bg="red")
cuadro8.grid(row=2, column=1)




root.mainloop()