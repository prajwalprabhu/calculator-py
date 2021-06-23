import tkinter as tk
from tkinter.constants import *
from math import sqrt


class calculator():
    def __init__(self):
        root = tk.Tk()
        root.config(bg="#ff0000")
        root.title("Simple Calculator")
        root.iconbitmap("img\\tkicon.ico")
        tk.Label(root, text="Welcome to the World of calculation",
                 bg="#ffff00").pack()
        display = tk.Frame(root)
        display.pack(anchor="nw")
        self.e = tk.Entry(display)
        e = self.e
        e.pack()
        # e.insert(0,"Welcome To the Calculator")
        keys = tk.Frame(root)
        keys.config(bg="blue")

        keys.pack(side='left', padx=10, pady=10)

        tk.Button(keys, text=" 1 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(1)).grid(row=0, column=1)
        tk.Button(keys, text=" 2 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(2)).grid(row=0, column=2)
        tk.Button(keys, text=" 3 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(3)).grid(row=0, column=3)
        tk.Button(keys, text=" 4 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(4)).grid(row=1, column=1)
        tk.Button(keys, text=" 5 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(5)).grid(row=1, column=2)
        tk.Button(keys, text=" 6 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(6)).grid(row=1, column=3)
        tk.Button(keys, text=" 7 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(7)).grid(row=2, column=1)
        tk.Button(keys, text=" 8 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(8)).grid(row=2, column=2)
        tk.Button(keys, text=" 9 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(9)).grid(row=2, column=3)
        tk.Button(keys, text=" / ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click('/')).grid(row=0, column=4)
        tk.Button(keys, text=" * ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click('*')).grid(row=1, column=4)
        tk.Button(keys, text=" - ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click('-')).grid(row=2, column=4)
        tk.Button(keys, text=" + ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click('+')).grid(row=3, column=4)
        tk.Button(keys, text="  =  ", border=5, relief=RAISED, bg="blue", fg="white",
                  command=lambda: self.click('=')).grid(row=3, column=0, columnspan=1)
        tk.Button(keys, text=" . ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click('.')).grid(row=3, column=1)
        tk.Button(keys, text=" 0 ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click(0)).grid(row=3, column=2)
        tk.Button(keys, text="root", border=5, relief=RAISED, bg="blue",
                  fg="white", command=self.root_).grid(row=0, column=0)
        tk.Button(keys, text=" CE ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=self.all_clr).grid(row=1, column=0)
        tk.Button(keys, text=" AC ", border=5, relief=RAISED, bg="blue",
                  fg="white", command=self.all_clr).grid(row=2, column=0)
        tk.Button(keys, text="00", border=5, relief=RAISED, bg="blue",
                  fg="white", command=lambda: self.click('00')).grid(row=3, column=3)
        root.mainloop()

    def root_(self):
        e = self.e
        num = e.get()
        result = eval(num)
        root = sqrt(result)
        e.delete(0, END)
        e.insert(0, root)

    def all_clr(self):
        self.e.delete(0, END)

    def click(self, a):
        # if self.e[0]=='W':
        #     self.e.delete(0,END)
        self.num = self.e.get()
        self.e.insert(END, a)

        if a == "=":
            result = eval(self.num)
            self.e.delete(0, END)
            self.e.insert(0, result)


calculator()
