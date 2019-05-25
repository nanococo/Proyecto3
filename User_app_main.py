import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import socket, os, pickle

class map(ttk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.counter = 0
        self.img = Image.open("newDataFiles/Assets/europe_map(3).png")
        self.display =ImageTk.PhotoImage(self.img)
        self.map= tk.Label(self,image=self.display, bd=5, relief="ridge")
        self.map.pack()


        self.pin= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin = ImageTk.PhotoImage(self.pin)
        self.pinButton=ttk.Button(self, command=self.create_window)
        self.pinButton.config(image=self.displayPin)
        self.pinButton.place(x=90,y=330)

    def create_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="This is window #%s" % self.counter)
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)



class logIn(ttk.Frame):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)


        self.userID= ttk.Entry(self,show="*")
        self.userID.place(x=230,y=80)
        self.userIDLabel = ttk.Label(self,text="User ID")
        self.userIDLabel.place(x=120, y=80)

        self.logIn=ttk.Button(self,text="Log In",command=self.getLoginInfo)
        self.logIn.place(x=200,y=200)
    def getLoginInfo(self):
        userId=self.userID.get()

        codeList = ["00", userId]
        s.send(pickle.dumps(codeList))
        userValidated = pickle.loads(s.recv(8192))

        if userValidated:

            codeList = ["01", userId]
            s.send(pickle.dumps(codeList))
            userStatus = pickle.loads(s.recv(8192))

            if userStatus == "0":
                # AQUI DEJA CARGAR NUEVA VENTANA
                # Set userName here:
                codeList = ["02", userId]
                s.send(pickle.dumps(codeList))
                userName = pickle.loads(s.recv(8192))
                for child in self.winfo_children():
                    child.place_forget()
                self.chooseRecervation()
                print("Success")

                # Set logged flag (ESTO DEBE SER UNA VARIABLE GLOBAL)
                logged = True

            else:

                messagebox.showinfo("Access denied","User with migration issues")

                loginError = False
                blocked = True
        else:

            messagebox.showinfo("Access denied", "Wrong User Name or password")

            loginError = True


        self.userID.delete(0, tk.END)

    def chooseRecervation(self):

        self.fixedRouteRecervation=ttk.Button(self, text="Fixed route recervation", command=self.drawFixedRecervation)
        self.fixedRouteRecervation.place(x=170,y=100)

        self.customRecervation = ttk.Button(self, text="Custom route recervation", command=self.drawCustomRecervation)
        self.customRecervation.place(x=161,y=250)

    def drawFixedRecervation(self):
        for child in self.winfo_children():
            child.place_forget()

        self.searchKey=[]

        self.departureCountryList = ttk.Combobox(self, state="readonly", width= 40)
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.departureCountryList["values"] = pickle.loads(s.recv(8192))
        self.departureCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionFixed)
        self.departureCountryList.place(x=180, y=50)
        self.departureCountryListLabel=ttk.Label(self, text="Countries")
        self.departureCountryListLabel.place(x=100, y=50)

        self.departureCityList = ttk.Combobox(self, state="readonly")
        self.departureCityList.bind("<<ComboboxSelected>>", self.selectCityFixed)
        self.departureCityList.place(x=250, y=100)
        self.departureCityListLabel=ttk.Label(self, text="Cities")
        self.departureCityListLabel.place(x=100, y = 100)


        """
                ADD BILLING BUTTON
        """

        self.backButton=ttk.Button(self, text="Back", command= self.backToLogIn)
        self.backButton.place(x=40,y=200)

    def drawCustomRecervation(self):
        for child in self.winfo_children():
            child.place_forget()

        self.searchKey=[]

        self.departureCountryList = ttk.Combobox(self, state="readonly", width= 40)
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.departureCountryList["values"] = pickle.loads(s.recv(8192))
        self.departureCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionCustom1)
        self.departureCountryList.place(x=180, y=50)
        self.departureCountryListLabel=ttk.Label(self, text="Departure Country")
        self.departureCountryListLabel.place(x=100, y=50)

        self.departureCityList = ttk.Combobox(self, state="readonly")
        self.departureCityList.bind("<<ComboboxSelected>>", self.selectCityCustom1)
        self.departureCityList.place(x=250, y=100)
        self.departureCityListLabel=ttk.Label(self, text="Departure City")
        self.departureCityListLabel.place(x=100, y = 100)

        self.ArrivalCountryList = ttk.Combobox(self, state="readonly", width=40)
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.ArrivalCountryList["values"] = pickle.loads(s.recv(8192))

        self.ArrivalCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionCustom2)
        self.ArrivalCountryList.place(x=180, y=200)
        self.ArrivalCountryListLabel = ttk.Label(self, text="Arrival Country")
        self.ArrivalCountryListLabel.place(x=100, y=200)

        self.ArrivalCityList = ttk.Combobox(self, state="readonly")
        self.ArrivalCityList.bind("<<ComboboxSelected>>", self.selectCityCustom2)
        self.ArrivalCityList.place(x=250, y=250)
        self.ArrivalCityListLabel = ttk.Label(self, text="Arrival City")
        self.ArrivalCityListLabel.place(x=100, y=250)




    def updateCitiesOnSelectionFixed(self, event):


        self.searchKey=[self.departureCountryList.get().split(" ")[0]]


        print(self.searchKey[0])
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        self.departureCityList["values"] = pickle.loads(s.recv(8192))
        print(self.searchKey)
    def selectCityFixed(self, event):

        if len(self.searchKey)==1:
             self.searchKey+=[self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1]=self.departureCityList.get().split(" ")[0]
        print(self.searchKey)
    def updateCitiesOnSelectionCustom1(self, event):


        self.searchKey=[self.departureCountryList.get().split(" ")[0]]

        print(self.searchKey[0])
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        self.departureCityList["values"] = pickle.loads(s.recv(8192))
        print(self.searchKey)
    def selectCityCustom1(self, event):

        if len(self.searchKey)==1:
             self.searchKey+=[self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1]=self.departureCityList.get().split(" ")[0]
        print(self.searchKey)

