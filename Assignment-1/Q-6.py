# Write a Python GUI program to create three single line text-box to accept a value from the user using tkinter module.
from tkinter import *

root = Tk()
root.geometry("300x300")


txt = Entry(root).pack()
txt1 = Entry(root).pack()
txt2 = Entry(root).pack()

root.mainloop()