# Expense-Manager-
A desktop application using MySQL and Python Tkinter GUI

# family.sql
This file creates database for the progam and cretares the tables requiired .

# Welcome.py
##class WelcomePage()
   
###Methods defined here:
__init__(self)
this constructor is called when a instance is created for WelcomePage class.
Here we connect the program to the database and create the root window and set
height, width, color of the window and call gui_init function.

gui_init(self)
This function creates frames in the root window viz. up_frame and down_frame
In the up_frame we display the title of the application in the down_frame we show 
the login and sign-up options.This is done by creating a instance of class
MainPage by passing 7 parameters of which down_frame is also passsed.

# index.py
##class MainPage()
MainPage(parent, root, height, width, side, color, dbconnection)
 
###Methods defined here:
__init__(self, parent, root, height, width, side, color, dbconnection)
this constructor is called when a instance is created for MainPage class.
It takes 7 parameters.In addition we also set the
font.Then we call gui_init function of class MainPage.

gui_init(self)
Here we create a frame inside a frame and create two buttons
viz. login and sign-up. When we click on Sign-up button register function is called
and when we click on login we create a new instance of class LoginFrame and pass it 
same 7 parameters as earlier

insert_family(self, member_id, first_name, last_name, username, password)
This function takes 5 parameters and enters the users information in the database with others.

insert_income(self, member_id)
This function takes 1 parameter and creates a blank dashboard for the user so that he can 
start trcking his expenses once he logins.

register(self)
This function is called when Sign-Up button is clicked.This creates a new window
and ask for required details to sign up. On entering the details we click on register
button and register_user function is called.

register_user(self)
This function is called on clicking the register button.This function checks the users
details with others details and display appropriate message on the screen.If the user is
successfully registered then 2 functions insert_income and insert_family are called to
create a blank dashboard for the user and insert the credentials to the database respectively

# Message.py
##class Message()
Message(root, color, message)
 
###Methods defined here:
__init__(self, root, color, message)
This is the most commonly used class in the entire program that displays.
This constructor is called when a instance is created for Message class.
It takes 3 parameters. 
the messages to the user.It calls gui_init function of class Message.

gui_init(self)
This simply creates a window with label to display message and a button which destroys the
current window.

# LoginPage.py
##class LoginFrame()
LoginFrame(parent, root, height, width, side, color, dbconnection)
 
###Methods defined here:
__init__(self, parent, root, height, width, side, color, dbconnection)
this constructor is called when a instance is created for LoginFrame class.
It takes 7 parameters.In addition we also set the
font.Then we call gui_init function of class LoginFrame.

gui_init(self)
Here we create a frame inside a frame and create 2 labels and a buttonto enter our credentials.When we press the button it calls __loginAction function.


# AdminPage.py
##class AdminPage()
AdminPage(root, color, font, dbconnection, width, current_login)
 
###Methods defined here:
__init__(self, root, color, font, dbconnection, width, current_login)
this constructor is called when a instance is created for AdminPage class.
It takes 6 parameters with the exception of screen
height so dashboard is created in full screen.In addition we also set the
font.We also create a menu bar with various functions .
Then we call gui_init function of class Admin_Page.

addNewExpense(self, event)
This function is called when user clicks on Add New Expense button
It creates a instance to the class NewExpense in a new window
and then again displays the updated expense list.

addNewIncome(self, event)
This function is called when user clicks on Add New Income button
It creates a instance to the class NewIncome in a new window
and then again displays the updated income list.

delete(self)
This function is called when user clicks on delete account button from menubar.It opens a 
new window and creates a instance to class delete.

deleteAE(self)
This function is called when user clicks on delete all expense button from menubar.It opens a 
new window and creates a instance to class deleteAE and then again display the updated expense
transaction list on dashboard as well as updated expense on up_frame.

deleteAI(self)
This function is called when user clicks on delete all income button from menubar.It opens a 
new window and creates a instance to class deleteAI and then again display the updated income
transaction list on dashboard as well as updated income on up_frame.

deleteE(self)
This function is called when user clicks on delete expense button from menubar.It opens a 
new window and creates a instance to class deleteE and then again display the updated expense
transaction list on dashboard as well as updated expense on up_frame.

deleteI(self)
This function is called when user clicks on delete income button from menubar.It opens a 
new window and creates a instance to class deleteI and then again display the updated income
transaction list on dashboard as well as updated income on up_frame.

display(self)
This function displays the income, expense and balance on the up_frame and calls 2 function
viz. print_total_income and print_total_expenes to get the current income and expense.

gui_init(self)
This function creates 2 frames viz. up_frame and down_frame
in up_frme we display income, expense and balance by calling display function
in down_frame we create the list of transactions by calling print_expenses and print_income function
It also  has buttons which calls respective function on clicking.

message(self, message)
this is the common function for all modules that is used to display any message

name(self)
This function is called by print_expenses and print_income function to get the first name 
of the user.

print_expenses(self, frame)
This function is called when a new expense is created so that all the 
expense transaction of user can be displayed.

print_income(self, frame)
This function is called when a new income or a new acount is created so that all the 
income transaction of user can be displayed.

print_total_expenes(self)
This function is called by display function and it returns the total expense of a user.

print_total_income(self)
This function is called by display function and it returns the total income of a user.

profile(self)
This function is called when user clicks on profile button from menubar.It opens a 
new window and calls view function from profile module.

