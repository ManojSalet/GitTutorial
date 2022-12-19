# Write a Python GUI program to create three radio buttons widgets using tkinter module. Display the value of checked radio button
from tkinter import *
root = Tk()
root.geometry("300x300")


rdb = IntVar


def Disp():
    radio = rdb.get()
    if(radio == "m"):
        l = Label(root,text=rdb1.cget("text")).pack()
    else:
        l = Label(root,text=rdb2.cget("text")).pack()
        


rdb1 = Radiobutton(root,text="Male",variable=rdb,value="m",command=Disp)
rdb1.deselect()
rdb1.pack()
rdb2 = Radiobutton(root,text="Female",variable=rdb,value="f",command=Disp)
rdb2.deselect()
rdb2.pack()


root.mainloop()