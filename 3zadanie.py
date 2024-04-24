#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def change_size(event=None):
    try:
        width = int(width_entry.get())
        height = int(height_entry.get())
        text_area.config(width=width, height=height)
    except ValueError:
        pass


def change_background_color(event):
    text_area.config(bg="white")


def change_background_color_out(event):
    text_area.config(bg="lightgrey")


if __name__ == "__main__":
    root = Tk()
    root.title("Изменение размера многострочного текстового поля")

    Label(root, text="Ширина:").grid(row=0, column=0, padx=5, pady=5)
    width_entry = Entry(root)
    width_entry.grid(row=0, column=1, padx=5, pady=5)
    Label(root, text="Высота:").grid(row=1, column=0, padx=5, pady=5)
    height_entry = Entry(root)
    height_entry.grid(row=1, column=1, padx=5, pady=5)
    Button(root, text="Применить", command=change_size).grid(
        row=2, columnspan=2, pady=5
    )

    text_area = Text(root, bg="lightgrey")
    text_area.grid(row=3, columnspan=2, padx=5, pady=5)

    text_area.bind("<FocusIn>", change_background_color)
    text_area.bind("<FocusOut>", change_background_color_out)

    width_entry.bind("<Return>", change_size)
    height_entry.bind("<Return>", change_size)

    root.mainloop()