#####################
    def updateCitiesOnSelectionCustom2(self, event):

        if len(self.searchKey)==2:
            self.searchKey+=[self.departureCountryList.get().split(" ")[0]]
        else:
            self.searchKey[2]= self.departureCountryList.get().split(" ")[0]

        print(self.searchKey[0])
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        self.departureCityList["values"] = pickle.loads(s.recv(8192))
        print(self.searchKey)
    def selectCityCustom2(self, event):

        if len(self.searchKey)==1:
             self.searchKey+=[self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1]=self.departureCityList.get().split(" ")[0]
        print(self.searchKey)
#####################

    def backToLogIn(self):
        for child in self.winfo_children():
            child.place_forget()
        self.chooseRecervation()

    def predefinedRouteList(self):
        if self.searchKey==[]:
            messagebox.showinfo("","Please select a contry and a city")
        elif len(self.searchKey)==2:
            for child in self.winfo_children():
                child.place_forget()
            """ routes es la lista que se va a cargar para que el usuario seleccione la ruta que desea"""
            routes=[]
            if self.searchKey==['1','a']:
                routes=[1,2,3,4,5,6]
            elif self.searchKey==['2','c']:
                routes=['a','b','c','d']

            self.routesListBox = tk.Listbox(self,width=69,height=20, selectmode=tk.SINGLE)
            self.routesListBox.bind("<<ListboxSelect>>", self.getListBox )
            self.routesListBox.place(x=19,y=20)
            for i in routes:
                self.routesListBox.insert(tk.END,i)

            self.backButton=ttk.Button(self, text="Back", command=self.backToRecervation)
            self.backButton.place(x=90,y=380)

            self.billingButton=ttk.Button(self, text="Continue", command = self.continueToBilling)
            self.billingButton.place(x=290, y=380)

            self.vcmd = (self.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            self.amountOfSeats = ttk.Entry (self, validate = 'key',validatecommand=self.vcmd)
            self.amountOfSeats.place(x=165, y=350)

    def customRouteList(self):
        if self.searchKey == []:
            messagebox.showinfo("", "Please select a contry and a city")
        elif len(self.searchKey) == 2:
            for child in self.winfo_children():
                child.place_forget()
            """ routes es la lista que se va a cargar para que el usuario seleccione la ruta que desea"""
            routes = []
            if self.searchKey == ['1', 'a']:
                routes = [1, 2, 3, 4, 5, 6]
            elif self.searchKey == ['2', 'c']:
                routes = ['a', 'b', 'c', 'd']

            self.routesListBox = tk.Listbox(self, width=69, height=20, selectmode=tk.SINGLE)
            self.routesListBox.bind("<<ListboxSelect>>", self.getListBox)
            self.routesListBox.place(x=19, y=20)
            for i in routes:
                self.routesListBox.insert(tk.END, i)

            self.backButton = ttk.Button(self, text="Back", command=self.backToRecervation)
            self.backButton.place(x=90, y=380)

            self.billingButton = ttk.Button(self, text="Continue", command = self.continueToBilling)
            self.billingButton.place(x=290, y=380)

            self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            self.amountOfSeats = ttk.Entry(self, validate='key', validatecommand=self.vcmd)
            self.amountOfSeats.place(x=165, y=350)

    def getListBox(self, event):
        if len(self.searchKey)==2:
            self.searchKey+=[self.routesListBox.get(self.routesListBox.curselection())]
        else:
            self.searchKey[2]=self.routesListBox.get(self.routesListBox.curselection())
        print(self.searchKey)

    def continueToBilling(self):
        seatsToBuyself=self.amountOfSeats.get()
        #Metale un elif para que segun la ruta seleccionada el mae no pueda avanzar si metio un numero mas alto que el total de asientos de la ruta
        if len(self.searchKey)==2:
            messagebox.showinfo("","Please select a route")
        else:
            print(seatsToBuyself)
        # else:
        #     for child in self.winfo_children():
        #         child.place_forget()

    def backToRecervation(self):
        for child in self.winfo_children():
            child.place_forget()
        self.draw_recervation()

    def validate(self, action, index, value_if_allowed,prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                if value_if_allowed=="":
                    return True
                else:
                    return False

        else:
            return False

class MainApp(ttk.Frame):
    def __init__(self,main_window):
        super().__init__(main_window)
        main_window.title("User")


        #Creacion del notebook
        self.notebook = ttk.Notebook(self,height=600,width=500)

        #Se agregan las paginas
        self.map=map(self.notebook)
        self.notebook.add(self.map,text="Map", padding=10)

        self.reservation_page=logIn(self.notebook)
        self.notebook.add(self.reservation_page,text="Reservations",padding=10)

        self.notebook.pack(padx=10, pady=10)

        self.pack()

if __name__ == '__main__':
    """
        MAIN APPLICATION METHOD. INVOKES METHODS ON ADMIN AND USER MODULES

    """
    host = '127.0.0.1'
    # Define the port on which you want to connect
    port = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server on local computer
    s.connect((host, port))



    main_window=tk.Tk()
    main_window.geometry("500x600")
    main_window.iconbitmap(default="icono.ico")
    main_window.resizable(0,0)
    app = MainApp(main_window)

    app.mainloop()