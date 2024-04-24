#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def move_to_point(event):
    x1, y1, x2, y2 = c.coords(ball)
    target_x, target_y = event.x, event.y
    dx = target_x - x1
    dy = target_y - y1
    while abs(dx) > 1 or abs(dy) > 1:
        x1 += int(dx * 0.1)
        y1 += int(dy * 0.1)
        x2 += int(dx * 0.1)
        y2 += int(dy * 0.1)
        c.coords(ball, x1, y1, x2, y2)
        c.update()
        dx = target_x - x1
        dy = target_y - y1


if __name__ == "__main__":
    root = Tk()
    root.title("Постепенное движение круга")

    c = Canvas(root, width=400, height=400, bg="white")
    c.pack()

    ball = c.create_oval(0, 100, 40, 140, fill="green")
    c.bind("<Button-1>", move_to_point)

    root.mainloop()
