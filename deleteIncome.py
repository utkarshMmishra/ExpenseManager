# utkarsh
from tkinter import *
from tkinter import messagebox
import Message

class deleteI:
    def __init__(self,root,dbconnection,current_login):
        self.root=root
        self.dbconnection=dbconnection
        self.current_login=current_login
        self.color='#E2FFE6'
        self.enterIno()

    def enterIno(self):
        global num
        global e1
        num=StringVar()
        label1=Label(self.root,text="Enter income number you want to delete :",font=('Arial',12,'bold')).place(x=50,y=150)
        e1=Entry(self.root,textvariable=num).place(x=400,y=150)
        button1=Button(self.root,text="Delete",width=30,command=self.removeE).place(x=550,y=150)

    def removeE(self):
        no=num.get()
        mycursor = self.dbconnection.cursor()
        variable=(no,)
        query="delete from income where income_id=%s"
        mycursor.execute(query,variable)
        self.dbconnection.commit()
        self.message("Income deleted successfully ")
        self.root.destroy()



    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window,self.color,message)
        new_window.wait_window()