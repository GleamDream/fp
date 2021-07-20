import tkinter
from math import sin, cos, pi

def f(a):
    return (250 + 100 * cos(a), 250 - 100 * sin(a))

root = tkinter.Tk()
canvas = tkinter.Canvas(root,width=500,height=500, bg="#fff")
canvas.pack()

for i in range(5):
    canvas.create_line(*f(i * 144 * pi / 180), *f((i + 1) * 144 * pi / 180), fill="#000")

root.mainloop()
