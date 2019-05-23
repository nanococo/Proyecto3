import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default='icono.ico')

        container = tk.Frame(self)
        container.pack(side='top', fill='both',  expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # menuBar = tk.Menu(container)
        # fileMenu = tk.Menu(menuBar, tearoff=0)
        # fileMenu.add_command(label='LogOut', command= lambda: 'Sale al menu principal')
        # fileMenu.add_separator()
        # fileMenu.add_command(label='End program', command=quit)
        # menuBar.add_cascade(label='Exit', menu=fileMenu)
        # tk.Tk.config(self, menu=menuBar)


        self.frames = {}

        for F in (AdminMainMenu, PageOne, PageTwo, logIn):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(logIn)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()



class AdminMainMenu(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
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



class logIn(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.userName=ttk.Entry(self)
        self.userName.place(x=230,y=50)
        self.userNameLabel=ttk.Label(self,text="User Name")
        self.userNameLabel.place(x=120, y =50)

        self.passwordLabel = ttk.Label(self, text="Password")
        self.passwordLabel.place(x=120, y=100)
        self.password= ttk.Entry(self, show='*')
        self.password.place(x=230,y=100)


        self.logIn=ttk.Button(self,text="Log In",command=lambda :self.getLoginInfo(controller))
        self.logIn.place(x=200,y=200)
        controller.show_frame(AdminMainMenu)

    def getLoginInfo(self,controller):
        userName=self.userName.get()
        password=self.password.get()

        # Change this for the actual user list
        logInList=[['1','a','0'],['2','b','1'],['3','c','0'], ['JorgeG','2019077521','1']]


        login_success=False
        migration_status=False
        #Eddit to fit logInList indexes

        for user in logInList:
            if userName == user[0]:
                if password==user[1]:
                    login_success=True
        if not login_success:
            messagebox.showinfo("Access denied", "Wrong User Name or password")
        elif login_success and not migration_status:
            for child in self.winfo_children():
                child.place_forget()
            self.draw_mainMenu(controller)

    def draw_mainMenu(self,controller):
        # messagebox.showinfo("Conection ")
        controller.show_frame(AdminMainMenu)


        # self.userName.delete(0, tk.END)
        # self.password.delete(0, tk.END)

app = mainApp()
app.title('Admin')
app.geometry('500x600')
app.resizable(0,0)
app.mainloop()
