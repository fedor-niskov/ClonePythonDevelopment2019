#!/usr/bin/env python3
'''
Пример для первой лекции про TkInter

Закрытие окошка в постинтерактивном режиме
'''

from tkinter import *
import random

def load_colors(filepath):
    with open(filepath) as f:
        return [l.split()[3] for l in f.readlines()]

def dump(*args):
    print("DUMP:",args)

def repaint(label):
    # tkinter doesn't know about some colors
    ex = True
    while ex:
        try:
            label.configure(
                fg=random.sample(colors, 1),
                bg=random.sample(colors, 1)
            )
            ex = False
        except TclError:
            ex = True

def add_button_label(*args):
    global column_num
    b = Button(root, text="B")
    b.grid(row=0, column=column_num, rowspan=3, sticky=E+W+S+N)
    column_num += 1
    l = Label(root, text="L")
    l.grid(row=0, column=column_num, rowspan=3, sticky=E+W+S+N)
    column_num += 1
    b.configure(command = lambda label=l : repaint(l) )


colors = load_colors("rgb.txt")

TKroot = Tk()
TKroot.title("Hello")

root = Frame(TKroot)
root.pack(fill=BOTH, expand=1)

column_num = 2

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)

Add = Button(root, text="Add")
Add.bind('<Button-1>', add_button_label)
Add.grid(row=0, column=0, sticky=E+W)
Exit = Button(root, text="Exit", command=root.quit)
Exit.grid(row=0, column=1, sticky=E+W)
Txt = Label(root, text="This is a label", bg="PeachPuff")
Txt.grid(row=1, column=0, columnspan=2, sticky=E+W+N)

TKroot.mainloop()
print("Done")
#root.destroy()
