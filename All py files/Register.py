from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class RegisterForm:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1550x800+0+0")




# -----------------------------------------------------------variables-----------------------------------------


        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SwcurityA=StringVar()
        self.var_password=StringVar()
        self.var_conpassword=StringVar()
# ---------------------------------------------------------image---------------------------------------------
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sai\Desktop\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------------------------left image---------------------------------------------
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\sai\Desktop\hotel images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

# -----------------------------------------------------------frame------------------------------------------------
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        reg_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        reg_lbl.place(x=20,y=20)

        # ------------------------------------------------------labels and entrys----------------------------------------
        # ---------------------------row1------------------------------------------------------------------------
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=371,y=130,width=250)


        # -----------------------------------------row2---------------------------------------------------------------


        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email_lbl=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email_lbl.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)


        # -------------------------------row3---------------------------------------------------------------------
        security_qlbl=Label(frame,text="Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_qlbl.place(x=50,y=240)

        self.comb0_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.comb0_security_q["values"]=("Select","Your Birth Place","Your father Name","Your Pet Name")
        self.comb0_security_q.place(x=50,y=270,width=250)
        self.comb0_security_q.current(0)




        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)


        self.txt_security=ttk.Entry(frame,textvariable=self.var_SwcurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)




        # -----------------------------row4----------------------------------------------------------------------
        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_password,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd_lbl=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd_lbl.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_conpassword,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

 # ------------------------------------------------checkbutton-----------------------------------

        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & conditions",font=("times new roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
# --------------------------------buttons------------------------------------------


        img=Image.open(r"C:\Users\sai\Desktop\hotel images\register-now-button1.jpg")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        btn=Button(frame,image=self.photoimage,command=self.reg_data,borderwidth=0,cursor="hand2")
        btn.place(x=50,y=420,width=200)

        img1 = Image.open(r"C:\Users\sai\Desktop\hotel images\loginpng.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        btn1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        btn1.place(x=390, y=420, width=200)
    # --------------------------------------------------function deleclaration------------------------------

    def reg_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_password.get()!=self.var_conpassword.get():
            messagebox.showerror("Error","Password and Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Bhavesh123",database="hotel",auth_plugin="mysql_native_password")
            mycursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist ,please try another email")
            else:
                mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_SwcurityA.get(),
                                                                                    self.var_password.get()
                                                                                    ))
                conn.commit()
                conn.close()



if __name__=="__main__":
    root=Tk()
    obj=RegisterForm(root)
    root.mainloop()
