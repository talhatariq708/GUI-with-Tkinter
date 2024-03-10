import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("Place")
root.resizable(False, False)
root.config(background="#975353")
root.geometry("500x450+400+100")

btn1 = Button(root, text="Button 1")
btn1.place(x=0, y=0)

btn2 = Button(root, text="Button 2")
btn2.place(x=20, y=50)

btn3 = Button(root, text="Button 3")
btn3.place(x=40, y=100)

root.mainloop()