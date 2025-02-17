from tkinter import *
from PIL import Image,ImageTk
from  tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class report:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        L1=Label(self.root,text='Give Your Feed Back Below',font=("times new roman",20,"bold"),fg="red",bg="white")
        L1.pack(anchor=CENTER)


        text=Text(self.root)
        text.pack()

        btn=Button(self.root,text="Submit",command=self.submit,font=("times new roman",20,"bold"),fg="red",bg="white")
        btn.pack()

    def submit(self):
        messagebox.showinfo("Thank You","Thank You for your feed back")








if __name__==" __main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()