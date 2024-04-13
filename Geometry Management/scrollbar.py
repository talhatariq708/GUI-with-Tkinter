import tkinter
from tkinter import *

root = tkinter.Tk()

root.resizable(False,False)
root.geometry("500x350+300+100")
root.configure(background="Yellow")
root.title("Scroll Bar")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root,font=("Arial", 16), height=9)
listbox.pack()

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

for i in range(51):
    listbox.insert(END, i)

root.mainloop()