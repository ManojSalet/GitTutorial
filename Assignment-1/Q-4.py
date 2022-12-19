# Write a Python GUI program to create a Checkbutton widget using tkinter module
from tkinter import *
root = Tk()
root.geometry("300x300")

lblSport = Label(root,text="Choose Your Fevorite Sports").pack()
chkM = Checkbutton(root,text="Cricket").pack()
chkF = Checkbutton(root,text="Vollyball").pack()
chkF = Checkbutton(root,text="Kabbadi").pack()
chkF = Checkbutton(root,text="Football").pack()
chkF = Checkbutton(root,text="Basketball").pack()



root.mainloop()