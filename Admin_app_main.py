import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk
from tkinter import Tk, Canvas
import socket, os, pickle
import time

adminID = ""

class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default='icono.ico')
        self.bind("<Destroy>", self.handle_close)

        container = tk.Frame(self)
        container.pack(side='top', fill='both',  expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menuBar = tk.Menu(container)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='LogOut', command= lambda: self.server_Logout(logIn))
        fileMenu.add_separator()
        fileMenu.add_command(label='End program', command=quit)
        menuBar.add_cascade(label='Exit', menu=fileMenu)
        tk.Tk.config(self, menu=menuBar)


        self.frames = {}

        for F in (AdminMainMenu, Consult, DataBase, Insert,Delete, Modify, logIn):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(AdminMainMenu)

    def handle_close(self, event):
        global adminID
        if event.widget == self:
            print("Closing")
            # METHOD TO UNLOCK SERVER
            codeList = ["46", adminID]
            s.send(pickle.dumps(codeList))

    def server_Logout(self, cont):
        # METHOD TO UNLOCK SERVER
        codeList = ["46", adminID]
        s.send(pickle.dumps(codeList))
        self.show_frame(cont)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




class AdminMainMenu(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Main menu')
        label.config(font=('Calibri', 13))
        label.place(x=0, y=0)

        #Notebook
        self.notebook = ttk.Notebook(self,height=550,width=500)
        self.consult = Consult(self.notebook, controller)
        self.notebook.add(self.consult, text="Consult", padding=10)
        self.dataBaseChanges = DataBase(self.notebook, controller)
        self.notebook.add(self.dataBaseChanges, text="Data Base Management", padding=10)
        self.notebook.pack(side='bottom')
        self.history = History(self.notebook, controller)
        self.notebook.add(self.history, text="History", padding=10)
        self.pack()
        #


class Consult(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.init_consults()

    #Check prices
    def draw_checkPrices(self):
        global adminID
        self.clear()

        codeList = ["43", adminID]
        s.send(pickle.dumps(codeList))
        trains = pickle.loads(s.recv(8192))
        trains = self.sliceTrains(trains)

        self.trainCodeLabel = ttk.Label(self, text="Please select a train code to find assosiated route prices")
        self.trainCodeLabel.place(x=78, y=20)

        self.trainCode = ttk.Combobox(self, state="readonly")
        self.trainCode["values"] = trains
        self.trainCode.bind("<<ComboboxSelected>>")
        self.trainCode.place(x=153, y=50)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=150, y=120)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithPrices())
        Continue.place(x=188, y=80)

        self.pricesListbox = tk.Listbox(self, width=75)
        self.pricesListbox.place(x=10, y=150)

        self.buttonBack()
    def fillWithPrices(self):
        global adminID
        self.pricesListbox.delete(0, tk.END)

        code = self.trainCode.get().split(' ')[0]

        if code == '':
            messagebox.showerror('ERROR', 'Please type a train code')
        else:

            codeList = ["07", adminID, code]
            s.send(pickle.dumps(codeList))
            prices = pickle.loads(s.recv(8192))

            if not prices:

                self.label.configure(
                    text='There are no route prices associated with ' + self.trainCode.get().split(' ')[1])
                self.label.config(font=('Calibri', 10))
                self.label.place(x=93, y=120)

            else:

                self.label.configure(text='The route prices are:')
                self.label.config(font=('Calibri', 10))
                self.label.place(x=167, y=120)

                index = 0
                for route in prices:
                    self.pricesListbox.insert(index, route)
    def sliceTrains(self, list):
        newList = []
        for i in list:
            newList += [i[1] + ' ' + i[2]]
        return newList

    #

    #Check countries
    def draw_checkCountries(self):
        global adminID
        self.clear()

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        label = tk.Label(self, text='These are the registered countries:')
        label.config(font=('Calibri', 11))
        label.place(x=115, y=20)

        self.countryListbox = tk.Listbox(self, width=30, height=20)

        index = 0
        for country in countries:
            self.countryListbox.insert(index, country[0]+' '+country[1])
        self.countryListbox.place(x=138, y=50)

        self.buttonBack()
    #

    #Check cities
    def draw_checkCities(self):
        global adminID
        self.clear()

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.selection = StringVar()

        self.availableCountries = ttk.Combobox(self, state="readonly", textvariable=self.selection)
        self.availableCountries["values"] = countries

        self.availableCountries.bind("<<ComboboxSelected>>")
        self.availableCountries.place(x=153, y=50)
        self.availableCountriesLabel = ttk.Label(self, text="Please choose a country to find associated cities:")
        self.availableCountriesLabel.place(x=93, y=20)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=153, y=120)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithCities())
        Continue.place(x=188, y=80)

        self.cityListbox = tk.Listbox(self)
        self.cityListbox.place(x=163, y=150)

        self.buttonBack()
    def fillWithCities(self):
        global adminID
        self.cityListbox.delete(0, tk.END)

        self.searchKey = self.availableCountries.get().split(' ')[0]
        codeList = ["04", adminID, self.searchKey]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))

        if not cities:
            self.label.configure(text=self.selection.get()+' does not have any registered cities')
            self.label.config(font=('Calibri',10))
            self.label.place(x=102,y=120)

        index = 0
        for city in cities:
            self.cityListbox.insert(index, city[0]+' '+city[1])
    #

    #Check connections
    def draw_checkConnections(self):

        global adminID

        self.clear()

        self.searchKey = []

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryList = ttk.Combobox(self, state="readonly")
        self.countryList["values"] = countries
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryList.place(x=153, y=50)
        self.countryListLabel = ttk.Label(self, text="Select a country")
        self.countryListLabel.place(x=183, y=30)

        self.cityList = ttk.Combobox(self, state="readonly")
        self.cityList.bind("<<ComboboxSelected>>", self.selectCity)
        self.cityList.place(x=153, y=130)
        self.cityListLabel = ttk.Label(self, text="Select a city")
        self.cityListLabel.place(x=193, y=100)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))

        self.connectionListbox = tk.Listbox(self, width=50)
        self.connectionListbox.place(x=73, y=250)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithConnections())
        Continue.place(x=188, y=180)

        self.buttonBack()
    def fillWithConnections(self):
        global adminID
        self.connectionListbox.delete(0, tk.END)

        countryCode = self.countryList.get().split(' ')[0]
        cityCode = self.cityList.get().split(' ')[0]

        if countryCode == '':
            messagebox.showerror('ERROR', 'Please select a country')
        elif cityCode == '':
            messagebox.showerror('ERROR', 'Please select a city')
        else:

            codeList = ["05", adminID, countryCode, cityCode]
            s.send(pickle.dumps(codeList))
            connections = pickle.loads(s.recv(8192))

            if not connections:
                self.label.configure(text=self.cityList.get() + ' does not have registered connections')
                self.label.place(x=73, y=230)

            else:
                self.label.configure(text='The connections of ' + self.cityList.get() + ' are:')
                self.label.place(x=123, y=230)
                index = 0
                for connection in connections:
                    self.connectionListbox.insert(index, connection)
                    print(connection[0])
    def updateCitiesOnSelection(self, event):
        global adminID
        self.searchKey = [self.countryList.get().split(" ")[0]]
        print(self.searchKey[0])
        codeList = ["04", adminID, self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        self.cityList["values"] = cities
        print(self.searchKey)
    def selectCity(self, event):

        if len(self.searchKey) == 1:
            self.searchKey += [self.cityList.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.cityList.get().split(" ")[0]
        print(self.searchKey)
    #

    #Check routes
    def draw_checkRoutes(self):
        global adminID
        self.clear()

        codeList = ["44", adminID]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))

        self.cityCodeLabel = ttk.Label(self, text="Please select a city code to find assosiated routes")
        self.cityCodeLabel.place(x=98, y=20)

        self.cityCode = ttk.Combobox(self, state="readonly")
        self.cityCode["values"] = cities
        self.cityCode.bind("<<ComboboxSelected>>")
        self.cityCode.place(x=153, y=50)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=143, y=120)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithRoutes())
        Continue.place(x=188, y=80)

        self.routesListbox = tk.Listbox(self, width=48)
        self.routesListbox.place(x=76, y=150)

        self.buttonBack()
    def fillWithRoutes(self):
        global adminID
        self.routesListbox.delete(0, tk.END)

        city = self.cityCode.get()

        if not city:
            messagebox.showerror('ERROR', 'Please select a country')

        else:
            code = self.cityCode.get().split()[0]
            codeList = ["09", adminID, code]
            s.send(pickle.dumps(codeList))
            routes = pickle.loads(s.recv(8192))

            if not routes:
                self.label.configure(text='There are no routes associated with ' + self.cityCode.get().split(' ')[1])
                self.label.config(font=('Calibri', 10))
                self.label.place(x=98, y=120)

            else:
                self.label.configure(text='The routes associated with ' + self.cityCode.get().split(' ')[1] + ' are:')
                self.label.config(font=('Calibri', 10))
                self.label.place(x=118, y=120)
                index = 0
                for route in routes:
                    self.routesListbox.insert(index, route)
    #

    #Check trains
    def draw_checkTrains(self):
        global adminID
        self.clear()

        self.typeLabel = ttk.Label(self, text="Select a train type.")
        self.typeLabel.place(x=173, y=20)
        codeList = ["51", adminID]
        s.send(pickle.dumps(codeList))
        types = pickle.loads(s.recv(8192))

        self.type = ttk.Combobox(self, state="readonly")
        self.type["values"] = types

        self.type.bind("<<ComboboxSelected>>")
        self.type.place(x=153, y=50)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=143, y=120)

        self.trainsListbox = tk.Listbox(self, width=48)
        self.trainsListbox.place(x=86, y=150)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithTrains())
        Continue.place(x=188, y=80)

        self.buttonBack()
    def fillWithTrains(self):
        global adminID
        self.trainsListbox.delete(0, tk.END)

        type = self.type.get()
        if not type:
            messagebox.showerror('ERROR','Please select a train type')

        else:
            codeList = ["06", adminID, type]
            s.send(pickle.dumps(codeList))
            trains = pickle.loads(s.recv(8192))


            if not trains:
                self.label.configure(text='There are no type '+self.type.get()+' trains.')
                self.label.config(font=('Calibri', 10))
                self.label.place(x=158, y=120)

            else:

                self.label.configure(text='The type ' + self.type.get() + ' trains are:')
                self.label.config(font=('Calibri', 10))
                self.label.place(x=168, y=120)
                index = 0
                for train in trains:
                    self.trainsListbox.insert(index, train)
    #

    #Consult menu
    def init_consults(self):

        for child in self.winfo_children():
            child.place_forget()

        label = tk.Label(self, text='Do you want to check:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonCheckPrices = ttk.Button(self, text='Prices',
                                       command=lambda: self.draw_checkPrices())
        buttonCheckPrices.place(x=10, y=40)

        buttonCheckCountries = ttk.Button(self, text='Countries',
                                          command=lambda: self.draw_checkCountries())
        buttonCheckCountries.place(x=10, y=80)

        buttonCheckCities = ttk.Button(self, text='Cities',
                                       command=lambda: self.draw_checkCities())
        buttonCheckCities.place(x=10, y=120)

        buttonCheckConnections = ttk.Button(self, text='Connections',
                                            command=lambda: self.draw_checkConnections())
        buttonCheckConnections.place(x=130, y=40)

        buttonCheckRoutes = ttk.Button(self, text='Routes',
                                       command=lambda: self.draw_checkRoutes())
        buttonCheckRoutes.place(x=130, y=80)

        buttonCheckTrains = ttk.Button(self, text='Trains',
                                       command=lambda: self.draw_checkTrains())
        buttonCheckTrains.place(x=130, y=120)
    #


    def buttonBack(self):
        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: self.init_consults())
        buttonBACK.place(x=188, y=500)
    def clear(self):
        for child in self.winfo_children():
            child.place_forget()

