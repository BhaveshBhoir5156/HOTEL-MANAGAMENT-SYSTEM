from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import  messagebox
import mysql

def main():
    win=Tk()
    obj=LoginSystem(win)
    win.mainloop()

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\sai\Desktop\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg=Label(root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)


        fraame=Frame(self.root,bg="black")
        fraame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\sai\Desktop\hotel images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        img1_lbl=Label(image=self.photoimage1,bg="black",borderwidth=0)
        img1_lbl.place(x=730,y=175,width=100,height=100)

        get_str=Label(fraame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # -----------------------------------------------------------variables-----------------------------------------

        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_SwcurityA = StringVar()
        self.var_password = StringVar()
        self.var_conpassword = StringVar()

#labels

        username=lbl=Label(fraame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(fraame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)


        password=lbl=Label(fraame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)

        self.txtword=ttk.Entry(fraame,font=("times new roman",15,"bold"))
        self.txtword.place(x=40,y=250,width=270)


# --------------------icon images--------------

        img2=Image.open(r"hotel images/LoginIconAppl.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        img1_lbl=Label(image=self.photoimage2,bg="black",borderwidth=0)
        img1_lbl.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r"hotel images/lock-512.png")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        img1_lbl=Label(image=self.photoimage3,bg="black",borderwidth=0)
        img1_lbl.place(x=650,y=395,width=25,height=25)

# ----------------------------------loginButton------------------------------------
        loginbtn=Button(fraame,command=self.Login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

# -------------------register button---------------------------------------------------
        regbtn=Button(fraame,text="New User Register",command=self.reg_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=15,y=350,width=160)

# forget password btn----------------------------------------------------------------------

        forgotbtn=Button(fraame,text="Forget Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgotbtn.place(x=10,y=370,width=160)
    def reg_window(self):
        self.new_window=Toplevel(self.root)
        self.obj=RegisterForm(self.new_window)

    def Login(self):
        if self.txtuser.get()=="" or self.txtword.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.txtuser.get()=="Bhavesh@123" and self.txtword.get()=="1234":
            messagebox.showinfo("Success","Welcome to Grand Hotel")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            mycursor = conn.cursor()
            mycursor.execute("select * from register where email=%s and password=%s",(
                                                                            self.var_email.get(),
                                                                            self.var_password.get()

                                                                       ) )

            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("Yes /No","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.obj=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

            # ------------------------------Reset Password----------------------------------------

    def reset_password(self):
        if self.comb0_security_q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_password.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            mycursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.comb0_security_q.get(),self.txt_security.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("Update register set password=%s where email=%s")
                value=(self.txt_password.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()

                messagebox.showinfo("Info","Your password has been reset ,please login new password",parent=self.root2)

                self.root2.destroy()

# -------------------------------------------forgot password window-------------------------------

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter The Email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Bhavesh123", database="hotel",auth_plugin="mysql_native_password")
            mycursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror("Error","Please Enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                L=Label(self.root2,text="Forgot Password",font=("times new roman",12,"bold"),fg="red",bg="white")
                L.place(x=0,y=10,relwidth=1)

                security_qlbl = Label(self.root2, text="Security Questions", font=("times new roman", 15, "bold"),
                                      bg="white", fg="black")
                security_qlbl.place(x=50, y=80)

                self.comb0_security_q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15, "bold"), state="readonly")
                self.comb0_security_q["values"] = ("Select", "Your Birth Place", "Your father Name", "Your Pet Name")
                self.comb0_security_q.place(x=50, y=110, width=250)


                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                                   fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2,  font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)


                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_password = ttk.Entry(self.root2,  font=("times new roman", 15))
                self.txt_password.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_password,font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)



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
        self.bg=ImageTk.PhotoImage(file=r"hotel images/0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------------------------left image---------------------------------------------
        self.bg1 = ImageTk.PhotoImage(file=r"hotel images/thought-good-morning-messages-LoveSove.jpg")
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
        btn1 = Button(frame, image=self.photoimage1,command=self.return_login, borderwidth=0, cursor="hand2")
        btn1.place(x=390, y=420, width=200)
    # --------------------------------------------------function declaration------------------------------

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

    def return_login(self):
        self.root.destroy()

from tkinter import *
from PIL import Image,ImageTk
from Customer import Cust_Win
from room import Roombooking
from details import Detailsroom
from REPORT import report
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ==================1st image=======================
        img1=Image.open(r"C:\Users\sai\Desktop\hotel images\hotel1.png")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)


        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        # =========================logo===========================
        img2 = Image.open(r"C:\Users\sai\Desktop\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # ===========================title================================

        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)


        # =============================main frame===========================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)

        # ===============================menu================================

        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)


        # ==============================btn frame=================================

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0)


        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0)


        details_btn=Button(btn_frame,text="DETAILS",command=self.detailsroom,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0)

        report_btn=Button(btn_frame,text="REPORT",command=self.report,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0)


        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0)


        # ===========================RIGHT SIDE IMAGE=============

        img3 = Image.open(r"hotel images/slide3.jpg")
        img3 = img3.resize((1310,590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)


        # =========down images=======================================

        img4 = Image.open(r"C:\Users\sai\Desktop\hotel images\myh.jpg")
        img4 = img4.resize((225, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(self.root, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=400, width=230, height=210)

        img5 = Image.open(r"C:\Users\sai\Desktop\hotel images\khana.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(self.root, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=600, width=230, height=190)


    def cust_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Cust_Win(self.new_window)

    def roombooking(self):
            self.new_window=Toplevel(self.root)
            self.app=Roombooking(self.new_window)



    def detailsroom(self):
            self.new_window=Toplevel(self.root)
            self.app=Detailsroom(self.new_window)

    def report(self):
        self.new_window=Toplevel(self.root)
        self.app=report(self.new_window)


    def logout(self):
        self.root.destroy()

if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()


if __name__=="__main__":
    main()

