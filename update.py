# utkarsh
from tkinter import *
from tkinter import messagebox
import Message

class updates:
    def __init__(self,root,dbconnection,current_login):
        self.root=root
        self.dbconnection=dbconnection
        self.current_login=current_login
        self.color='#E2FFE6'
        self.update()

    def update(self):
        global fname
        global lname
        global uname
        global password
        global entry1
        global entry2
        global entry3
        global entry4
        fname=StringVar()
        lname=StringVar()
        uname=StringVar()
        password=StringVar()
        label1=Label(self.root,text="Enter new First Name :",font=('Arial',12,'bold')).place(x=50,y=150)
        entry1=Entry(self.root,textvariable=fname).place(x=250,y=150)
        button1=Button(self.root,text="Change first name",width=30,command=self.changeFname).place(x=400,y=150)
        label2=Label(self.root,text="Enter new Last Name :",font=('Arial',12,'bold')).place(x=50,y=200)
        entry2=Entry(self.root,textvariable=lname).place(x=250,y=200)
        button2=Button(self.root,text="Change last name",width=30,command=self.changeLname).place(x=400,y=200)
        label3=Label(self.root,text="Enter new username :",font=('Arial',12,'bold')).place(x=50,y=250)
        entry3=Entry(self.root,textvariable=uname).place(x=250,y=250)
        button3=Button(self.root,text="Change user name",width=30,command=self.changeUname).place(x=400,y=250)
        label4=Label(self.root,text="Enter new password :",font=('Arial',12,'bold')).place(x=50,y=300)
        entry4=Entry(self.root,textvariable=password).place(x=250,y=300)
        button4=Button(self.root,text="Change password",width=30,command=self.changePass).place(x=400,y=300)

    def changeFname(self):
        finame=fname.get()
        mycursor = self.dbconnection.cursor()
        variable=(finame,self.current_login,)
        query="update family set first_name=%s where member_id=%s"
        mycursor.execute(query,variable)
        self.dbconnection.commit()
        self.message("First Name changed successfully")
        self.root.destroy()


    def changeLname(self):
        laname=lname.get()
        mycursor = self.dbconnection.cursor()
        variable=(laname,self.current_login,)
        query="update family set last_name=%s where member_id=%s"
        mycursor.execute(query,variable)
        self.dbconnection.commit()
        messagebox.showerror("Updated")
        self.message("Last Name changed successfully")
        self.root.destroy()


    def changeUname(self):
        usname=uname.get()
        mycursor = self.dbconnection.cursor()
        variable=(usname,self.current_login,)
        query="update family set username=%s where member_id=%s"
        mycursor.execute(query,variable)
        self.dbconnection.commit()
        self.message("Username changed successfully")
        self.root.destroy()
        

    def changePass(self):
        pw=password.get()
        mycursor = self.dbconnection.cursor()
        variable=(pw,self.current_login,)
        query="update family set password=%s where member_id=%s"
        mycursor.execute(query,variable)
        self.dbconnection.commit()
        self.message("Password changed successfully")
        self.root.destroy()


    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window,self.color,message)
        new_window.wait_window()

