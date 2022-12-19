# Write a Python GUI program to create a Text widget using tkinter module.
from tkinter import *
root = Tk()
root.geometry("300x300")

Info = "Hii My Name Is Manoj And I am a Stundet"

Txt = Text(root)
Txt.insert(Txt)
Txt.pack()



root.mainloop()