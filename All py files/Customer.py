from tkinter import *
from PIL import Image,ImageTk
from  tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        # =================variables====================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()



        # ====================title====================
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=6,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=70)

        # =========================logo===============

        img2 = Image.open(r"C:\Users\sai\Desktop\hotel images\logohotel.png")
        img2 = img2.resize((230, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=9, width=90, height=58)

        # ==============lableframe========================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=2,y=65,width=425,height=490)

        # =================labels and entrys==============

        # ------------Cust Ref-------------
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",13,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman",13,"bold"))
        entry_ref.grid(row=0,column=1)

        # ------------------cust name-------------

        cname=Label(labelframeleft,font=("arial",13,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        # -----------------mother name------------

        mname=Label(labelframeleft,font=("arial",13,"bold"),text="Mother Name:",padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)

        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        # ----------gender combobox-------------


        label_gender=Label(labelframeleft,font=("arial",13,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)
        comb0_gender=ttk.Combobox(labelframeleft,textvariable= self.var_gender,font=("arial",13,"bold"),width=27,state=READABLE)

        comb0_gender["value"]=("Select","Male","Female","Other")
        comb0_gender.grid(row=3,column=1)
        comb0_gender.current(0)



        # -----------------postcode-----------------

        postcode=Label(labelframeleft,font=("arial",13,"bold"),text="PostCode:",padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)

        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtpostcode.grid(row=4,column=1)


        # -------------mobile number------------

        mobileno=Label(labelframeleft,font=("arial",13,"bold"),text="Mobile:",padx=2,pady=6)
        mobileno.grid(row=5,column=0,sticky=W)

        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtmobile.grid(row=5,column=1)


        # --------------------E-mail-------------------


        email=Label(labelframeleft,font=("arial",13,"bold"),text="Email:",padx=2,pady=6)
        email.grid(row=6,column=0,sticky=W)

        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)


        # -------------------------nationality-------------------

        nationality=Label(labelframeleft,font=("arial",13,"bold"),text="Nationality",padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality,font=("arial", 13, "bold"), width=27, state=READABLE)

        combo_nationality["value"] = ("Indian", "American", "British")
        combo_nationality.grid(row=7, column=1)

        # -------------------idproof type combobox---------------

        idproof=Label(labelframeleft,font=("arial",13,"bold"),text="Id Proof Type:",padx=2,pady=6)
        idproof.grid(row=8,column=0,sticky=W)

        combo_idproof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof,font=("arial", 13, "bold"), width=27, state=READABLE)

        combo_idproof["value"] = ("Aadhar Card", "DrivingLicence", "Passport")
        combo_idproof.grid(row=8, column=1)

        # -----------------------------Id number---------------------


        idno=Label(labelframeleft,font=("arial",13,"bold"),text="Id Number:",padx=2,pady=6)
        idno.grid(row=9,column=0,sticky=W)
        txtidno=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtidno.grid(row=9,column=1)



        # -----------------------------Address---------------------


        address=Label(labelframeleft,font=("arial",13,"bold"),text="Address:",padx=2,pady=6)
        address.grid(row=10,column=0,sticky=W)

        txtadd=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtadd.grid(row=10,column=1)

        # ===================btns=========================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)

        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update",command=self.Update_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1,padx=1)

        btnDelete = Button(btn_frame, text="Delete",command=self.delete, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2,padx=1)

        btnReset = Button(btn_frame, text="Reset",command=self.reset,font=("arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3,padx=1)

        # ==========table frame================================

        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and search system", padx=2,
                                    font=("times new roman", 12, "bold"))
        table_frame.place(x=435, y=61, width=860, height=490)

        lbl_search = Label(table_frame, font=("arial", 13, "bold"), text="Search By:", bg="red",fg="white")
        lbl_search.grid(row=6, column=0, sticky=W,padx=2)
        self.search_var=StringVar()
        combo_search = ttk.Combobox(table_frame,textvariable=self.search_var, font=("arial", 13, "bold"), width=24,state="readonly")

        combo_search["value"] = ("Mobile", "Ref")
        combo_search.grid(row=6,column=2,padx=2)
        self.txt_search=StringVar()
        txt_search = ttk.Entry(table_frame,textvariable=self.txt_search, font=("arial", 13, "bold"), width=24)
        txt_search.grid(row=6, column=3,padx=2)

        btnsearch = Button(table_frame, text="Search",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnsearch.grid(row=6, column=4, padx=1)

        btnshowall = Button(table_frame, text="Show All",command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnshowall.grid(row=6, column=5, padx=1)

        # =============show data table=========

        details_frame = Frame(table_frame, bd=2, relief=RIDGE)
        details_frame.place(x=0, y=50, width=860, height=350)

        scrollx=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scrolly=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.Cust_details_table=ttk.Treeview(details_frame,columns=("ref","name","mothername","gender","post","mobile","email","nationality","idproof","Id number","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.Cust_details_table.xview)
        scrolly.config(command=self.Cust_details_table.yview())


        self.Cust_details_table.heading("ref",text="Refer No")
        self.Cust_details_table.heading("name",text="Name")
        self.Cust_details_table.heading("mothername",text="Mother Name")
        self.Cust_details_table.heading("gender",text="Gender")
        self.Cust_details_table.heading("post",text="PostCode")
        self.Cust_details_table.heading("mobile",text="Mobile")
        self.Cust_details_table.heading("email",text="Email")
        self.Cust_details_table.heading("nationality",text="Nationality")
        self.Cust_details_table.heading("idproof",text="Id Proof")
        self.Cust_details_table.heading("Id number",text="Id Number")
        self.Cust_details_table.heading("address",text="Address")

        self.Cust_details_table["show"]="headings"

        self.Cust_details_table.column("ref",width=100)
        self.Cust_details_table.column("name",width=100)
        self.Cust_details_table.column("mothername",width=100)
        self.Cust_details_table.column("gender",width=100)
        self.Cust_details_table.column("post",width=100)
        self.Cust_details_table.column("mobile",width=100)
        self.Cust_details_table.column("email",width=100)
        self.Cust_details_table.column("nationality",width=100)
        self.Cust_details_table.column("idproof",width=100)
        self.Cust_details_table.column("Id number",width=100)
        self.Cust_details_table.column("address",width=100)

        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="Bhavesh123",database="hotel",auth_plugin="mysql_native_password")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                 self.var_ref.get(),
                                                                                 self.var_cust_name.get(),
                                                                                 self.var_mother.get(),
                                                                                 self.var_gender.get(),
                                                                                 self.var_post.get(),
                                                                                 self.var_mobile.get(),
                                                                                 self.var_email.get(),
                                                                                 self.var_nationality.get(),
                                                                                 self.var_id_proof.get(),
                                                                                 self.var_id_number.get(),
                                                                                 self.var_address.get()

                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","customer has been added",parent=self.root)
            except Exception as es:
               messagebox.showwarning("Warning",f"Something went Wrong:{(es)}")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cursor_row)
        row=content["values"]


        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def Update_data(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
        else:
            conn =mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            my_cursor.execute(" UPDATE customer SET Name=%s,Mother Name=%s,Gender=%s,PostCode=%s,,Mobile=%s,Email=%s,Nationality=%s,Id Proof=%s,Id Number=%s,Address=%s where Ref=%s",(                                                                                                                                                                                     self.var_cust_name.get(),
                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_mother.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                      ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","customers details has been updated successfully!!",parent=self.root)






    def delete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if mdelete>0:
            conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            my_cursor = conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):


        # self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        # self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        # self.var_nationality.set(""),
        # self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))


    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE'%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_details_table.delete(* self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()



if __name__==" __main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()