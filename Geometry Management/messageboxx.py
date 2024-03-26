import tkinter
from tkinter import messagebox

root = tkinter.Tk()

root.title("messagebox")
root.configure(background="Light Blue")
root.geometry("300x250+200+100")
root.resizable(False, False)

messagebox.showinfo("info", "Welcome")
messagebox.showerror("error", "ERROR")
messagebox.showwarning("error", "window is not opening!")

root.mainloop()