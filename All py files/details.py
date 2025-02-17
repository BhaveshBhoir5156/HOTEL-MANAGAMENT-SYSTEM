from tkinter import *
from PIL import Image,ImageTk
from  tkinter import ttk
import random
from time import strftime
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Detailsroom:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        # ====================title====================
        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=6,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=70)

        # =========================logo===============

        img2 = Image.open(r"C:\Users\sai\Desktop\hotel images\logohotel.png")
        img2 = img2.resize((230, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=9, width=90, height=58)

        # ==============lableframe========================

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=2, y=65, width=540, height=350)

        # -----------Floor-------------
        lbl_floor = Label(labelframeleft, text="Floor", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)


        self.var_floor=StringVar()
        entry_floor = ttk.Entry(labelframeleft,  width=20,textvariable=self.var_floor,font=("times new roman", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        # ------------Room No-------------
        lbl_RoomNo = Label(labelframeleft, text="Room No", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)
        self.var_roomNo=StringVar()
        entry_RoomNo = ttk.Entry(labelframeleft,  width=20,textvariable=self.var_roomNo,font=("times new roman", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # ------------Room Type-------------
        lbl_RoomType = Label(labelframeleft, text="Room Type", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)
        self.var_RoomType=StringVar()

        entry_RoomType = ttk.Entry(labelframeleft,  width=20,textvariable=self.var_RoomType,font=("times new roman", 13, "bold"))
        entry_RoomType.grid(row=2, column=1, sticky=W)


        # ===================btns=========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)

        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.Update_data(), font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete,font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset_data,font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3,padx=1)

        # ==========table frame================================

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room details", padx=2,
                                 font=("times new roman", 12, "bold"))
        table_frame.place(x=600, y=55, width=600, height=350)

        scrollx = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scrolly = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.roomtable = ttk.Treeview(table_frame, columns=(
        "floor", "roomno",  "roomType"), xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.roomtable.xview)
        scrolly.config(command=self.roomtable.yview())



        self.roomtable.heading("floor",text="Floor")
        self.roomtable.heading("roomno",text="Room No")
        self.roomtable.heading("roomType",text="Room Type")



        self.roomtable["show"]="headings"

        self.roomtable.column("floor",width=100)
        self.roomtable.column("roomno",width=100)
        self.roomtable.column("roomType",width=100)



        self.roomtable.pack(fill=BOTH,expand=1)
        self.roomtable.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123",
                                               database="hotel", auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_RoomType.get(),


                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "New Room has been added successfully !!!", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went Wrong:{(es)}")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",
                                       auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows:
                self.roomtable.insert("", END, values=i)
            conn.commit()
        conn.close()

# get cursor------------------------------
    def get_cursor(self, event=""):
            cursor_row = self.roomtable.focus()
            content = self.roomtable.item(cursor_row)
            row = content["values"]

            self.var_floor.set(row[0]),
            self.var_roomNo.set(row[1]),
            self.var_RoomType.set(row[2])


    def Update_data(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:
            conn =mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute(" update detail SET Floor=%s,RoomType=%s where RoomNo=%s",(


                                                                                                                                                                             self.var_floor.get(),
                                                                                                                                                                             self.var_RoomType.get(),
                                                                                                                                                                             self.var_roomNo.get(),

                                                                                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update"," New room details has been updated successfully!!",parent=self.root)




    def delete(self):
            mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room",parent=self.root)
            if mdelete > 0:
                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                query = "delete from details where RoomNo=%s"
                value = (self.var_roomNo.get(),)
                my_cursor.execute(query, value)
            else:
                if not mdelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()


    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")





if __name__==" __main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
