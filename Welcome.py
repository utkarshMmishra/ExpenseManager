from mysql.connector import MySQLConnection


from index import *
# Database
USER = 'root'
PASSWORD = 'UtSQL@1to9'
HOST = 'localhost'
DATABASE = 'mydatabase'


class WelcomePage:
    def __init__(self):
        self.root = root
        self.color = '#E2FFE6'
        self.screen_width = root.winfo_screenwidth() / 2
        self.screen_height = root.winfo_screenheight() / 2
        self.dbConnection = MySQLConnection(user=USER, password=PASSWORD, host=HOST, database=DATABASE)
        self.up_frame = None
        self.down_frame = None
        self.welcomeText = None
        self.login_frame = None
        self.gui_init()

    def gui_init(self):
        self.up_frame = Frame(
            self.root,
            cursor='arrow',
            bg='#3368FF',
        )
        self.up_frame.pack(side=TOP, expand=True, fill=BOTH)
        self.down_frame = Frame(
            self.root,
            cursor='arrow',
            bg=self.color,
        )
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.welcomeText = Label(
            self.up_frame,
            text="Expense Manager",
            font=('Verdana', 40, 'bold'),
            bg=self.color)
        self.welcomeText.place(relx=.5, rely=.5, anchor='center')
# utkarsh
        self.login_frame = MainPage(self.root, self.down_frame,   
                                      self.screen_height * 3 / 4,
                                      self.screen_width / 2, LEFT,
                                      self.color,
                                      self.dbConnection,
                                      )


root = Tk()
root.title("Expense Manager")
root.geometry("1920x1080")
root.resizable(width=True, height=True)

logupFrame = WelcomePage()
root.mainloop()
