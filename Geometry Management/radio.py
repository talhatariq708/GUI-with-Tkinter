import tkinter
from tkinter import *

root = tkinter.Tk()

root.title("Radio Button")
root.geometry("230x200+200+60")
root.configure(background="Yellow")
root.resizable(False, False)

V = IntVar()

Radiobutton(root, text="Male", value=1).pack()
Radiobutton(root, text="Female", value=2).pack()

root.mainloop()