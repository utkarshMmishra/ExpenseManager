# utkarsh
from tkinter import *
from tkinter import messagebox
import Message

class deleteAE:
    def __init__(self,root,dbconnection,current_login):
        self.root=root
        self.dbconnection=dbconnection
        self.current_login=current_login
        self.color='#E2FFE6'
        self.confirm()


    def confirm(self):
        global choice
        global e1
        choice=StringVar()
        label1=Label(self.root,text="Do you want to delete all expense (Y/N) :",font=('Arial',12,'bold')).place(x=50,y=150)
        e1=Entry(self.root,textvariable=choice).place(x=400,y=150)
        button1=Button(self.root,text="Delete",width=30,command=self.removeAllexpense).place(x=550,y=150)

    def removeAllexpense(self):
        ch=choice.get()
        if ch=='Y' or ch=='y':
            mycursor = self.dbconnection.cursor()
            variable=(self.current_login,)
            query="delete from expense where member_id=%s"
            mycursor.execute(query,variable)
            self.dbconnection.commit()
            self.message("All Expense deleted successfully")
            self.root.destroy()
        elif (ch=='N' or ch=='n'):
            self.message("As you wish")
            self.root.destroy()
        elif ch!='Y' or ch!='y' or ch!='N' or ch!='n':
            self.message("Invalid")
    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window,self.color,message)
        new_window.wait_window()
