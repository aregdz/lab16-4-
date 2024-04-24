#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


if __name__ == "__main__":
    root = Tk()
    root.title("Рисование на холсте")

    canvas = Canvas(root, width=400, height=400, bg="lightblue")
    canvas.pack()

    sun = canvas.create_oval(250, 50, 350, 150, fill="yellow", outline="yellow")
    triangle = canvas.create_polygon(50, 200, 250, 200, 150, 50, fill="blue")
    rectangle = canvas.create_rectangle(130, 200, 180, 400, fill="blue")

    for i in range(0, 400, 20):
        canvas.create_line(i, 400, i, 380, fill="green")

    root.mainloop()
