# Write a Python GUI program to add a button in your application using tkinter module.
from tkinter import *
root = Tk()
root.geometry("500x500")
b1 = Button(root,text="Click me",bg="#ff9900").pack()

root.mainloop()