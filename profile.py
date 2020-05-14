# utkarsh
from tkinter import *
from update import *

def view(profile_screen,dbconnection,current_login):
    fname=getFirst_name(dbconnection,current_login)
    lname=getLast_name(dbconnection,current_login)
    uname=getUsername(dbconnection,current_login)
    label1=Label(profile_screen,text="Member ID : "+str(current_login),font=('Arial',12,'bold')).place(x=50,y=100)
    label1=Label(profile_screen,text="First Name :"+fname,font=('Arial',12,'bold')).place(x=50,y=150)
    label1=Label(profile_screen,text="Last Name :"+lname,font=('Arial',12,'bold')).place(x=50,y=200)
    label1=Label(profile_screen,text="username :"+uname,font=('Arial',12,'bold')).place(x=50,y=250)
    label1=Label(profile_screen,text="password : **********",font=('Arial',12,'bold')).place(x=50,y=300)

def getFirst_name(dbconnection,current_login):
    mycursor = dbconnection.cursor()
    variable=(current_login,)
    query="select first_name from family where member_id=%s"
    mycursor.execute(query,variable)
    name = mycursor.fetchone()
    return name[0]

def getLast_name(dbconnection,current_login):
    mycursor = dbconnection.cursor()
    variable=(current_login,)
    query="select last_name from family where member_id=%s"
    mycursor.execute(query,variable)
    name = mycursor.fetchone()
    return name[0]


def getUsername(dbconnection,current_login):
    mycursor = dbconnection.cursor()
    variable=(current_login,)
    query="select username from family where member_id=%s"
    mycursor.execute(query,variable)
    name = mycursor.fetchone()
    return name[0]






