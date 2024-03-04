import tkinter
from tkinter import *
root = tkinter.Tk()
root.geometry("500x400+500+100")
root.title("Geometry")
root.config(background="yellow")
root.resizable(False,False)

btn1 = Button(root, text="Button 1")
btn1.grid(row = 0, column = 2)

btn1 = Button(root, text="Button 1")
btn1.grid(row = 1, column = 2)

btn1 = Button(root, text="Button 1")
btn1.grid(row = 2, column = 2)

root.mainloop()