update(self)
This function is called when user clicks on update button from menubar.It opens a 
new window and creates a instance to class updates.

# NewExpense.py
##class NewExpense()
NewExpense(root, color, dbconnection, current_login)

###Methods defined here:
__init__(self, root, color, dbconnection, current_login)
this constructor is called when a instance is created for NewExpense class.
It takes 4 parameters.In addition we set screen
height and screen width.Then we call gui_init function of class NewExpense.
This class is used to add new expense.

addexpense(self, event)
This method is called on clicking submit button and it inserts the new expense into database.
Then it prints the appropriate message by calling message function.

gui_init(self)
This creates a new root window a frame with 3 labels and a submit button which on clicking 
calls addexpense function.

# NewIncome.py
##class NewIncome()
NewIncome(root, color, dbconnection, current_login)
 
###Methods defined here:
__init__(self, root, color, dbconnection, current_login)
this constructor is called when a instance is created for NewIncome class.
It takes 4 parameters.In addition we set screen
height and screen width.Then we call gui_init function of class NewIncome.
This class is used to add new income.

addincome(self, event)
This method is called on clicking submit button and it inserts the new income into database.
Then it prints the appropriate message by calling message function.

gui_init(self)
This creates a new root window a frame with 3 labels and a submit button which on clicking 
calls addincome function.

# profile.py
###Methods defined here:
getFirst_name(dbconnection, current_login)
This function gets the first name of user.

getLast_name(dbconnection, current_login)
This function gets the last name of user.

getUsername(dbconnection, current_login)
This function gets the username of user.

view(profile_screen, dbconnection, current_login)
this function is called when we click on profile in menu bar.
It is used to view the users profile.

# update.py
##class updates()
updates(root, dbconnection, current_login)
 
###Methods defined here:
__init__(self, root, dbconnection, current_login)
this constructor is called when a instance is created for updates class.
It takes 4 parameters.In addition we set color
of the screen.Then we call update function.
This class is used to update the profile.

changeFname(self)
This function updates the first name of user in database and displays 
appropriate message.

changeLname(self)
This function updates the last name of user in database and displays 
appropriate message.

changePass(self)
This function updates the password of user in database and displays 
appropriate message.

changeUname(self)
This function updates the username of user in database and displays 
appropriate message.

update(self)
This function has 4 labels and 4 button which performs task assigned to them when clicked.

# deleteIncome.py
##class deleteI()
deleteI(root, dbconnection, current_login) 
 
###Methods defined here:
__init__(self, root, dbconnection, current_login)
this constructor is called when a instance is created for deleteI class.
It takes 4 parameters.In addition we set color of the screen.
Then we call enterIno function.
This class is used to delete a particular income.

enterIno(self)
When this function is called It asks for user to enter income id to delete.
If users enter Y and clicks the button then removeE function is called else
appropriate message is displayed.

removeE(self)
This function removes the particular income from the records and displays appropriate
message .

# deleteExpense.py
##class deleteE()   
deleteE(root, dbconnection, current_login)

###Methods defined here:
__init__(self, root, dbconnection, current_login)
this constructor is called when a instance is created for deleteE class.
It takes 4 parameters.In addition we set color of the screen.
Then we call enterEno function.
This class is used to delete a particular expense.

enterEno(self)
When this function is called It asks for user to enter expense no to delete.
If users enter Y and clicks the button then removeE function is called else
appropriate message is displayed.

removeE(self)
This function removes the particular expense from the records and displays appropriate
message .

# delAllincome.py
##class deleteAI()   
deleteAI(root, dbconnection, current_login)
 
###Methods defined here:
__init__(self, root, dbconnection, current_login)
this constructor is called when a instance is created for deleteAI class.
It takes 4 parameters.In addition we set color of the screen.
Then we call confirm function.
This class is used to delete entire income transaction of user.

confirm(self)
When this function is called It asks for user to confirm deletion.
If users enter Y and clicks the button then removeAllincome function is called else
appropriate message is displayed.

removeAllincome(self)
This function removes the entire income list of user from the records and displays appropriate message .

# delAllexpense.py
##class deleteAE()
deleteAE(root, dbconnection, current_login)
 
###Methods defined here:
__init__(self, root, dbconnection, current_login)
this constructor is called when a instance is created for deleteAE class.
It takes 4 parameters.In addition we set color of the screen.
Then we call confirm function.
This class is used to delete entire expense transaction of user.

confirm(self)
When this function is called It asks for user to confirm deletion.
If users enter Y and clicks the button then removeAllexpense function is called else
appropriate message is displayed.

removeAllexpense(self)
This function removes the entire expense list of user from the records and displays appropriate message .

# deleteAccount.py
##class delete()
delete(root, dbconnection, current_login)
 
###Methods defined here:
__init__(self, root, dbconnection, current_login)
this constructor is called when a instance is created for delete class.
It takes 4 parameters.In addition we set color of the screen.
Then we call confirm function.
This class is used to delete user account.

confirm(self)
When this function is called It asks for user to confirm account deletion.
If users enter Y and clicks the button then removeAccount function is called else
appropriate message is displayed.

removeAccount(self)
This function removes the account from the records and displays appropriate
message .It also calls functions to remove income and expenses from the records.

removeExpense(self)
This function removes the users entire expense from the records and displays appropriate
message .

removeIncome(self)
This function removes the users entire income from the records and displays appropriate
message .