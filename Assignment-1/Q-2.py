# Write a python program to take two input from the users and display in label using tkinter module.
from tkinter import *
root = Tk()
root.geometry("500x500")
Fname = StringVar();
Sname = StringVar();

def Disp():
    lName = Label(root,text=Fname.get() + " " + Sname.get())
    lName.grid(row=6,column=3)
l1 = Label(root,text="Enter First Name :")
l1.grid(row=0,column=0)
e = Entry(root,textvariable=Fname)
e.grid(row=0,column=1)
l2 = Label(root,text="Enter Second Name :")
l2.grid(row=1,column=0)
e2 = Entry(root,textvariable=Sname)
e2.grid(row=1,column=1)

b1 = Button(root,text="Display",command=Disp)
b1.grid(row=3,column=3)



root.mainloop()