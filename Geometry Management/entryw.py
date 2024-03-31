import tkinter
from tkinter import *

root = tkinter.Tk()

root.title("Entry Widget")
root.resizable(False, False)
root.geometry("500x450+100+100")
root.configure(background="Black")

ent_w = Entry(root, font=('Arial', 12))
ent_w.pack(pady = 10)

ent_w = Entry(root, font=('Arial', 12))
ent_w.pack(pady = 20)

root.mainloop()