#########

class DataBase(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Do you want to:')
        label.config(font=('Calibri', 11))
        label.place(x=0,y=0)

        buttonInsert = ttk.Button(self, text='Insert Data',
                             command=lambda: controller.show_frame(Insert))
        buttonInsert.place(x=5, y=40)


        buttonDelete = ttk.Button(self, text='Delete Data',
                                  command=lambda: controller.show_frame(Delete))
        buttonDelete.place(x=5, y=80)


        buttonModify = ttk.Button(self, text='Modify Data',
                                  command=lambda: controller.show_frame(Modify))
        buttonModify.place(x=5, y=120)

class Insert(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Insert:')
        label.config(font=('Calibri', 11))
        label.place(x=0,y=0)

        self.init_insert(controller)
    def init_insert(self, controller):

        self.clear()

        label = tk.Label(self, text='Insert:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonInsertCountry = ttk.Button(self, text='Country',
                                         command=lambda: self.draw_insertCountry(controller))
        buttonInsertCountry.place(x=10, y=40)

        buttonInsertCity = ttk.Button(self, text='City',
                                      command=lambda: self.draw_insertCity(controller))
        buttonInsertCity.place(x=10, y=80)

        buttonInsertConnection = ttk.Button(self, text='Connection',
                                            command=lambda: self.draw_insertConnection(controller))
        buttonInsertConnection.place(x=10, y=120)

        buttonInsertTrain = ttk.Button(self, text='Train',
                                       command=lambda: self.draw_insertTrain(controller))
        buttonInsertTrain.place(x=130, y=40)

        buttonInsertTrainType = ttk.Button(self, text='Train type',
                                           command=lambda: self.draw_insertTrainType(controller))
        buttonInsertTrainType.place(x=130, y=120)

        buttonInsertRoute = ttk.Button(self, text='Route',
                                       command=lambda: self.draw_insertRoute(controller))
        buttonInsertRoute.place(x=130, y=80)

        self.buttonBackToMenu(controller)


    #Insert country
    def draw_insertCountry(self, controller):

        self.clear()

        self.code = ttk.Entry(self)
        self.code.place(x=200, y=80)
        self.countryCodeLabel = ttk.Label(self, text="Code")
        self.countryCodeLabel.place(x=120, y=80)

        self.name = ttk.Entry(self)
        self.name.place(x=200, y=160)
        self.countryNameLabel = ttk.Label(self, text="Name")
        self.countryNameLabel.place(x=120, y=160)

        self.COUNTRY_DONE = ttk.Button(self, text='DONE',
                                command=lambda: self.createNewCountry())
        self.COUNTRY_DONE.place(x=200,y=240)

        self.buttonBackToInsert(controller)
    def createNewCountry(self):
        global adminID
        newCountryCode = self.code.get()
        newCountryName = self.name.get()

        print(newCountryCode, newCountryName)

        if newCountryCode == '' or newCountryName == '':
            messagebox.showerror('ERROR','Please fill all the gaps.')
        else:

            codeList = ["14", adminID, newCountryCode, newCountryName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showerror('ERROR','The typed code already exists')
            else:
                messagebox.showinfo("Done", "The country " + newCountryName + '(' + newCountryCode + ")  was succesfully inserted.")
    #

    #Insert city
    def draw_insertCity(self, controller):
        global adminID

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.clear()

        self.availableCountries= ttk.Combobox(self, state="readonly")
        self.availableCountries["values"] = countries

        self.availableCountries.bind("<<ComboboxSelected>>")
        self.availableCountries.place(x=180, y=50)
        self.availableCountriesLabel = ttk.Label(self, text="Add to")
        self.availableCountriesLabel.place(x=100, y=50)

        self.code = ttk.Entry(self)
        self.code.place(x=180, y=105)
        self.countryCodeLabel = ttk.Label(self, text="Code")
        self.countryCodeLabel.place(x=100, y=105)

        self.name = ttk.Entry(self)
        self.name.place(x=180, y=160)
        self.countryNameLabel = ttk.Label(self, text="Name")
        self.countryNameLabel.place(x=100, y=160)

        self.CITY_DONE = ttk.Button(self, text='DONE',
                           command=lambda: self.createNewCity())
        self.CITY_DONE.place(x=200, y=240)

        self.buttonBackToInsert(controller)
    def createNewCity(self):
        global adminID
        newCityCode = self.code.get()
        newCityName = self.name.get()
        countryCodeForCity = self.availableCountries.get().split(' ')[0]

        if newCityCode == '' or newCityName == '':
            messagebox.showerror('ERROR','Please fill all the gaps.')

        elif countryCodeForCity == '':
            messagebox.showerror('ERROR', 'Please select a country.')

        else:
            print(newCityCode)
            print(newCityName)
            print(countryCodeForCity)
            codeList = ["15", adminID, countryCodeForCity, newCityCode, newCityName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showerror('ERROR','The city is already present')
            else:
                messagebox.showinfo("Done", newCityName+'('+newCityCode+")  was succesfully inserted to the cities of "+
                                    self.availableCountries.get())
    #

    #Insert connectio
    def draw_insertConnection(self, controller):
        global adminID
        self.clear()

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryList = ttk.Combobox(self, state="readonly")
        self.countryList["values"] = countries
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryList.place(x=169, y=50)
        self.countryListLabel = ttk.Label(self, text="Select a departure country")
        self.countryListLabel.place(x=170, y=30)

        self.cityList = ttk.Combobox(self, state="readonly")
        self.cityList.bind("<<ComboboxSelected>>", self.selectCity)
        self.cityList.place(x=169, y=110)
        self.cityListLabel = ttk.Label(self, text="Select a departure city")
        self.cityListLabel.place(x=181, y=90)

        self.arrival_countryList = ttk.Combobox(self, state="readonly")
        self.arrival_countryList["values"] = countries
        self.arrival_countryList.bind("<<ComboboxSelected>>", self.updateArrivalCitiesOnSelection)
        self.arrival_countryList.place(x=169, y=170)
        self.arrival_countryListLabel = ttk.Label(self, text="Select an arrival country")
        self.arrival_countryListLabel.place(x=175, y=150)

        self.arrival_cityList = ttk.Combobox(self, state="readonly")
        self.arrival_cityList.bind("<<ComboboxSelected>>", self.selectArrivalCity)
        self.arrival_cityList.place(x=169, y=230)
        self.arrival_cityListLabel = ttk.Label(self, text="Select an arrival city")
        self.arrival_cityListLabel.place(x=186, y=210)

        self.code = ttk.Entry(self)
        self.code.place(x=180, y=290)
        self.codeLabel = ttk.Label(self, text="Enter a code")
        self.codeLabel.place(x=203, y=270)

        self.duration = ttk.Entry(self)
        self.duration.place(x=180, y=350)
        self.durationLabel = ttk.Label(self, text="Enter a duration (numbers)")
        self.durationLabel.place(x=169, y=330)

        self.CONN_DONE = ttk.Button(self, text="DONE",
                          command=lambda: self.createNewConnection())
        self.CONN_DONE.place(x=200, y=400)

        self.buttonBackToInsert(controller)
    def createNewConnection(self):
        global adminID
        newDepCountry = self.countryList.get()
        newDepCity = self.cityList.get()
        newArrCountry = self.arrival_countryList.get()
        newArrCity = self.arrival_cityList.get()

        newConnCode = self.code.get()
        newConnDuration = self.duration.get()

        params = [newArrCity, newArrCountry, newConnCode, newDepCity, newDepCountry, newConnDuration]
        if self.isIncomplete(params):
            messagebox.showerror('ERROR','Please fill all the gaps.')

        elif newDepCity == newArrCity:
            messagebox.showinfo("ERROR","Cannot depart and arrive to the same place.")

        elif not newConnDuration.isdigit():
            messagebox.showerror("ERROR","The duration must be an integral number.")

        else:
            newDepCountryCode = self.countryList.get().split(" ")[0]
            newDepCityCode = self.cityList.get().split(" ")[0]
            newArrCountryCode = self.arrival_countryList.get().split(" ")[0]
            newArrCityCode = self.arrival_cityList.get().split(" ")[0]

            codeList = ["16", adminID, newDepCountryCode, newDepCityCode, newConnCode, newArrCountryCode, newArrCityCode, newConnDuration]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showerror("Error","The connection is already present")
            else:
                messagebox.showinfo("Done","The connection was succesfully added.")


    def updateArrivalCitiesOnSelection(self, event):
        global adminID
        self.searchKey = [self.arrival_countryList.get().split(" ")[0]]
        print(self.searchKey[0])
        print("HERE")
        print(adminID)
        codeList = ["04", adminID, self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        self.arrival_cityList["values"] = cities
        print(self.searchKey)
    def selectArrivalCity(self, event):

        if len(self.searchKey) == 1:
            self.searchKey += [self.arrival_cityList.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.arrival_cityList.get().split(" ")[0]
        print(self.searchKey)
    #

    #Insert route
    def draw_insertRoute(self, controller):
        global adminID
        self.clear()

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=143, y=120)

        codeList = ["43", adminID]
        s.send(pickle.dumps(codeList))
        self.trains = pickle.loads(s.recv(8192))
        self.short_trains = self.sliceTrains(self.trains)


        self.trainCodeLabel = ttk.Label(self, text="Please select a train for the new route")
        self.trainCodeLabel.place(x=136, y=30)

        self.trainCode = ttk.Combobox(self, state="readonly")
        self.trainCode["values"] = self.short_trains
        self.trainCode.bind("<<ComboboxSelected>>")
        self.trainCode.place(x=169, y=50)

        self.buttonBackToInsert(controller)

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryList = ttk.Combobox(self, state="readonly")
        self.countryList["values"] = countries
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryList.place(x=169, y=110)
        self.countryListLabel = ttk.Label(self, text="Select an arrival country")
        self.countryListLabel.place(x=169, y=90)

        self.cityList = ttk.Combobox(self, state="readonly")
        self.cityList.bind("<<ComboboxSelected>>", self.selectCity)
        self.cityList.place(x=169, y=170)
        self.cityListLabel = ttk.Label(self, text="Select an arrival city")
        self.cityListLabel.place(x=180, y=150)

        self.priceLabel = ttk.Label(self, text="Enter a price")
        self.priceLabel.place(x=203, y=210)
        self.price = ttk.Entry(self)
        self.price.place(x=177,y=230)

        self.ROUTE_DONE = ttk.Button(self, text="DONE",
                               command=lambda: self.createNewRoute())
        self.ROUTE_DONE.place(x=200, y=300)
    def createNewRoute(self):
        global adminID
        train = self.trainCode.get()

        if train == "":
            messagebox.showerror("ERROR", "Please select a train.")

        else:
            train = self.getSelectedTrain()
            newRouteTrainType = train[0]
            newRouteTrainCode = train[1]
            newRouteDepartCountry = train[4]
            newRouteDepartCity = train[5]
            newRouteArrivalCountry = self.countryList.get().split(" ")[0]
            newRouteArrivalCity = self.cityList.get().split(" ")[0]
            newRoutePrice = self.price.get()

            params = [newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity,
                      newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice]
            if self.isIncomplete(params):
                messagebox.showerror("ERROR","Please fill all de gaps.")
            elif not newRoutePrice.isdigit():
                messagebox.showerror("ERROR", "The price must be an integral number.")
            elif newRouteArrivalCity == newRouteDepartCity:
                messagebox.showerror("ERROR", train[2]+" already departs from the selected city, please select another one.")

            else:
                codeList = ["17", adminID, newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity,
                            newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice]
                s.send(pickle.dumps(codeList))

                success = pickle.loads(s.recv(8192))

                if not success:
                    messagebox.showerror("ERROR","The entered route is already present.")
                else:
                    messagebox.showinfo("DONE", "The route was succesfully entered.")
    def sliceTrains(self, trains):
        newList = []
        for train in trains:
            newList += [[train[1], train[2]]]
        return newList
    def getSelectedTrain(self):

        self.selected = []
        searchFor = self.trainCode.get().split(" ")[0]
        for train in self.trains:
            if train[1] == searchFor:
                self.selected = train
        return self.selected
    #

    #Insert train
    def draw_insertTrain(self, controller):
        global adminID

        self.clear()

        codeList = ["51", adminID]
        s.send(pickle.dumps(codeList))
        types = pickle.loads(s.recv(8192))

        self.typeLabel = ttk.Label(self, text="Select a train type")
        self.typeLabel.place(x=189, y=30)

        self.type = ttk.Combobox(self, state="readonly")
        self.type["values"] = types

        self.type.bind("<<ComboboxSelected>>")
        self.type.place(x=169, y=50)

        self.newTrainCodeLabel = ttk.Label(self, text="Enter a train code")
        self.newTrainCodeLabel.place(x=192, y=90)
        self.newTrainCode = ttk.Entry(self)
        self.newTrainCode.place(x=177, y=110)

        self.newTrainNameLabel = ttk.Label(self, text="Enter a train name")
        self.newTrainNameLabel.place(x=191, y=150)
        self.newTrainName = ttk.Entry(self)
        self.newTrainName.place(x=175, y=170)

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.newTrainSeatsLabel = ttk.Label(self, text="Enter a number of seats")
        self.newTrainSeatsLabel.place(x=176, y=210)
        self.newTrainSeats = ttk.Entry(self)
        self.newTrainSeats.place(x=177, y=230)

        self.countryList = ttk.Combobox(self, state="readonly")
        self.countryList["values"] = countries
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryList.place(x=169, y=290)
        self.countryListLabel = ttk.Label(self, text="Select a departure country")
        self.countryListLabel.place(x=169, y=270)

        self.cityList = ttk.Combobox(self, state="readonly")
        self.cityList.bind("<<ComboboxSelected>>", self.selectCity)
        self.cityList.place(x=169, y=350)
        self.cityListLabel = ttk.Label(self, text="Select an departure city")
        self.cityListLabel.place(x=178, y=330)

        self.buttonBackToInsert(controller)

        self.TRAIN_DONE = ttk.Button(self, text="DONE",
                               command=lambda: self.createNewTrain())
        self.TRAIN_DONE.place(x=200, y=400)
    def createNewTrain(self):
        global adminID

        newTrainType = self.type.get()
        newTrainCode = self.newTrainCode.get()
        newTrainName = self.newTrainName.get()
        newTrainSeats = self.newTrainSeats.get()
        newTrainDepCountry = self.countryList.get()
        newTrainsDepCity = self.cityList.get()

        params = [newTrainType, newTrainCode, newTrainName, newTrainSeats, newTrainDepCountry, newTrainsDepCity]
        if self.isIncomplete(params):
            messagebox.showerror("ERROR","Pease fill all the gaps.")
        elif not newTrainSeats.isdigit():
            messagebox.showerror("ERROR","The number of seats must be an integral number.")
        else:

            newTrainDepCountryCode = self.countryList.get().split(" ")[0]
            newTrainsDepCityCode = self.cityList.get().split(" ")[0]

            codeList = ["18", adminID, newTrainType, newTrainCode, newTrainName, newTrainSeats, newTrainDepCountryCode,
                        newTrainsDepCityCode]
            print(codeList)
            s.send(pickle.dumps(codeList))

            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showinfo("ERROR", "The train code is already present.")
            else:
                messagebox.showinfo("DONE", "The new train was succesfully inserted")

    #

    #Insert train type
    def draw_insertTrainType(self, controller):

        self.clear()

        self.code = ttk.Entry(self)
        self.code.place(x=180, y=105)
        self.countryCodeLabel = ttk.Label(self, text="Type code")
        self.countryCodeLabel.place(x=210, y=85)

        enter = ttk.Button(self, text='DONE',
                           command=lambda: self.createNewType())
        enter.place(x=200, y=240)

        self.buttonBackToInsert(controller)
    def createNewType(self):

        code = self.code.get()

        if code == '':
            messagebox.showerror('ERROR', 'Please type  a train type.')
        else:
            newType = code
            codeList = ["50", adminID, newType]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if success:
                messagebox.showinfo("Done", "The train type was succesfully inserted.")
            else:
                messagebox.showerror("ERROR", "The type is already present.")
    #

    def buttonBackToMenu(self, controller):
        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.place(x=200, y=550)
    def buttonBackToInsert(self, controller):
        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: self.init_insert(controller))
        buttonBACK.place(x=200, y=550)
    def clear(self):
        for child in self.winfo_children():
            child.place_forget()
    def isIncomplete(self, list):
        incomplete = False
        for i in list:
            if i == "":
                incomplete = True
        return incomplete
    def updateCitiesOnSelection(self, event):
        global adminID
        self.searchKey = [self.countryList.get().split(" ")[0]]
        print(self.searchKey[0])
        codeList = ["04", adminID, self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        self.cityList["values"] = cities
        print(self.searchKey)
    def selectCity(self, event):

        if len(self.searchKey) == 1:
            self.searchKey += [self.cityList.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.cityList.get().split(" ")[0]
        print(self.searchKey)


class Delete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.init_delete(controller)


    def init_delete(self, controller):

        self.clear()

        label = tk.Label(self, text='Delete:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonDeleteCountry = ttk.Button(self, text='Country',
                                         command=lambda: self.draw_deleteCountry(controller))
        buttonDeleteCountry.place(x=10, y=40)

        buttonDeleteCity = ttk.Button(self, text='City',
                                      command=lambda: self.draw_deleteCity(controller))
        buttonDeleteCity.place(x=10, y=80)

        buttonDeleteConnection = ttk.Button(self, text='Connection',
                                            command=lambda: self.draw_deleteConnection(controller))
        buttonDeleteConnection.place(x=10, y=120)

        buttonDeleteTrain = ttk.Button(self, text='Train',
                                       command=lambda: self.draw_deleteTrain(controller))
        buttonDeleteTrain.place(x=130, y=40)

        buttonDeleteRoute = ttk.Button(self, text='Route',
                                       command=lambda: self.draw_deleteRoute(controller))
        buttonDeleteRoute.place(x=130, y=80)

        buttonDeleteAtraction = ttk.Button(self, text='Atraction',
                                           command=lambda: self.draw_deleteAttraction(controller))
        buttonDeleteAtraction.place(x=130, y=120)

        self.buttonBackToMenu(controller)

    #Delete Country
    def draw_deleteCountry(self, controller):

        self.clear()

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.deleteCountryLabel = ttk.Label(self, text="Select a country to delete")
        self.deleteCountryLabel.place(x=168, y=20)

        self.deleteCountry = ttk.Combobox(self, state="readonly")
        self.deleteCountry["values"] = countries
        self.deleteCountry.bind("<<ComboboxSelected>>")
        self.deleteCountry.place(x=166, y=50)

        Enter = ttk.Button(self, text='ENTER',
                              command=lambda: self.confirmationCountry(controller))
        Enter.place(x=200, y=80)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=153, y=120)

        self.cityListbox = tk.Listbox(self)
        self.cityListbox.place(x=178, y=150)

        self.buttonBackToDelete(controller)
    def confirmationCountry(self, controller):
        global adminID

        if self.deleteCountry.get() == "":
            messagebox.showerror("ERROR","Please select a country")
        else:
            self.cityListbox.delete(0, tk.END)

            self.searchKey = self.deleteCountry.get().split(' ')[0]
            codeList = ["04", adminID, self.searchKey]
            s.send(pickle.dumps(codeList))
            cities = pickle.loads(s.recv(8192))

            self.label.configure(text='Delete ' + self.deleteCountry.get() + '? It contains:')
            self.label.config(font=('Calibri', 10))
            self.label.place(x=150, y=120)

            index = 0
            for city in cities:
                self.cityListbox.insert(index, city[0] + ' ' + city[1])

            self.yes = ttk.Button(self, text="YES",
                                  command = lambda: self.confirmationCommandCountry("YES", controller))
            self.yes.place(x=150,y=350)


            self.no = ttk.Button(self, text="NO",
                                 command=lambda: self.confirmationCommandCountry("NO", controller))
            self.no.place(x=250, y=350)
    def confirmationCommandCountry(self, confirmation, controller):

        if confirmation == "YES":
            countryToDel = self.deleteCountry.get()
            if countryToDel == " ":
                messagebox.showerror("ERROR", "Please select a country")
            else:
                countryToDelCode = self.deleteCountry.get().split(" ")[0]
                print(countryToDelCode)
                codeList = ["19", adminID, countryToDelCode]
                s.send(pickle.dumps(codeList))
                success = pickle.loads(s.recv(8192))

                if success:
                    messagebox.showinfo("DONE", "The country was succesfully deleted")
                else:
                    messagebox.showerror("ERROR", "Could not delete country.")

        self.draw_deleteCountry(controller)
    #

    #Delete City
    def draw_deleteCity(self, controller):

        self.clear()

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryToDelete = ttk.Combobox(self, state="readonly")
        self.countryToDelete["values"] = countries
        self.countryToDelete.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryToDelete.place(x=167, y=50)
        self.countryToDeleteLabel = ttk.Label(self, text="Select a country to delete a city")
        self.countryToDeleteLabel.place(x=155, y=30)

        self.cityToDelete = ttk.Combobox(self, state="readonly")
        self.cityToDelete.bind("<<ComboboxSelected>>", self.selectCity)
        self.cityToDelete.place(x=167, y=130)
        self.cityToDeleteLabel = ttk.Label(self, text="Select a city to delete")
        self.cityToDeleteLabel.place(x=183, y=100)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))

        self.connectionListbox = tk.Listbox(self, width=50)
        self.connectionListbox.place(x=85, y=250)

        ENTER = ttk.Button(self, text='ENTER',
                              command=lambda: self.confirmationCity(controller))
        ENTER.place(x=200, y=180)

        self.buttonBackToDelete(controller)
    def confirmationCity(self, controller):

        global adminID

        self.connectionListbox.delete(0, tk.END)

        countryCode = self.countryToDelete.get().split(' ')[0]
        cityCode = self.cityToDelete.get().split(' ')[0]

        if countryCode == '':
            messagebox.showerror('ERROR', 'Please select a country')
        elif cityCode == '':
            messagebox.showerror('ERROR', 'Please select a city')
        else:

            codeList = ["05", adminID, countryCode, cityCode]
            s.send(pickle.dumps(codeList))
            connections = pickle.loads(s.recv(8192))

            if not connections:
                self.label.configure(text='Delete: ' + self.cityToDelete.get() + '? Does not contain any connections.')
                self.label.place(x=73, y=230)

            else:
                self.label.configure(text='Delete: ' + self.cityToDelete.get() + '? Contains:')
                self.label.place(x=130, y=230)
                index = 0
                for connection in connections:
                    self.connectionListbox.insert(index, connection)

        self.yes = ttk.Button(self, text="YES",
                              command=lambda: self.confirmationCommandCity("YES", controller))
        self.yes.place(x=150, y=440)

        self.no = ttk.Button(self, text="NO",
                             command=lambda: self.confirmationCommandCity("NO", controller))
        self.no.place(x=250, y=440)
    def confirmationCommandCity(self, confirmation, controller):

        if confirmation == "YES":
            countryToDel = self.countryToDelete.get()
            cityToDel = self.cityToDelete.get()
            if countryToDel == "":
                messagebox.showerror("ERROR", "Please select a country")

            elif cityToDel == "":
                messagebox.showerror("ERROR", "Please select a city")
            else:
                countryToDelCode = self.countryToDelete.get().split(" ")[0]
                cityToDelCode = self.cityToDelete.get().split(" ")[0]
                print(countryToDelCode)
                codeList = ["20", adminID, countryToDelCode, cityToDelCode]
                s.send(pickle.dumps(codeList))
                success = pickle.loads(s.recv(8192))

                if success:
                    messagebox.showinfo("DONE", "The city was succesfully deleted")
                else:
                    messagebox.showerror("ERROR", "Could not delete city.")

        self.draw_deleteCity(controller)
    #

    #Delete connection
    def draw_deleteConnection(self, controller):
        self.clear()

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryToDelete = ttk.Combobox(self, state="readonly")
        self.countryToDelete["values"] = countries
        self.countryToDelete.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryToDelete.place(x=167, y=50)
        self.countryToDeleteLabel = ttk.Label(self, text="Select the country of the connection")
        self.countryToDeleteLabel.place(x=138, y=30)

        self.cityToDelete = ttk.Combobox(self, state="readonly")
        self.cityToDelete.bind("<<ComboboxSelected>>", self.updateConnectionsOnSelection)
        self.cityToDelete.place(x=167, y=130)
        self.cityToDeleteLabel = ttk.Label(self, text="Select the city of the connection")
        self.cityToDeleteLabel.place(x=151, y=110)

        self.connectionToDelete = ttk.Combobox(self, state="readonly", width=40)
        self.connectionToDelete.bind("<<ComboboxSelected>>", self.selectCity)
        self.connectionToDelete.place(x=105, y=210)
        self.connectionToDeleteLabel = ttk.Label(self, text="Select a connection")
        self.connectionToDeleteLabel.place(x=183, y=190)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))

        ENTER = ttk.Button(self, text='ENTER',
                           command=lambda: self.confirmationConnection(controller))
        ENTER.place(x=200, y=250)

        self.buttonBackToDelete(controller)
    def confirmationConnection(self, controller):

        global adminID

        self.countryCode = self.countryToDelete.get().split(' ')[0]
        self.cityCode = self.cityToDelete.get().split(' ')[0]
        self.connection = self.connectionToDelete.get().split(' ')
        print(self.connection)

        if self.countryCode == '':
            messagebox.showerror('ERROR', 'Please select a country')
        elif self.cityCode == '':
            messagebox.showerror('ERROR', 'Please select a city')
        elif self.connection == '':
            messagebox.showerror('ERROR', 'Please select a connection')
        else:
            self.label = ttk.Label(self,text="Are you sure you want to delete '"+self.connectionToDelete.get()+"'?")
            self.label.config(font=('Calibri', 10))
            self.label.place(x=45, y=300)

            self.yes = ttk.Button(self, text="YES",
                                  command=lambda: self.confirmationCommandConnection("YES", controller))
            self.yes.place(x=150, y=440)

            self.no = ttk.Button(self, text="NO",
                                 command=lambda: self.confirmationCommandConnection("NO", controller))
            self.no.place(x=250, y=440)
    def confirmationCommandConnection(self, confirmation, controller):

        if confirmation == "YES":

            connDepCountry = self.countryCode
            connDepCity = self.cityCode
            connCode = self.connection[0]
            connArrCountry = self.connection[5]
            connArrCity = self.connection[6]

            codeList = ["21", adminID, connDepCountry, connDepCity, connCode, connArrCountry, connArrCity]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if success:
                messagebox.showinfo("DONE","The connection was succesfully deleted.")

            else:
                messagebox.showerror("ERROR","Could delete connection")


        self.draw_deleteConnection(controller)
    def updateConnectionsOnSelection(self, event):

        global adminID

        if len(self.searchKey) == 1:
           self.searchKey += [self.cityToDelete.get().split(" ")[0]]
           print(self.searchKey)
        else:
           self.searchKey[1] = self.cityToDelete.get().split(" ")[0]
           print(self.searchKey)

        codeList = ["05", adminID, self.searchKey[0], self.searchKey[1]]
        s.send(pickle.dumps(codeList))
        connections = pickle.loads(s.recv(8192))
        self.connectionToDelete["values"] = connections
    #

    #Delete Train
    def draw_deleteTrain(self, controller):
        global adminID
        self.clear()

        codeList = ["43", adminID]
        s.send(pickle.dumps(codeList))
        trains = pickle.loads(s.recv(8192))
        trains = self.sliceTrains(trains)

        self.trainCodeLabel = ttk.Label(self, text="Please select a train to delete")
        self.trainCodeLabel.place(x=146, y=20)

        self.trainCode = ttk.Combobox(self, state="readonly")
        self.trainCode["values"] = trains
        self.trainCode.bind("<<ComboboxSelected>>")
        self.trainCode.place(x=153, y=50)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=150, y=120)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.confirmationTrain(controller))
        Continue.place(x=188, y=80)

        self.pricesListbox = tk.Listbox(self, width=75)
        self.pricesListbox.place(x=10, y=150)

        self.buttonBackToDelete(controller)
    def confirmationTrain(self, controller):
        global adminID

        self.pricesListbox.delete(0, tk.END)

        train = self.trainCode.get()
        print(train)

        if train == '':
            messagebox.showerror('ERROR', 'Please select a train code')
        else:

            code = train.split(" ")[1]

            codeList = ["07", adminID, code]
            s.send(pickle.dumps(codeList))
            routes = pickle.loads(s.recv(8192))
            print(routes)

            if not routes:

                self.label.configure(text='Delete: ' + self.trainCode.get().split(' ')[2] + '? It contains no routes')
                self.label.config(font=('Calibri', 10))
                self.label.place(x=113, y=120)

            else:

                self.label.configure(text='Delete: ' + self.trainCode.get().split(' ')[2] + '? It contains:')
                self.label.config(font=('Calibri', 10))
                self.label.place(x=137, y=120)

                index = 0
                for route in routes:
                    self.pricesListbox.insert(index, route)

            self.yes = ttk.Button(self, text="YES",
                                  command=lambda: self.confirmationCommandTrain("YES", controller))
            self.yes.place(x=150, y=440)

            self.no = ttk.Button(self, text="NO",
                                 command=lambda: self.confirmationCommandTrain("NO", controller))
            self.no.place(x=250, y=440)
    def confirmationCommandTrain(self, confirmation, controller):

        train = self.trainCode.get().split(" ")
        print(train)

        if confirmation == "YES":

            trainType = train[0]
            trainCode = train[1]

            codeList = ["23", adminID, trainType, trainCode]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if success:
                messagebox.showinfo("DONE", "The train was succesfully deleted.")

            else:
                messagebox.showerror("ERROR", "Could not delete train.")

        self.draw_deleteTrain(controller)
    def sliceTrains(self, list):
        newList = []
        for i in list:
            newList += [i[0]+" "+i[1]+" "+i[2]]
        return newList
    #

    #Delete Route
    def draw_deleteRoute(self, controller):
        self.clear()

        self.routeCodeLabel = ttk.Label(self, text="Please enter a route code to delete")
        self.routeCodeLabel.place(x=142, y=20)
        self.routeCode = ttk.Entry(self)
        self.routeCode.place(x=175,y=40)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.confirmationRoute(controller))
        Continue.place(x=200, y=80)

        self.buttonBackToDelete(controller)
    def confirmationRoute(self, controller):

        if self.routeCode.get() == "":
            messagebox.showerror("ERROR", "Please type a route code")
        else:

            self.confirmLabel = ttk.Label(self, text="Are you sure?")
            self.confirmLabel.place(x=200,y=110)

            self.yes = ttk.Button(self, text="YES",
                                  command=lambda: self.confirmationCommandRoute("YES", controller))
            self.yes.place(x=150, y=150)

            self.no = ttk.Button(self, text="NO",
                                 command=lambda: self.confirmationCommandRoute("NO", controller))
            self.no.place(x=250, y=150)

    def confirmationCommandRoute(self, confirmation, controller):

        if confirmation == "YES":

            codeList = ["22", adminID, self.routeCode.get()]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if success:
                messagebox.showinfo("DONE", "The route was succesfully deleted.")
            else:
                messagebox.showerror("ERROR", "The route code does not exist.")

        self.draw_deleteRoute(controller)
    #

    #Delete Atraction
    def draw_deleteAttraction(self, controller):

        self.clear()

        codeList = ["54", adminID]
        s.send(pickle.dumps(codeList))
        attractions = pickle.loads(s.recv(8192))
        short_attractions = self.sliceAttractions(attractions)

        self.attractionLabel = ttk.Label(self, text="Select an attraction to delete")
        self.attractionLabel.place(x=160, y=20)
        self.attraction = ttk.Combobox(self, state="readonly")
        self.attraction["values"] = short_attractions
        self.attraction.bind("<<ComboboxSelected>>")
        self.attraction.place(x=163, y=50)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=200, y=120)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.confirmationAttraction(controller))
        Continue.place(x=200, y=80)

        self.buttonBackToDelete(controller)
    def confirmationAttraction(self, controller):

        if self.attraction.get() == "":
            messagebox.showerror("ERROR", "Please select an attraction")
        else:

            name = self.attraction.get().split(" ")[1]

            self.label.configure(text="Delete: "+name+"?")

            self.yes = ttk.Button(self, text="YES",
                                  command=lambda: self.confirmationCommandAttraction("YES", controller))
            self.yes.place(x=150, y=200)

            self.no = ttk.Button(self, text="NO",
                                 command=lambda: self.confirmationCommandTrain("NO", controller))
            self.no.place(x=250, y=200)
    def confirmationCommandAttraction(self, confirmation, controller):

        if confirmation == "YES":

            attCode = self.attraction.get().split(" ")[0]

            codeList = ["52", adminID, attCode]
            s.send(pickle.dumps(codeList))
            success= pickle.loads(s.recv(8192))


            if success:
                messagebox.showinfo("DONE", "The attraction was succesfully deleted")
            else:
                messagebox.showerror("ERROR", "Could not delete attraction")

        self.draw_deleteAttraction(controller)
    def sliceAttractions(self, list):
        newList = []
        for item in list:
            newList += [item[2:4]]
        return newList
    #

    def updateCitiesOnSelection(self, event):

        global adminID

        self.searchKey = [self.countryToDelete.get().split(" ")[0]]
        print(self.searchKey[0])
        codeList = ["04", adminID, self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        self.cityToDelete["values"] = cities
        print(self.searchKey)
    def selectCity(self, event):
        if len(self.searchKey) == 1:
            self.searchKey += [self.cityToDelete.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.cityToDelete.get().split(" ")[0]
        print(self.searchKey)
    def buttonBackToDelete(self, controller):
        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: self.init_delete(controller))
        buttonBACK.place(x=200, y=550)
    def buttonBackToMenu(self, controller):
        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.place(x=200, y=550)
    def clear(self):
        for child in self.winfo_children():
            child.place_forget()

class Modify(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        self.init_modify(controller)

        self.init_modify(controller)

    def init_modify(self, controller):

        self.clear()

        label = tk.Label(self, text='Modify:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonModifyPrice = ttk.Button(self, text='Prices',
                                       command=lambda: self.draw_modifyPrice(controller))
        buttonModifyPrice.place(x=10, y=40)

        buttonModifyTime = ttk.Button(self, text='Times',
                                      command=lambda: self.draw_changeTimes(controller))
        buttonModifyTime.place(x=10, y=80)

        buttonModifySeats = ttk.Button(self, text='Seats',
                                       command=lambda: self.draw_updateSeats(controller))
        buttonModifySeats.place(x=10, y=120)

        buttonModifyRoute = ttk.Button(self, text='Route',
                                       command=lambda: controller.show_frame('PENDIENTE'))
        buttonModifyRoute.place(x=130, y=40)

        buttonModifyTrain = ttk.Button(self, text='Train',
                                       command=lambda: controller.show_frame('PENDIENTE'))
        buttonModifyTrain.place(x=130, y=80)

        buttonModifyMigratoryStatus = ttk.Button(self, text='Migratory Status',
                                                 command=lambda: controller.show_frame('PENDIENTE'))
        buttonModifyMigratoryStatus.place(x=130, y=120)

        self.buttonBackToMenu(controller)

    #Price
    def draw_modifyPrice(self,controller):
        self.clear()

        self.routeLabel = ttk.Label(self, text="Enter a route code")
        self.routeLabel.place(x=190, y=50)
        self.routeEntry=ttk.Entry(self)
        self.routeEntry.place(x=177, y=80)

        self.priceLabel = ttk.Label(self, text="Enter a new price")
        self.priceLabel.place(x=190, y=130)
        self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.newPrice = ttk.Entry(self, validate='key', validatecommand=self.vcmd)
        self.newPrice.place(x=177, y=160)

        self.changePrice = ttk.Button(self, text="Change Price", command=lambda: self.getPriceModifyData(controller))
        self.changePrice.place(x=200, y=200)

        self.buttonBackToModify(controller)
    def getPriceModifyData(self, controller):

        route = self.routeEntry.get()
        newPrice = self.newPrice.get()

        if not (route or newPrice):
            messagebox.showerror("ERROR", "Please fill all the gaps.")
        else:
            codeList = ["24", "", route, newPrice]
            s.send(pickle.dumps(codeList))
            confirmation = pickle.loads(s.recv(8192))

            if confirmation:
                messagebox.showinfo("DONE", "Price changed")
                self.draw_modifyPrice(controller)
            else:
                messagebox.showerror("ERROR","Could not change price.")

    # Time
    def draw_changeTimes(self,controller):

        global adminID

        self.clear()

        self.searchKey = []

        codeList = ["03", adminID]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryList = ttk.Combobox(self, state="readonly")
        self.countryList["values"] = countries
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection)
        self.countryList.place(x=168, y=50)
        self.countryListLabel = ttk.Label(self, text="Select a country")
        self.countryListLabel.place(x=198, y=30)

        self.cityList = ttk.Combobox(self, state="readonly")
        self.cityList.bind("<<ComboboxSelected>>", self.selectCity)
        self.cityList.place(x=168, y=130)
        self.cityListLabel = ttk.Label(self, text="Select a city")
        self.cityListLabel.place(x=203, y=100)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithConnections())
        Continue.place(x=200, y=180)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))

        self.connectionListbox = tk.Listbox(self, width=50)
        self.connectionListbox.bind("<<ListboxSelect>>", self.getConnectionCode)
        self.connectionListbox.place(x=88, y=230)

        self.newTimeLabel = ttk.Label(self, text="Enter a new duration")
        self.newTimeLabel.place(x=181, y=420)

        self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.newTime = ttk.Entry(self, validate='key', validatecommand=self.vcmd)
        self.newTime.place(x=175,y=450)

        self.changeTime=ttk.Button(self,text="Change duration", command=lambda :self.modifyTimeConfirm(controller))
        self.changeTime.place(x=188,y=500)

        self.buttonBackToModify(controller)
