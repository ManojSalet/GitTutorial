# Write a Python GUI program to create a Listbox bar widgets using tkinter module
from tkinter import *
root = Tk()
root.geometry("300x300")

l = Listbox(root)
l.insert(1,"Apple")
l.insert(2,"Samsung")
l.insert(3,"Vivo")
l.insert(4,"Oppo")
l.pack()




root.mainloop()