# Write a Python GUI program to create two buttons exit and hello using tkinter module. Whne click on exit application must close.
from tkinter import *
root = Tk()


b1 = Button(root,text="Hello").pack()

def Close():
    root.destroy()
b2 = Button(root,text="Exit",command=Close).pack()



root.mainloop()