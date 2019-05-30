import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk
from tkinter import Tk, Canvas
import socket, os, pickle

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
            messagebox.showinfo('ERROR', 'Please type a train code')
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
            newList += [i[1]+' '+i[2]]
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

        self.label.configure(text='The cities of '+self.selection.get()+' are:')
        self.label.config(font=('Calibri',10))
        self.label.place(x=150,y=120)

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
            messagebox.showinfo('ERROR', 'Please select a country')
        elif cityCode == '':
            messagebox.showinfo('ERROR', 'Please select a city')
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
            messagebox.showinfo('ERROR', 'Please select a country')

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
            messagebox.showinfo('ERROR','Please select a train type')

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

        # buttonInsertTrainType = ttk.Button(self, text='Train type',
        #                           command=lambda: self.draw_insertTrainType(controller))
        # buttonInsertTrainType.place(x=10, y=160)

        # buttonInsertAtraction = ttk.Button(self, text='Atraction',
        #                           command=lambda: controller.show_frame('PENDIENTE'))
        # buttonInsertAtraction.place(x=130, y=120)

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
        buttonInsertTrainType.place(x=10, y=160)

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
            messagebox.showinfo('ERROR','Please fill all the gaps.')
        else:

            codeList = ["14", adminID, newCountryCode, newCountryName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showinfo('ERROR','The typed code already exists')
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
            messagebox.showinfo('ERROR','Please fill all the gaps.')

        elif countryCodeForCity == '':
            messagebox.showinfo('ERROR', 'Please select a country.')

        else:
            print(newCityCode)
            print(newCityName)
            print(countryCodeForCity)
            codeList = ["15", adminID, countryCodeForCity, newCityCode, newCityName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showinfo('ERROR','The city is already present')
            else:
                messagebox.showinfo("Done", newCityName+'('+newCityCode+")  was succesfully inserted to the cities of "+
                                    self.availableCountries.get())
    #

    #Insert connection
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
            messagebox.showinfo('ERROR','Please fill all the gaps.')

        elif newDepCity == newArrCity:
            messagebox.showinfo("ERROR","Cannot depart and arrive to the same place.")

        elif not newConnDuration.isdigit():
            messagebox.showinfo("ERROR","The duration must be an integral number.")

        else:
            newDepCountryCode = self.countryList.get().split(" ")[0]
            newDepCityCode = self.cityList.get().split(" ")[0]
            newArrCountryCode = self.arrival_countryList.get().split(" ")[0]
            newArrCityCode = self.arrival_cityList.get().split(" ")[0]

            codeList = ["16", adminID, newDepCountryCode, newDepCityCode, newConnCode, newArrCountryCode, newArrCityCode, newConnDuration]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showinfo("Error","The connection is already present")
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
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelection2)
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
            messagebox.showinfo("ERROR", "Please select a train.")

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
                messagebox.showinfo("ERROR","Please fill all de gaps.")
            elif not newRoutePrice.isdigit():
                messagebox.showinfo("ERROR", "The price must be an integral number.")
            elif newRouteArrivalCity == newRouteDepartCity:
                messagebox.showinfo("ERROR", train[2]+" already departs from the selected city, please select another one.")

            else:
                codeList = ["17", adminID, newRouteTrainType, newRouteTrainCode, newRouteDepartCountry, newRouteDepartCity,
                            newRouteArrivalCountry, newRouteArrivalCity, newRoutePrice]
                s.send(pickle.dumps(codeList))

                success = pickle.loads(s.recv(8192))

                if not success:
                    messagebox.showinfo("ERROR","The entered route is already present.")
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

        self.typeLabel = ttk.Label(self, text="Select a train type")
        self.typeLabel.place(x=189, y=30)

        self.type = ttk.Combobox(self, state="readonly")
        self.type["values"] = ['01',
                               '02',
                               '03',
                               '04', ]

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
            messagebox.showinfo("ERROR","Pease fill all the gaps.")
        elif not newTrainSeats.isdigit():
            messagebox.showinfo("ERROR","The number of seats must be an integral number.")
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
            messagebox.showinfo('ERROR', 'Please type  a train type.')
        else:
            newType = code
            codeList = ["50", adminID, newType]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if success:
                messagebox.showinfo("Done", "The train type was succesfully inserted.")
            else:
                messagebox.showinfo("ERROR", "The type is already present.")
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
                                      command=lambda: controller.show_frame('PENDIENTE'))
        buttonDeleteCity.place(x=10, y=80)

        buttonDeleteConnection = ttk.Button(self, text='Connection',
                                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonDeleteConnection.place(x=10, y=120)

        buttonDeleteTrain = ttk.Button(self, text='Train',
                                       command=lambda: controller.show_frame('PENDIENTE'))
        buttonDeleteTrain.place(x=130, y=40)

        buttonDeleteRoute = ttk.Button(self, text='Route',
                                       command=lambda: controller.show_frame('PENDIENTE'))
        buttonDeleteRoute.place(x=130, y=80)

        buttonDeleteAtraction = ttk.Button(self, text='Atraction',
                                           command=lambda: controller.show_frame('PENDIENTE'))
        buttonDeleteAtraction.place(x=130, y=120)

        self.buttonBackToMenu(controller)

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

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.confirmation(controller))
        Continue.place(x=200, y=80)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=153, y=120)

        self.cityListbox = tk.Listbox(self)
        self.cityListbox.place(x=178, y=150)

        self.buttonBackToInsert(controller)

    def confirmation(self, controller):
        global adminID

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
                              command = lambda: self.confirmationCommand("YES", controller))
        self.yes.place(x=150,y=350)


        self.no = ttk.Button(self, text="NO",
                             command=lambda: self.confirmationCommand("NO", controller))
        self.no.place(x=250, y=350)

    def confirmationCommand(self, confirmation, controller):

        if confirmation == "YES":
            countryToDel = self.deleteCountry.get()
            if countryToDel == " ":
                messagebox.showinfo("ERROR", "Please select a country")
            else:
                countryToDelCode = self.deleteCountry.get().split(" ")[0]
                print(countryToDelCode)
                codeList = ["19", adminID, countryToDelCode]
                s.send(pickle.dumps(codeList))
                success = pickle.loads(s.recv(8192))

                if success:
                    messagebox.showinfo("DONE", "The country was succesfully deleted")
                else:
                    messagebox.showinfo("ERROR", "Could not delete country.")

        self.draw_deleteCountry(controller)



    def buttonBackToInsert(self, controller):
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
        label = tk.Label(self, text='Modify:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonModifyPrice = ttk.Button(self, text='Prices',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonModifyPrice.place(x=10, y=40)

        buttonModifyTime = ttk.Button(self, text='Times',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonModifyTime.place(x=10, y=80)

        buttonModifySeats = ttk.Button(self, text='Seats',
                                  command=lambda: controller.show_frame('PENDIENTE'))
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

        button = ttk.Button(self, text='BACK',
                            command=lambda: controller.show_frame(AdminMainMenu))
        button.pack(side='bottom')
#########

class History(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = tk.Label(self, text='See history of:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonLastInserted = ttk.Button(self, text='Last insterted',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonLastInserted.place(x=10, y=40)


        buttonLastDeleted = ttk.Button(self, text='Last deleted',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonLastDeleted.place(x=10, y=80)


        buttonMostUsed = ttk.Button(self, text='Most Used',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonMostUsed.place(x=10, y=120)


        buttonLeastUsed = ttk.Button(self, text='Least Used',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonLeastUsed.place(x=10, y=160)

        buttonMostVisited = ttk.Button(self, text='Most visited',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonMostVisited.place(x=130, y=40)


        buttonLeastVisited = ttk.Button(self, text='Least visited',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonLeastVisited.place(x=130, y=80)


        buttonMostFrequentUsers = ttk.Button(self, text='Most frequent users',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonMostFrequentUsers.place(x=130, y=120)


        buttonLeastFrequentUsers = ttk.Button(self, text='Least frequent users',
                            command=lambda: controller.show_frame('PENDIENTE'))
        buttonLeastFrequentUsers.place(x=130, y=160)

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
