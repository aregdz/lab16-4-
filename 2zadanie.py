#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def add_item(event=None):
    text = entry.get()
    if text:
        shopping_list.insert(END, text)
        entry.delete(0, END)


def copy_item(event):
    selected_index = shopping_list.curselection()
    if selected_index:
        text_to_copy = shopping_list.get(selected_index)
        entry.delete(0, END)
        entry.insert(END, text_to_copy)


if __name__ == "__main__":
    root = Tk()
    root.title("Перемещение и копирование элементов")

    entry = Entry(root)
    entry.pack(pady=5, padx=10, fill=X)
    entry.bind("<Return>", add_item)

    shopping_list = Listbox(root)
    shopping_list.pack(pady=5, padx=10, fill=BOTH, expand=True)
    shopping_list.bind("<Double-Button-1>", copy_item)

    root.mainloop()