<<<<<<< HEAD
        
=======
>>>>>>> 193fcf42d39bdcae075726ad37d1acfe2566add7
    def fillWithConnections(self):
        global adminID
        self.connectionListbox.delete(0, tk.END)

        countryCode = self.countryList.get().split(' ')[0]
        cityCode = self.cityList.get().split(' ')[0]
        if countryCode == '':
            messagebox.showerror('ERROR', 'Please select a country')
        elif cityCode == '':
            messagebox.showerror('ERROR', 'Please select a city')
        else:

            codeList = ["05", adminID, countryCode, cityCode]
            s.send(pickle.dumps(codeList))
            connections = pickle.loads(s.recv(8192))

            if not connections:
                self.label.configure(text=self.cityList.get() + ' does not have registered connections')
                self.label.place(x=73, y=230)

            else:
                self.label.configure(text='The connections of ' + self.cityList.get() + ' are:')
                self.label.place(x=123, y=230)
                index = 0
                for connection in connections:
                    self.connectionListbox.insert(index, connection)
                    print(connection[0])
    def updateCitiesOnSelection(self, event):
        global adminID
        self.searchKey = [self.countryList.get().split(" ")[0]]
        print(self.searchKey[0])
        codeList = ["04", adminID, self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        self.cityList["values"] = cities
        print(self.searchKey)
    def selectCity(self, event):

        if len(self.searchKey) == 1:
            self.searchKey += [self.cityList.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.cityList.get().split(" ")[0]
        print(self.searchKey)
    def getConnectionCode(self,event):

        if len(self.searchKey)==2:
            self.searchKey+=[self.connectionListbox.get(self.connectionListbox.curselection())[0]]
            print(self.searchKey[2])
        elif len(self.searchKey)==3:
            self.searchKey[2]=self.connectionListbox.get(self.connectionListbox.curselection())[0]
    def modifyTimeConfirm(self,controller):

        if not self.searchKey:
            messagebox.showerror("ERROR", "Please fill all the gaps.")
        elif len(self.searchKey) == 1:
            messagebox.showerror("ERROR", "Please select a city.")
        elif len(self.searchKey) == 2:
            messagebox.showerror("ERROR", "Please select a connection.")
        else:

            country = self.searchKey[0]
            city = self.searchKey[1]
            connection = self.searchKey[2]
            newTime = self.newTime.get()

            if not newTime:
                messagebox.showerror("ERROR", "Please enter a new duration.")
            else:
                codeList = ["25", "", country, city, connection, newTime]
                s.send(pickle.dumps(codeList))
                confirmation = pickle.loads(s.recv(8192))

                if confirmation:
                    messagebox.showinfo("DONE", "Time changed")
                    self.draw_changeTimes(controller)
                else:
                    messagebox.showerror("ERROR", "Could not change time.")

    #Seats
    def draw_updateSeats(self,controller):
        self.clear()

        self.modifyKey=[]

        trainTypelabel=ttk.Label(self,text="Select train Type")
        trainTypelabel.pack(pady=10)

        self.trainType=ttk.Combobox(self)
        self.trainType["values"]=['01','02','03','04']
        self.trainType.bind("<<ComboboxSelected>>", self.updateTrains)
        self.trainType.pack()

        trainCodelabel=ttk.Label(self,text="Select Train")
        trainCodelabel.pack(pady=10)

        self.trains=ttk.Combobox(self)
        self.trains.bind("<<ComboboxSelected>>", self.getTrain)
        self.trains.pack()

        trainSeatslabel=ttk.Label(self, text=" New seats")
        trainSeatslabel.pack(pady=10)

        self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.newSeats = ttk.Entry(self, validate='key', validatecommand=self.vcmd)
        self.newSeats.pack()

        modify=ttk.Button(self, text="Modify", command=lambda:self.modifySeats(controller))
        modify.pack(pady=10)

        self.buttonBackToModify(controller)

    def updateTrains(self, event):
        self.modifyKey=[self.trainType.get()]

        codeList = ["06", "",self.modifyKey[0]]
        s.send(pickle.dumps(codeList))
        trainElement = pickle.loads(s.recv(8192))

        self.trains["values"]=trainElement
    def getTrain(self, event):
        if len(self.modifyKey)==1:
            self.modifyKey+=[self.trains.get().split(" ")[1]]
        elif len(self.modifyKey)==2:
            self.modifyKey[1]=self.trains.get().split(" ")[1]
        print(self.modifyKey)
    def modifySeats(self,controller):
        if self.newSeats.get()=="" or len(self.modifyKey)!=2:
            messagebox.showinfo("","All info is necessary")
        else:
            codeList = ["26", "", self.modifyKey[0], self.modifyKey[1], self.newSeats.get()]
            s.send(pickle.dumps(codeList))
            updateSeats = pickle.loads(s.recv(8192))

            self.init_modify(controller)
            messagebox.showinfo("","Seats updated successfully")





    #Misc
    def validate(self, action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789.-+':
            try:
                float(value_if_allowed)
                return True
            except ValueError:
                if value_if_allowed == "":
                    return True
                else:
                    return False

        else:
            return False
    def buttonBackToModify(self, controller):
        button = ttk.Button(self, text='BACK',
                            command=lambda: self.init_modify(controller))
        button.place(x=200,y=550)
    def buttonBackToMenu(self, controller):
        button = ttk.Button(self, text='BACK',
                            command=lambda: controller.show_frame(AdminMainMenu))
        button.place(x=200,y=550)
    def clear(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()


#########

class History(ttk.Frame):


    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text='See history of:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        self.init_history(controller)

    def init_history(self, controller):

        self.clear()

        buttonLastInserted = ttk.Button(self, text='Last insterted',
                                  command=lambda: self.lastInserted(controller))
        buttonLastInserted.place(x=10, y=40)


        buttonLastDeleted = ttk.Button(self, text='Last deleted',
                            command=lambda: self.lastDeleted(controller))
        buttonLastDeleted.place(x=10, y=80)


        buttonMostUsed = ttk.Button(self, text='Most Used',
                            command=lambda: self.mostUsed(controller))
        buttonMostUsed.place(x=10, y=120)


        buttonLeastUsed = ttk.Button(self, text='Least Used',
                            command=lambda: self.leastUsed(controller))
        buttonLeastUsed.place(x=10, y=160)

        buttonMostVisited = ttk.Button(self, text='Most visited',
                            command=lambda: self.mostVisited(controller))
        buttonMostVisited.place(x=130, y=40)

        buttonMostFrequentUsers = ttk.Button(self, text='Most frequent users',
                            command=lambda: self.mostFrequentUsers(controller))
        buttonMostFrequentUsers.place(x=130, y=80)


        buttonLeastFrequentUsers = ttk.Button(self, text='Least frequent users',
                            command=lambda: self.leastFrequentUsers(controller))
        buttonLeastFrequentUsers.place(x=130, y=120)

    def lastInserted(self, controller):

        self.clear()

        self.drawTheInfo(controller, "30")

    def lastDeleted(self, controller):

        self.clear()

        self.drawTheInfo(controller, "31")

    def mostVisited(self, controller):

        self.clear()

        label = ttk.Label(self, text="Select an option:")
        label.config(font=("Calibri", 10))
        label.place(x=180,y=10)

        self.countries = ttk.Button(self, text="Countries",
                              command=lambda: self.drawTheInfo(controller, "34"))
        self.countries.place(x=138, y=40)

        self.cities = ttk.Button(self, text="Cities",
                             command=lambda: self.drawTheInfo(controller, "35"))
        self.cities.place(x=238, y=40)


        self.buttonBackToMenu(controller)

    def mostUsed(self, controller):

        self.clear()

        self.drawTheInfo(controller, "32")

    def leastUsed(self, controller):

        self.clear()

        self.drawTheInfo(controller, "33")

    def mostFrequentUsers(self, controller):

        self.clear()

        self.drawTheInfo(controller, "36")

    def leastFrequentUsers(self, controller):

        self.clear()

        self.drawTheInfo(controller, "37")


    def drawTheInfo(self, controller, code):


        self.infoListBox = tk.Listbox(self, width=53, height=20)
        self.infoListBox.place(x=77, y=100)
        codeList = [code, adminID]
        s.send(pickle.dumps(codeList))
        info = pickle.loads(s.recv(8192))
        print(info)

        if not info:
            self.infoListBox.insert(0,"Nothing to show.")
        else:
            index = 0
            for item in info:
                self.infoListBox.insert(index, item)
        self.buttonBackToMenu(controller)


    def clear(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()
    def buttonBackToMenu(self, controller):
        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: self.init_history(controller))
        buttonBACK.place(x=188, y=500)


class logIn(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.passwordLabel = ttk.Label(self, text="Enter Admin ID")
        self.passwordLabel.place(x=120, y=100)
        self.password= ttk.Entry(self, show='*')
        self.password.place(x=230,y=100)


        self.logIn=ttk.Button(self,text="Log In",command=lambda : self.getLoginInfo(controller))
        self.logIn.place(x=200,y=200)
        # controller.show_frame(AdminMainMenu)

    def getLoginInfo(self, controller):
        global adminID
        password=self.password.get()

        codeList = ["12", "", password]
        s.send(pickle.dumps(codeList))
        adminValidate = pickle.loads(s.recv(8192))

        if adminValidate != "1":
            if adminValidate:
                # ADDS TO GLOBAL VARIABLE adminID the admin id
                adminID = password

                # Lock server here:
                codeList = ["45", "", adminID]
                s.send(pickle.dumps(codeList))

                self.draw_mainMenu(controller)
                print("success")

                # Set logged flag (ESTO DEBE SER UNA VARIABLE GLOBAL)
                logged = True


            else:

                messagebox.showinfo("Access denied", "Wrong User Name or password")


            loginError = True
        else:
            messagebox.showinfo("Access denied", "Server is blocked")

        # #global adminFormatList
        # login_success=False
        # #Eddit to fit logInList indexes
        # registeredUser = ''
        # for user in adminFormatList:
        #     if password==user[1]:
        #         registeredUser = user
        #         login_success=True
        # if not login_success:
        #     messagebox.showinfo("Access denied", "Wrong Admin ID")
        # elif login_success:
        #     loggedIn = registeredUser[0]
        #     self.draw_mainMenu(controller)

    def draw_mainMenu(self, controller):
        controller.show_frame(AdminMainMenu)


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



    app = mainApp()
    app.title('UTS Europe - Admin Module')
    app.geometry('500x600')
    app.resizable(0, 0)
    app.mainloop()
