import tkinter
from tkinter import *

root = tkinter.Tk()

root.title("Pack")
root.configure(background="Yellow")
root.geometry("500x450+400+100")

btn1 = Button(root, text="Button 1")
btn1.pack(fill = X)

btn2 = Button(root, text="Button 2")
btn2.pack(fill=BOTH, expand=TRUE)

btn3 = Button(root, text="Button 3")
btn3.pack()

root.mainloop()
