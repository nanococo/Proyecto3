import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class startScreen(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self, default='C:/Users\jguty\OneDrive\Pictures/icono.ico')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = logIn(container, self)

        self.frames[logIn] = frame

        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(logIn)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class logIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.userNameLabel = ttk.Label(self, text="User Name")
        self.userNameLabel.pack()
        self.userName = ttk.Entry(self)
        self.userName.pack()


        self.passwordLabel = ttk.Label(self, text="Password")
        self.passwordLabel.pack()
        self.password = ttk.Entry(self, show='*')
        self.password.pack()


        self.logIn = ttk.Button(self, text="Log In", command=self.getLoginInfo)
        self.logIn.place(x=63,y=95)

    def getLoginInfo(self):
        userName = self.userName.get()
        password = self.password.get()

        # Change this for the actual user list
        logInList = [['1', 'a', '0'], ['2', 'b', '1'], ['3', 'c', '0'], ['JorgeG', '2019077521', '1']]

        login_success = False
        # Eddit to fit logInList indexes and migration status

        for user in logInList:
            if userName == user[0]:
                if password == user[1]:
                    login_success = True
        if not login_success:
            messagebox.showinfo("Access denied", "Wrong User Name or password")
        elif login_success:
            self.destroy()
            app = mainApp()
            app.title('Admin')
            app.geometry('500x600')
            app.resizable(0, 0)
            app.mainloop()


class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default='C:/Users\jguty\OneDrive\Pictures/icono.ico')

        container = tk.Frame(self)
        container.pack(side='top', fill='both',  expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menuBar = tk.Menu(container)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='LogOut', command= lambda: 'Sale al menu principal')
        fileMenu.add_separator()
        fileMenu.add_command(label='End program', command=quit)
        menuBar.add_cascade(label='Exit', menu=fileMenu)
        tk.Tk.config(self, menu=menuBar)


        self.frames = {}

        for F in (AdminMainMenu, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(AdminMainMenu)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class AdminMainMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Main menu. Logged user:')
        label.config(font=('Calibri', 13))
        label.place(x=0, y=0)


        #Notebook
        self.notebook = ttk.Notebook(self,height=550,width=500)
        self.consult = PageOne(self.notebook, controller)
        self.notebook.add(self.consult, text="Consult", padding=10)
        self.data = PageTwo(self.notebook, controller)
        self.notebook.add(self.data, text="Data", padding=10)
        self.notebook.pack(side='bottom')
        self.pack()
        #

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Please select an option:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        # button1 = ttk.Button(self, text='Visit page 1',
        #                      command=lambda: controller.show_frame(PageOne))
        # button1.place(x=5, y=40)

        # self.ListBoxExample=tk.Listbox(self,selectmode=tk.SINGLE)
        # listExample=['1','2','3','4']
        # for i in listExample:
        #     self.ListBoxExample.insert(tk.END,i)
        # self.ListBoxExample.place(x=0,y=200)

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Please select an option:')
        label.config(font=('Calibri', 11))
        label.place(x=0,y=0)

        # button1 = ttk.Button(self, text='Visit page 1',
        #                      command=lambda: controller.show_frame(PageOne))
        # button1.place(x=5, y=40)



startScreen= startScreen()
startScreen.title('SS')
startScreen.geometry("200x150")
startScreen.resizable(0, 0)
startScreen.mainloop()
