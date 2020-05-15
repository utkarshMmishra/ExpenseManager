# utkarsh
from tkinter import *
from LogInPage import *
from tkinter import messagebox
import time
import Message

class MainPage:
    def __init__(self, parent, root, height, width, side, color, dbconnection):
        self.parent = parent
        self.root = root
        self.height = height
        self.width = width
        self.side = side
        self.font = ('Times', 12, 'roman')
        self.color = color
        self.dbConnection = dbconnection
        self.frame = None
        self.loginButton=None
        self.gui_init()

    def gui_init(self):
        self.frame = Frame(
            self.root,
            cursor='arrow',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)
        self.frame.propagate(0)
        self.frame.pack(expand=True, side=self.side, fill=BOTH)

        frame1 = Frame(
            self.frame,
            cursor='arrow',
            bg=self.color,
            height=self.height / 3,
            width=self.width * 2 / 3)
        frame1.propagate(0)
        frame1.pack(expand=True, fill=BOTH)
        frame1.place(relx=0.5, rely=0.5, anchor='center')

        Label(text="").pack()
        self.loginButton = Button(frame1, text="Login", font=self.font)
        self.loginButton.bind("<Button>", LoginFrame(self.parent,self.root,
            self.height,self.width,self.side,self.color,self.dbConnection))
        Label(text="").pack()
        Button(frame1,text="Sign-Up",height="3",width=30,command=self.register).pack()

    def register(self):
        self.register_screen=Toplevel(self.root)
        self.register_screen.title("Sign-Up")
        self.register_screen.geometry("750x500")
        global username
        global password
        global member_id
        global first_name
        global last_name
        global username_entry
        global password_entry
        global member_id_entry
        global last_name_entry
        global first_name_entry
        username=StringVar()
        password=StringVar()
        member_id=IntVar()
        last_name=StringVar()
        first_name=StringVar()
        Label(self.register_screen,text="Please enter details below",bg='blue').pack()
        Label(self.register_screen,text="").pack()
        member_id_lable=Label(self.register_screen,text="Member Id :").pack()
        member_id_entry=Entry(self.register_screen,textvariable=member_id).pack()
        first_name_lable=Label(self.register_screen,text="First Name :").pack()
        first_name_entry=Entry(self.register_screen,textvariable=first_name).pack()
        last_name_lable=Label(self.register_screen,text="Last Name :").pack()
        last_name_entry=Entry(self.register_screen,textvariable=last_name).pack()

        username_lable=Label(self.register_screen,text="Username :")
        username_lable.pack()
        username_entry=Entry(self.register_screen,textvariable=username)
        username_entry.pack()
        password_lable=Label(self.register_screen,text="Password :")
        password_lable.pack()
        password_entry=Entry(self.register_screen,textvariable=password,show='*')
        password_entry.pack()
        Label(self.register_screen,text="").pack()
        Button(self.register_screen,text="Register",width=10,height=1,command=self.register_user).pack()

    def register_user(self):
        username_info=username.get()
        password_info=password.get()
        member_id_info=member_id.get()
        first_name_info=first_name.get()
        last_name_info=last_name.get()
        mycursor = self.dbConnection.cursor()
        query1 = "select member_id from family"
        variable = (username,)
        mycursor.execute(query1)
        username_list = mycursor.fetchall()
        final_username_list = []
        for i in range(len(username_list)):
            final_username_list.append(username_list[i][0])
        try:
            if member_id_info in final_username_list:
                messagebox.showerror("Error","Entered member id is registered")
            elif len(password_info)<=7:
                messagebox.showerror("Error","Enter a password of size 8")
            else:
                val=self.validate(password_info)
                if val==True:
                    self.insert_family(member_id_info,first_name_info,last_name_info,username_info,password_info)
                    self.insert_income(member_id_info)
                    self.message("Signed Up successfully")
                    
                    self.register_screen.destroy()

        except Exception as e:
            messagebox.showerror(e)

    def insert_family(self,member_id,first_name,last_name,username,password):
        mycursor = self.dbConnection.cursor()
        query1 = "insert into family (member_id,first_name,last_name,username,password) values(%s,%s,%s,%s,%s)"
        record=(member_id,first_name,last_name,username,password)
        mycursor.execute(query1,record)
        self.dbConnection.commit()

    def insert_income(self,member_id):
        mycursor = self.dbConnection.cursor()
        category = '0'
        amount = '0'
        comments = 'None'
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        query = "insert into income (member_id, income_category_id, income_date, amount, comments) values (%s, %s, " \
                "%s, %s, %s) "
        values = (member_id, category, current_time, amount, comments)
        mycursor.execute(query, values)
        self.dbConnection.commit()

    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()

    def validate(self,password):
        SpecialSym=['@','#','$','&','*']
        return_val=True
        if not any(char.isdigit() for char in password):
            self.message("The password should have at least\none numeral")
            return_val=False
        if not any(char.isupper() for char in password):
            self.message("The password should have at least\none uppercase letter")
            return_val=False
        if not any(char.islower() for char in password):
            self.message("The password should have at least\none lowercase letter")
            return_val=False
        if not any(char in SpecialSym for char in password):
            self.message("The password should have at least\none special symbols")
            return_val=False
        return return_val


