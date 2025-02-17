from tkinter import *
from PIL import Image,ImageTk
from  tkinter import ttk
import random
from time import strftime
from time import strptime
from datetime import datetime
import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # -------------variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


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

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", padx=2,
                                    font=("times new roman", 12, "bold"))
        labelframeleft.place(x=2, y=65, width=425, height=490)

        # ------------Customer contact-------------
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=("arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0,sticky=W)

        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, width=20, font=("times new roman", 13, "bold"))
        entry_contact.grid(row=0, column=1,sticky=W)


        # fetch data button-------------------------------------------
        btnfetchdata=Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)

        btnfetchdata.place(x=350,y=4)

        # ------------------Check in date-------------

        check_in_date = Label(labelframeleft, font=("arial", 13, "bold"), text="Check in Date", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheckindate = ttk.Entry(labelframeleft, textvariable=self.var_checkin,font=("arial", 13, "bold"), width=29)
        txtcheckindate.grid(row=1, column=1)

        # ------------------Check out date-------------

        checkoutdate = Label(labelframeleft, font=("arial", 13, "bold"), text="Check Out Date", padx=2, pady=6)
        checkoutdate.grid(row=2, column=0, sticky=W)

        txtcheckoutdate = ttk.Entry(labelframeleft,textvariable=self.var_checkout, font=("arial", 13, "bold"), width=29)
        txtcheckoutdate.grid(row=2, column=1)

        # ----------Room Type-------------

        room_type = Label(labelframeleft, font=("arial", 13, "bold"), text="Room Type", padx=2, pady=6)
        room_type.grid(row=4, column=0, sticky=W)
        combo_roomtype = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype,font=("arial", 13, "bold"), width=27,
                                    state=READABLE)

        combo_roomtype["value"] = ("Single", "Double", "Luxary")
        combo_roomtype.grid(row=4, column=1)

        # -----------------Avaliable Room-----------------

        avaliableroom = Label(labelframeleft, font=("arial", 13, "bold"), text="Avaliable Room", padx=2, pady=6)
        avaliableroom.grid(row=5, column=0, sticky=W)

        txtavaliablerroom = ttk.Entry(labelframeleft,textvariable=self.var_roomavailable, font=("arial", 13, "bold"), width=29)
        txtavaliablerroom.grid(row=5, column=1)

        # ----------------Meal-----------------

        meal = Label(labelframeleft, font=("arial", 13, "bold"), text="Meal", padx=2, pady=6)
        meal.grid(row=6, column=0, sticky=W)

        txtmeal = ttk.Entry(labelframeleft,textvariable=self.var_meal, font=("arial", 13, "bold"), width=29)
        txtmeal.grid(row=6, column=1)

        # -----------------No of days-----------------

        Noofdays = Label(labelframeleft, font=("arial", 13, "bold"), text="No Of Days", padx=2, pady=6)
        Noofdays.grid(row=7, column=0, sticky=W)

        txtnoofdays = ttk.Entry(labelframeleft,textvariable=self.var_noofdays, font=("arial", 13, "bold"), width=29)
        txtnoofdays.grid(row=7, column=1)

        # -----------------Paid Tax-----------------

        PaidTax = Label(labelframeleft, font=("arial", 13, "bold"), text="Paid Tax", padx=2, pady=6)
        PaidTax.grid(row=8, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=8, column=1)

        # -----------------Subcost-----------------

        Subcost = Label(labelframeleft, font=("arial", 13, "bold"), text="Sub Cost", padx=2, pady=6)
        Subcost.grid(row=9, column=0, sticky=W)

        txtSubcost = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal,font=("arial", 13, "bold"), width=29)
        txtSubcost.grid(row=9, column=1)

        # -----------------Total cost-----------------

        Totalcost = Label(labelframeleft, font=("arial", 13, "bold"), text="Total cost", padx=2, pady=6)
        Totalcost.grid(row=10, column=0, sticky=W)

        txttotalcost = ttk.Entry(labelframeleft, textvariable=self.var_total,font=("arial", 13, "bold"), width=29)
        txttotalcost.grid(row=10, column=1)


        # ----------------btn bill-------------


        btnbill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=9)

        btnbill.grid(row=11,column=0,padx=1,sticky=W)


        # ===================btns=========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)

        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.Update_data(), font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.delete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3,padx=1)


        # ------------right side image-----------

        img3 = Image.open(r"C:\Users\sai\Desktop\hotel images\bed.jpg")
        img3 = img3.resize((520, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=65, width=520, height=200)
        # ==========table frame================================

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and search system", padx=2,
                                 font=("times new roman", 12, "bold"))
        table_frame.place(x=435, y=280, width=860, height=260)

        lbl_search = Label(table_frame, font=("arial", 13, "bold"), text="Search By:", bg="red", fg="white")
        lbl_search.grid(row=6, column=0, sticky=W, padx=2)
        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 13, "bold"), width=24,
                                    state="readonly")

        combo_search["value"] = ("Contact","Room")
        combo_search.grid(row=6, column=2, padx=2)
        self.txt_search = StringVar()
        txt_search = ttk.Entry(table_frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txt_search.grid(row=6, column=3, padx=2)

        btnsearch = Button(table_frame, text="Search",command=self.search, font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=9)
        btnsearch.grid(row=6, column=4, padx=1)

        btnshowall = Button(table_frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"),
                            bg="black", fg="gold", width=9)
        btnshowall.grid(row=6, column=5, padx=1)




        # =============show data table=========

        details_frame = Frame(table_frame, bd=2, relief=RIDGE)
        details_frame.place(x=0, y=50, width=860, height=180)

        scrollx=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.roomtable=ttk.Treeview(details_frame,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noofdays","nationality","idproof","Id number","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.roomtable.xview)
        scrolly.config(command=self.roomtable.yview())


        self.roomtable.heading("contact",text="Contact")
        self.roomtable.heading("checkin",text="Check-In")
        self.roomtable.heading("checkout",text="Check-Out")
        self.roomtable.heading("roomtype",text="Room Type")
        self.roomtable.heading("roomavailable",text="Room No")
        self.roomtable.heading("meal",text="Meal")
        self.roomtable.heading("noofdays",text="NoOfDays")


        self.roomtable["show"]="headings"

        self.roomtable.column("contact",width=100)
        self.roomtable.column("checkin",width=100)
        self.roomtable.column("checkout",width=100)
        self.roomtable.column("roomtype",width=100)
        self.roomtable.column("roomavailable",width=100)
        self.roomtable.column("meal",width=100)
        self.roomtable.column("noofdays",width=100)


        self.roomtable.pack(fill=BOTH,expand=1)
        self.roomtable.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
            if self.var_contact.get() == "" or self.var_checkin.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123",
                                                   database="hotel", auth_plugin="mysql_native_password")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                                            self.var_contact.get(),
                                                                                            self.var_checkin.get(),
                                                                                            self.var_checkout.get(),
                                                                                            self.var_roomtype.get(),
                                                                                            self.var_roomavailable.get(),
                                                                                            self.var_meal.get(),
                                                                                            self.var_noofdays.get()


                                                                                         ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "room has been added", parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning", f"Something went Wrong:{(es)}")
