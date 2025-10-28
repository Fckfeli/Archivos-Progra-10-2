from tkinter import *

root = Tk()
root.title("Spiderman casero xdlol")

PIXEL = 40 


Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=0, column=2)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=0, column=3)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=0, column=4)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=0, column=5)


Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=1, column=1)
for c in range(2,6):
    Frame(root, width=PIXEL, height=PIXEL, bg="red").grid(row=1, column=c)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=1, column=6)


Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=2, column=1)
Frame(root, width=PIXEL, height=PIXEL, bg="red").grid(row=2, column=2)
Frame(root, width=PIXEL, height=PIXEL, bg="white").grid(row=2, column=3)
Frame(root, width=PIXEL, height=PIXEL, bg="white").grid(row=2, column=4)
Frame(root, width=PIXEL, height=PIXEL, bg="red").grid(row=2, column=5)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=2, column=6)


Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=3, column=1)
for c in range(2,6):
    Frame(root, width=PIXEL, height=PIXEL, bg="red").grid(row=3, column=c)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=3, column=6)


Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=4, column=2)
Frame(root, width=PIXEL, height=PIXEL, bg="red").grid(row=4, column=3)
Frame(root, width=PIXEL, height=PIXEL, bg="red").grid(row=4, column=4)
Frame(root, width=PIXEL, height=PIXEL, bg="black").grid(row=4, column=5)

root.mainloop()