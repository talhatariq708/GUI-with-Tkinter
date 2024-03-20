import tkinter
from tkinter import *
root = tkinter.Tk()
strN = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Choose Day"]
variable1 = StringVar(root)
dropdown1 = OptionMenu(root, variable1, *strN)
dropdown1.pack()
root.geometry("500x450")
root.configure(background="Yellow")
root.title("DropDown")
variable1.set("Choose Day")
root.mainloop()