# -------------fetch data----------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
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

            self.var_contact.set(row[0]),
            self.var_checkin.set(row[1]),
            self.var_checkout.set(row[2]),
            self.var_roomtype.set(row[3]),
            self.var_roomavailable.set(row[4]),
            self.var_meal.set(row[5]),
            self.var_noofdays.set(row[6])



    def Update_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn =mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute(" UPDATE room SET check_in=%s,check_out=%s,roomtype=%s,,roomavailable=%s,meal=%s,Noofdays=%s where Contact=%s",(


                                                                                                                                            self.var_checkin.get(),
                                                                                                                                            self.var_checkout.get(),
                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                            self.var_roomavailable.get(),
                                                                                                                                            self.var_meal.get(),
                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                            self.var_contact.get()

                                                                                                                                             ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","room details has been updated successfully!!",parent=self.root)

    def delete(self):
            mdelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room",parent=self.root)
            if mdelete > 0:
                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor()
                query = "delete from room where Contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
            else:
                if not mdelete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

        # ---------all data fetch-----------------


    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter contact number",parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor(buffered=True)
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showdataframe.place(x=430,y=55,width=300,height=180)
                lblname=Label(showdataframe,text="Name:",font=("arial",12,"bold"))
                lblname.place(x=0,y=0)
                lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
     # ------------------Gender-------------------------
                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblgender = Label(showdataframe, text="Gender:", font=("arial", 12, "bold"))
                lblgender.place(x=0, y=30)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=30)

    # ---------------------------Email-----------------------------

                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblemail = Label(showdataframe, text="Email:", font=("arial", 12, "bold"))
                lblemail.place(x=0, y=60)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=60)


                # ----------------Nationality-------------------

                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblnation = Label(showdataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblnation.place(x=0, y=90)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=90)


                # ---------------------------Address--------------------

                conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",
                                               auth_plugin="mysql_native_password")
                my_cursor = conn.cursor(buffered=True)
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lbladd = Label(showdataframe, text="Address", font=("arial", 12, "bold"))
                lbladd.place(x=0, y=120)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=120)

                # -----------search system------------

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE'%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.roomtable.delete(*self.roomtable.get_children())
            for i in rows:
                self.roomtable.insert("", END, values=i)
            conn.commit()
        conn.close()

    def total(self):
        inDate=self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)


        if(self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxary"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)

            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        # elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
        #     q1=float(300)
        #     q2=float(700)
        #     q3=float(self.var_noofdays.get())
        #     q4=float(q1+q2)
        #     q5=float(q3+q4)
        #
        #     Tax="Rs."+str("%.2f"%((q5)*0.1))
        #     ST="Rs."+str("%.2f"%((q5)))
        #     TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
        #     self.var_paidtax.set(Tax)
        #     self.var_actualtotal.set(ST)
        #     self.var_total.set(TT)


        # elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
        #     q1 = float(300)
        #     q2 = float(700)
        #     q3 = float(self.var_noofdays.get())
        #     q4 = float(q1 + q2)
        #     q5 = float(q3 + q4)
        #
        #     Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
        #     ST = "Rs." + str("%.2f" % ((q5)))
        #     TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
        #     self.var_paidtax.set(Tax)
        #     self.var_actualtotal.set(ST)
        #     self.var_total.set(TT)


        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxary"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxary"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1 + q2)
            q5 = float(q3 + q4)

            Tax = "Rs." + str("%.2f" % ((q5) * 0.1))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5 + ((q5) * 0.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)




if __name__==" __main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
