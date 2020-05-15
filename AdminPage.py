# Dashboard
from tkinter import *
from tkinter import ttk

from profile import *
from NewExpense import *
from NewIncome import *
from update import *
from deleteAccount import *
from deleteExpense import *
from deleteIncome import *
from delAllincome import *
from delAllexpense import *


class AdminPage:
    def __init__(self, root, color, font, dbconnection, width, current_login):

        for child in root.winfo_children():
            child.destroy()

        self.root = root
        
        
        self.dbconnection = dbconnection
        self.current_login = current_login
        self.color = color
        self.font = font
        self.screen_width = self.root.winfo_screenwidth() * 3 / 4
        self.screen_height = self.root.winfo_screenheight() * 3 / 4
        self.width = width

        # utkarsh
        self.menubar=Menu(self.root)
        self.root.config(menu=self.menubar)
        self.filemenu=Menu(self.root,tearoff=0)
        self.filemenu.add_command(label="Profile",command=self.profile)
        self.filemenu.add_command(label="Update",command=self.update)
        self.filemenu.add_command(label="Delete Income",command=self.deleteI)
        self.filemenu.add_command(label="Delete Expense",command=self.deleteE)
        self.filemenu.add_command(label="Delete All Income",command=self.deleteAI)
        self.filemenu.add_command(label="Delete All Expense",command=self.deleteAE)
        self.filemenu.add_command(label="Delete Account",command=self.delete)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=root.destroy)
        self.menubar.add_cascade(label="Menu",menu=self.filemenu)

        self.gui_init()
        self.up_frame = 0
        self.dashBoard = 0
        self.logoutFrame = 0
        self.income = 0
        self.expense = 0
        self.balance = 0
        self.addNewExpenseButton = 0
        self.addNewIncomeButton = 0
        self.family_expenses = 0
        self.family_income = 0

    def gui_init(self):
        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#3368FF',
            height=self.screen_height * 1 / 8,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, fill=BOTH)
        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg='#120C2C',
            height=self.screen_height * 6 / 8,
            relief=RAISED,
            bd=5,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.display()
        self.print_expenses(self.down_frame)
        self.print_income(self.down_frame)
        self.addNewExpenseButton = Button(self.down_frame, text="Add new expense", font=self.font, bg='#938DF6')
        self.addNewExpenseButton.place(x=425, y=570, anchor='center')
        self.addNewExpenseButton.bind("<Button-1>", self.addNewExpense)
        self.addNewIncomeButton = Button(self.down_frame, text="Add new income", font=self.font, bg='#938DF6')
        self.addNewIncomeButton.place(x=925, y=570, anchor='center')
        self.addNewIncomeButton.bind("<Button-1>", self.addNewIncome)
      
    def display(self):     # utkarsh
        income_amount = self.print_total_income()
        expenses_amount = self.print_total_expenes()
        income_string = "Income " + str(income_amount)
        expenses_string = "Expenses " + str(expenses_amount)
        balance_string = "Balance " + str(income_amount - expenses_amount)
        self.income = Label(self.up_frame, height=2, width=35, text=income_string, font=44).place(x=75, y=15)
        self.expense = Label(self.up_frame, height=2, width=35, text=expenses_string, font=44).place(x=525, y=15)
        self.balance = Label(self.up_frame, height=2, width=35, text=balance_string, font=44)
        self.balance.place(x=975, y=15)

    def message(self, message):
        new_window = Toplevel(self.root)
        Message.Message(new_window, self.color, message)
        new_window.wait_window()

    def addNewExpense(self, event):
        new_window = Toplevel(self.root)
        NewExpense(new_window, self.color, self.dbconnection, self.current_login)
        new_window.wait_window()
        self.print_expenses(self.down_frame)
        self.display()     # utkarsh

    def addNewIncome(self, event):
        new_window = Toplevel(self.root)
        NewIncome(new_window, self.color, self.dbconnection, self.current_login)
        new_window.wait_window()
        self.print_income(self.down_frame)
        self.display()     # utkarsh

    def print_total_income(self):
        mycursor = self.dbconnection.cursor()
        member_variable = (self.current_login,)
        query = "select sum(amount) from income where member_id = %s"
        mycursor.execute(query, member_variable)
        total = mycursor.fetchone()
        return total[0] or 0

    def print_total_expenes(self):
        mycursor = self.dbconnection.cursor()
        member_variable = (self.current_login,)
        query = "select sum(amount) from expense where member_id = %s"
        mycursor.execute(query, member_variable)
        total = mycursor.fetchone()
        return total[0] or 0

    def name(self):     # utkarsh
    	cursor=self.dbconnection.cursor()
    	member_variable = (self.current_login,)
    	query="select first_name from family where member_id=%s"
    	cursor.execute(query,member_variable)
    	name = cursor.fetchone()
    	return name[0]

    def print_expenses(self, frame):
        mycursor = self.dbconnection.cursor()
        mycursor.execute("select e.expense_id,f.first_name,  ec.name, e.expense_date, e.amount, e.comments from "
                         "expense e inner join family f on e.member_id = f.member_id inner join e_category ec on "
                         "e.expense_category_id = ec.expense_category_id")
        expenses_list = mycursor.fetchall()
        label = Label(frame, font=("Arial", 15), text="Expenses ").place(x=630, y=10)
        cols = ("Number", "Member", "Expense - Category", "Date", "Amount", "Comments")
        list_box = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box.heading(col, text=col)
        list_box.place(x=55, y=40)
        verscrlbar = ttk.Scrollbar(frame,
                                   orient="vertical",
                                   command=list_box.yview)
        verscrlbar.place(x=1400, y=50)
        list_box.configure(xscrollcommand=verscrlbar.set)
        name=self.name()     # utkarsh
        for i, (id1, id2, cat, date, am, comm) in reversed(list(enumerate(expenses_list, start=1))):
            if name==id2:    # utkarsh
                list_box.insert("", "end", values=(id1, id2, cat, date, am, comm))

    def print_income(self, frame):

        mycursor = self.dbconnection.cursor()
        mycursor.execute("select i.income_id,f.first_name,  ic.name, i.income_date, i.amount, i.comments from income "
                         "i inner join family f on i.member_id = f.member_id inner join i_category ic on "
                         "i.income_category_id = ic.income_category_id")
        income_list = mycursor.fetchall()
        label = Label(frame, font=("Arial", 15), text="Income  ").place(x=630, y=270)
        cols = ("Number", "Member", "Income - Category", "Date", "Amount", "Comments")
        list_box2 = ttk.Treeview(frame, columns=cols, show='headings')
        for col in cols:
            list_box2.heading(col, text=col)
        list_box2.place(x=55, y=300)
        verscrlbar = ttk.Scrollbar(frame,
                                   orient="vertical",
                                   command=list_box2.yview)
        verscrlbar.place(x=1400, y=300)
        list_box2.configure(xscrollcommand=verscrlbar.set)

        name=self.name()     # utkarsh
        for i, (id1, id2, cat, date, am, comm) in reversed(list(enumerate(income_list, start=1))):
            if name==id2:    # utkarsh
            	list_box2.insert("", "end", values=(id1, id2, cat, date, am, comm))

    def profile(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Profile")
        profile_screen.geometry("750x500")
        view(profile_screen,self.dbconnection,self.current_login)

    def update(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Update")
        profile_screen.geometry("750x500")
        u=updates(profile_screen,self.dbconnection,self.current_login)

    def delete(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Delete Account")
        profile_screen.geometry("750x1000")
        d=delete(profile_screen,self.dbconnection,self.current_login)
        profile_screen.wait_window()
        self.root.destroy()

    def deleteI(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Delete Income")
        profile_screen.geometry("750x1000")
        d=deleteI(profile_screen,self.dbconnection,self.current_login)
        profile_screen.wait_window()
        self.print_income(self.down_frame)
        self.display()

    def deleteE(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Delete Expense")
        profile_screen.geometry("750x1000")
        d=deleteE(profile_screen,self.dbconnection,self.current_login)
        profile_screen.wait_window()
        self.print_expenses(self.down_frame)
        self.display()

    def deleteAI(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Delete All Income")
        profile_screen.geometry("750x1000")
        d=deleteAI(profile_screen,self.dbconnection,self.current_login)
        profile_screen.wait_window()
        self.print_income(self.down_frame)
        self.display()

    def deleteAE(self):     # utkarsh
        profile_screen=Toplevel(self.root)
        profile_screen.title("Delete All Expense")
        profile_screen.geometry("750x1000")
        d=deleteAE(profile_screen,self.dbconnection,self.current_login)
        profile_screen.wait_window()
        self.print_expenses(self.down_frame)
        self.display()
     