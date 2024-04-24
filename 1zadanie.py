#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *


def move_items(from_list, to_list):
    selected_items = list(from_list.curselection())
    selected_items.reverse()
    for index in selected_items:
        to_list.insert(END, from_list.get(index))
        from_list.delete(index)


def move_to_shopping_list():
    move_items(available_items, shopping_list)


def move_back_to_available():
    move_items(shopping_list, available_items)


if __name__ == "__main__":
    root = Tk()
    root.title("Список товаров и покупок")

    available_items = Listbox(root, selectmode=MULTIPLE)
    available_items.pack(side=LEFT, padx=5, pady=5)
    available_items.insert(END, "Яблоки")
    available_items.insert(END, "Бананы")
    available_items.insert(END, "Молоко")
    available_items.insert(END, "Хлеб")
    available_items.insert(END, "Масло")

    shopping_list = Listbox(root, selectmode=MULTIPLE)
    shopping_list.pack(side=LEFT, padx=5, pady=5)

    button_frame = Frame(root)
    button_frame.pack(side=LEFT, padx=5, pady=5)
    Button(
        button_frame, text="Добавить в список", command=move_to_shopping_list
    ).pack(fill=X)
    Button(
        button_frame, text="Удалить из списка", command=move_back_to_available
    ).pack(fill=X)

    root.mainloop()
