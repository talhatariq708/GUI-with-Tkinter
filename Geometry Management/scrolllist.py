import tkinter
from tkinter import *

root = tkinter.Tk()

root.configure(background="Yellow")
root.title("Scroll List")
root.geometry("500x450+300+100")
root.resizable(False,False)

scroll_List = Listbox(root, font=("Arial", 16), height=4)
scroll_List.pack()

scroll_List.insert(0, "Sample 1")
scroll_List.insert(1, "Sample 2")
scroll_List.insert(2, "Sample 3")
scroll_List.insert(3, "Sample 4")
scroll_List.insert(4, "Sample 5")
scroll_List.insert(5, "Sample 6")
scroll_List.insert(6, "Sample 7")
scroll_List.insert(7, "Sample 8")


root.mainloop()