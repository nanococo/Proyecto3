import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import Image,ImageTk
from tkinter import Tk, Canvas
import socket, os, pickle

loggedIn = ''

""""
Estas son las listas 
de prueba para todo.
*No era necesario este tipo de string 
solo queria usarlo y sentirme cool*
"""
countriesFormat = [['code','name',[['codeCityA','nameCityA',[['connection code', 'arrival country', 'arrival city','duration'],['connection code', 'arrival country', 'arrival city', 'duration']]],
                ['ARH','OJBHDIA',[['605AB', 'ES', 'ALC','12']],['codeCityC','nameCityC',[]]]]],['code','name',[['codeCityA','nameCityA',[['connection code', 'arrival country', 'arrival city','duration'],['connection code', 'arrival country', 'arrival city', 'duration']]],
                ['codeCityB','nameCityB',[['connection code', 'arrival country', 'arrival city','duration']],['codeCityC','nameCityC',[]]]]],['code','name',[['codeCityA','nameCityA',[['connection code', 'arrival country', 'arrival city','duration'],['connection code', 'arrival country', 'arrival city', 'duration']]],
                ['codeCityB','nameCityB',[['connection code', 'arrival country', 'arrival city','duration']],['codeCityC','nameCityC',[]]]]]]

trainsFormat = [['03','5BF67','LIMOSINA','745','ES','LEI',[['TR','AYT','259'],['arrival country','arrival city','price']]],
                ['type','ID','name','capacity', 'departure country', 'departure city',[['arrival country','arrival city','price']]]]

adminFormatList = [['1','a'],['2','b'],['3','c'],['4', 'd'],['5','e'],['Jorge Gutierrez', '2019077521']]

usersFormat = [['a','1','1'],['b', '2', '0'],['c','3','0']]

class mainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self,default='C:/Users\jguty\OneDrive\Pictures/icono.ico')

        container = tk.Frame(self)
        container.pack(side='top', fill='both',  expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menuBar = tk.Menu(container)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label='LogOut', command= lambda: self.show_frame(logIn))
        fileMenu.add_separator()
        fileMenu.add_command(label='End program', command=quit)
        menuBar.add_cascade(label='Exit', menu=fileMenu)
        tk.Tk.config(self, menu=menuBar)


        self.frames = {}

        for F in (AdminMainMenu, Consult, ConsultPrices,ConsultTrains,ConsultRoutes,ConsultConnections,ConsultCities,
                  ConsultCountries, DataBase, Insert,Delete, Modify, logIn):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(AdminMainMenu)

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
        label = tk.Label(self, text='Do you want to check:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)


        buttonCheckPrices = ttk.Button(self, text='Prices',
                             command=lambda: controller.show_frame(ConsultPrices))
        buttonCheckPrices.place(x=10, y=40)


        buttonCheckCountries = ttk.Button(self, text='Countries',
                             command=lambda: controller.show_frame(ConsultCountries))
        buttonCheckCountries.place(x=10, y=80)


        buttonCheckCities = ttk.Button(self, text='Cities',
                                       command=lambda: controller.show_frame(ConsultCities))
        buttonCheckCities.place(x=10, y=120)


        buttonCheckConnections = ttk.Button(self, text='Connections',
                             command=lambda: controller.show_frame(ConsultConnections))
        buttonCheckConnections.place(x=130, y=40)


        buttonCheckRoutes = ttk.Button(self, text='Routes',
                             command=lambda: controller.show_frame(ConsultRoutes))
        buttonCheckRoutes.place(x=130, y=80)


        buttonCheckTrains = ttk.Button(self, text='Trains',
                             command=lambda: controller.show_frame(ConsultTrains))
        buttonCheckTrains.place(x=130, y=120)


###FRAMES DE LAS CONSULTAS###
class ConsultPrices(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='These are the current ticket prices for our routes:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        self.checkPrices()

        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

    def checkPrices(self):

        for child in self.winfo_children():
            child.place_forget()

        self.trainCodeLabel = ttk.Label(self, text="Please type a train code to find assosiated route prices")
        self.trainCodeLabel.place(x=100, y=20)

        self.trainCode = ttk.Entry(self)
        self.trainCode.place(x=175, y=40)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=155, y=120)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithPrices())
        Continue.place(x=200, y=80)

        self.pricesListbox = tk.Listbox(self, width=79)
        self.pricesListbox.place(x=10, y=150)

    def fillWithPrices(self):

        self.pricesListbox.delete(0, tk.END)

        code = self.trainCode.get()
        print(code)
        if code == '':
            messagebox.showinfo('ERROR','Please type a train code')
        else:
            codeList = ["07", code]
            s.send(pickle.dumps(codeList))
            prices = pickle.loads(s.recv(8192))
            print(prices)

            self.label.configure(text='The route prices of are:')
            self.label.config(font=('Calibri', 10))
            self.label.place(x=160, y=120)


            index = 0
            for route in prices:
                self.cityListbox.insert(index, route)

class ConsultCountries(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='These are the registered countries:')
        label.config(font=('Calibri', 11))
        label.place(x=130, y=20)

        self.checkCoutries()

        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

    def checkCoutries(self):

        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        self.countryListbox = tk.Listbox(self, width=30, height=30)

        index = 0
        for country in countries:
            self.countryListbox.insert(index, country[0]+' '+country[1])
        self.countryListbox.place(x=155, y=50)

class ConsultCities(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='These are the registered cities:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        self.checkCities()

        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

    def checkCities(self):

        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))
        print(countries)

        for child in self.winfo_children():
            child.place_forget()

        self.selection = StringVar()

        self.availableCountries = ttk.Combobox(self, state="readonly", textvariable=self.selection)
        self.availableCountries["values"] = countries

        self.availableCountries.bind("<<ComboboxSelected>>")
        self.availableCountries.place(x=165, y=50)
        self.availableCountriesLabel = ttk.Label(self, text="Please choose a country to find associated cities:")
        self.availableCountriesLabel.place(x=105, y=20)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))
        self.label.place(x=155, y=120)

        Continue = ttk.Button(self, text='Continue',
                                command=lambda: self.fillWithCities())
        Continue.place(x=200,y=80)

        self.cityListbox = tk.Listbox(self)
        self.cityListbox.place(x=175, y=150)

        print(self.selection.get())

    def fillWithCities(self):

        self.cityListbox.delete(0, tk.END)

        self.searchKey = self.availableCountries.get().split(' ')[0]
        codeList = ["04", self.searchKey]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))

        self.label.configure(text='The cities of '+self.selection.get()+' are:')
        self.label.config(font=('Calibri',10))
        self.label.place(x=160,y=120)

        index = 0
        for city in cities:
            self.cityListbox.insert(index, city[0]+' '+city[1])

class ConsultConnections(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.checkConnections()

        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

    def checkConnections(self):
        self.searchKey = []

        self.countryList = ttk.Combobox(self, state="readonly")
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))
        self.countryList["values"] = countries
        self.countryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionFixed)
        self.countryList.place(x=165, y=50)
        self.countryListLabel = ttk.Label(self, text="Select a country")
        self.countryListLabel.place(x=195, y=30)

        self.cityList = ttk.Combobox(self, state="readonly")
        self.cityList.bind("<<ComboboxSelected>>", self.selectCityFixed)
        self.cityList.place(x=165, y=130)
        self.cityListLabel = ttk.Label(self, text="Select a city")
        self.cityListLabel.place(x=205, y=100)

        self.label = tk.Label(self, text='')
        self.label.config(font=('Calibri', 10))

        self.connectionListbox = tk.Listbox(self, width=50)
        self.connectionListbox.place(x=85, y=250)

        Continue = ttk.Button(self, text='Continue',
                              command=lambda: self.fillWithConnections())
        Continue.place(x=200, y=180)

    def fillWithConnections(self):

        self.connectionListbox.delete(0, tk.END)

        countryCode = self.countryList.get().split(' ')[0]
        cityCode = self.cityList.get().split(' ')[0]

        if countryCode == '':
            messagebox.showinfo('ERROR','Please select a country')
        elif cityCode == '':
            messagebox.showinfo('ERROR', 'Please select a city')
        else:

            codeList = ["05",countryCode,cityCode]
            s.send(pickle.dumps(codeList))
            connections = pickle.loads(s.recv(8192))

            if not connections:
                self.label.configure(text=self.cityList.get() + ' does not have registered connections')
                self.label.place(x=85,y=230)

            else:
                self.label.configure(text='The connections of '+self.cityList.get()+' are:')
                self.label.place(x=135, y=230)
                index = 0
                for connection in connections:
                    self.connectionListbox.insert(index, connection)


    def updateCitiesOnSelectionFixed(self, event):


        self.searchKey=[self.countryList.get().split(" ")[0]]
        print(self.searchKey[0])
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        self.cityList["values"] = cities
        print(self.searchKey)

    def selectCityFixed(self, event):

        if len(self.searchKey)==1:
             self.searchKey+=[self.cityList.get().split(" ")[0]]
        else:
            self.searchKey[1]=self.cityList.get().split(" ")[0]
        print(self.searchKey)

class ConsultRoutes(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='These are the registered routes:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        self.checkRoutes()

        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

    def checkRoutes(self):

        global trainsFormat

        y = 0
        for train in trainsFormat:
            if train[6]:
                x = 0
                y += 30
                label = tk.Label(self, text='Train:' + train[2])
                label.config(font=('Calibri', 10))
                label.place(x=x, y=y)
                for route in train[6]:
                    y += 30
                    x = 20
                    label = tk.Label(self,text='Route: ' + train[4] + ', ' + train[5] + ' - ' + route[0] +', '+route[1])
                    label.config(font=('Calibri', 13))
                    label.place(x=x, y=y)


class ConsultTrains(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='These are the registered trains:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        self.checkTrains()

        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

    def checkTrains(self):

        global trainsFormat

        y = 0
        for train in trainsFormat:
            if train[6]:
                x = 0
                y += 30
                label = tk.Label(self, text=train[1]+' - '+train[2]+', Type: '+train[0])
                label.config(font=('Calibri', 12))
                label.place(x=x, y=y)
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

        buttonInsertCountry = ttk.Button(self, text='Country',
                                  command=lambda: self.draw_insertCountry(controller))
        buttonInsertCountry.place(x=10, y=40)


        buttonInsertCity = ttk.Button(self, text='City',
                                  command=lambda: self.draw_insertCity(controller))
        buttonInsertCity.place(x=10, y=80)


        buttonInsertConnection = ttk.Button(self, text='Connection',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertConnection.place(x=10, y=120)


        buttonInsertTrainType = ttk.Button(self, text='Train type',
                                  command=lambda: self.draw_insertTrainType(controller))
        buttonInsertTrainType.place(x=10, y=160)


        buttonInsertTrain = ttk.Button(self, text='Train',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertTrain.place(x=130, y=40)


        buttonInsertRoute = ttk.Button(self, text='Route',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertRoute.place(x=130, y=80)

        buttonInsertAtraction = ttk.Button(self, text='Atraction',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertAtraction.place(x=130, y=120)


        buttonBACK = ttk.Button(self, text='BACK',
                                command=lambda: self.back_insert(controller))
        buttonBACK.pack(side='bottom')


    def draw_insertCountry(self, controller):
        for child in self.winfo_children():
            child.place_forget()

        fill = tk.Label(self, text='Please fill the gaps.')
        fill.config(font=('Calibri',13))
        fill.place(x=0,y=0)

        self.code = tk.Entry(self)
        self.code.place(x=230, y=80)
        self.countryCodeLabel = ttk.Label(self, text="Code")
        self.countryCodeLabel.place(x=120, y=80)

        self.name = tk.Entry(self)
        self.name.place(x=230, y=160)
        self.countryNameLabel = ttk.Label(self, text="Name")
        self.countryNameLabel.place(x=120, y=160)

        enter = ttk.Button(self, text='Enter',
                                command=lambda: self.createNewCountry(controller))
        enter.place(x=200,y=240)

    def createNewCountry(self, controller):

        newCountryCode = self.code.get()
        newCountryName = self.name.get()

        print(newCountryCode, newCountryName)

        if newCountryCode == '' or newCountryName == '':
            messagebox.showinfo('ERROR','Please fill all the gaps.')
        else:

            codeList = ["14", newCountryCode, newCountryName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showinfo('ERROR','The typed code already exists')
            else:
                messagebox.showinfo("Done", "The country " + newCountryName + '(' + newCountryCode + ")  was succesfully inserted.")
                self.back_insert(controller)




    def draw_insertCity(self, controller):

        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        countries = pickle.loads(s.recv(8192))

        for child in self.winfo_children():
            child.place_forget()

        fill = tk.Label(self, text='Please fill the gaps.')
        fill.config(font=('Calibri', 13))
        fill.place(x=0, y=0)

        self.availableCountries= ttk.Combobox(self, state="readonly")
        self.availableCountries["values"] = countries

        self.availableCountries.bind("<<ComboboxSelected>>")
        self.availableCountries.place(x=180, y=50)
        self.availableCountriesLabel = ttk.Label(self, text="Add to")
        self.availableCountriesLabel.place(x=100, y=50)

        self.code = tk.Entry(self)
        self.code.place(x=180, y=105)
        self.countryCodeLabel = ttk.Label(self, text="Code")
        self.countryCodeLabel.place(x=100, y=105)

        self.name = tk.Entry(self)
        self.name.place(x=180, y=160)
        self.countryNameLabel = ttk.Label(self, text="Name")
        self.countryNameLabel.place(x=100, y=160)

        enter = ttk.Button(self, text='Enter',
                           command=lambda: self.createNewCity(controller))
        enter.place(x=200, y=240)

    def createNewCity(self,controller):

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
            codeList = ["15", countryCodeForCity, newCityCode, newCityName]
            s.send(pickle.dumps(codeList))
            success = pickle.loads(s.recv(8192))

            if not success:
                messagebox.showinfo('ERROR','The city is already present')
            else:
                messagebox.showinfo("Done", newCityName+'('+newCityCode+")  was succesfully inserted to the cities of "+
                                    self.availableCountries.get())
                self.back_insert(controller)

    def draw_insertConnection(self, controller):

        # global countriesFormat
        #
        # cities = []
        # for country in countriesFormat:
        #     for city in country[2]:
        #         cities += [city[0] + '-' + city[1]]
        #
        # for child in self.winfo_children():
        #     child.place_forget()
        #
        # self.availableCities = ttk.Combobox(self, state="readonly")
        # self.availableCities["values"] = cities
        #
        # self.availableCountries.bind("<<ComboboxSelected>>")
        # self.availableCountries.place(x=180, y=50)
        # self.availableCountriesLabel = ttk.Label(self, text="Add to")
        # self.availableCountriesLabel.place(x=100, y=50)
        #
        # self.code = tk.Entry(self)
        # self.code.place(x=180, y=105)
        # self.CodeLabel = ttk.Label(self, text="Code")
        # self.CodeLabel.place(x=100, y=105)
        #
        # self.country = tk.Entry(self)
        # self.country.place(x=180, y=160)
        # self.countryLabel = ttk.Label(self, text="Duration")
        #
        # enter = ttk.Button(self, text='Enter',
        #                    command=lambda: self.createNewConnection(controller))
        # enter.place(x=200, y=240)

        """" PENDIENTE """

    def draw_insertTrainType(self, controller):

        for child in self.winfo_children():
            child.place_forget()

        fill = tk.Label(self, text='Please fill the gaps.')
        fill.config(font=('Calibri', 13))
        fill.place(x=0, y=0)

        self.code = tk.Entry(self)
        self.code.place(x=180, y=105)
        self.countryCodeLabel = ttk.Label(self, text="Type code")
        self.countryCodeLabel.place(x=100, y=105)

        self.name = tk.Entry(self)
        self.name.place(x=180, y=160)
        self.countryNameLabel = ttk.Label(self, text="Type name")
        self.countryNameLabel.place(x=100, y=160)

        enter = ttk.Button(self, text='Enter',
                           command=lambda: self.createNewCountry(controller))
        enter.place(x=200, y=240)

    def createNewType(self, controller):

        code = self.code.get()
        name = self.name.get()

        if code == '' or name == '':
            messagebox.showinfo('ERROR', 'Please fill all the gaps.')
        else:
            newType = [code, name, []]
            messagebox.showinfo("Done", "The train type " + name + '(' + code + ")  was succesfully inserted.")
            self.back_insert(controller)

    def back_insert(self, controller):
        controller.show_frame(AdminMainMenu)
        self.Insert(controller)

    def Insert(self, controller):
        for child in self.winfo_children():
            child.place_forget()

        label = tk.Label(self, text='Insert:')
        label.config(font=('Calibri', 11))
        label.place(x=0, y=0)

        buttonInsertCountry = ttk.Button(self, text='Country',
                                         command=lambda: self.draw_insertCountry(controller))
        buttonInsertCountry.place(x=10, y=40)

        buttonInsertCountry = ttk.Button(self, text='City',
                                         command=lambda: self.draw_insertCity(controller))
        buttonInsertCountry.place(x=10, y=80)

        buttonInsertConnection = ttk.Button(self, text='Connection',
                                  command=lambda: self.draw_insertConnection(controller))
        buttonInsertConnection.place(x=10, y=120)

        buttonInsertTrainType = ttk.Button(self, text='Train type',
                                           command=lambda: self.draw_insertTrainType(controller))
        buttonInsertTrainType.place(x=10, y=160)


class Delete(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Delete:')
        label.config(font=('Calibri', 11))
        label.place(x=0,y=0)

        buttonInsertCountry = ttk.Button(self, text='Country',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertCountry.place(x=10, y=40)


        buttonInsertCity = ttk.Button(self, text='City',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertCity.place(x=10, y=80)


        buttonInsertConnection = ttk.Button(self, text='Connection',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertConnection.place(x=10, y=120)


        buttonInsertTrainType = ttk.Button(self, text='Train type',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertTrainType.place(x=10, y=160)


        buttonInsertTrain = ttk.Button(self, text='Train',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertTrain.place(x=130, y=40)


        buttonInsertRoute = ttk.Button(self, text='Route',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertRoute.place(x=130, y=80)

        buttonInsertAtraction = ttk.Button(self, text='Atraction',
                                  command=lambda: controller.show_frame('PENDIENTE'))
        buttonInsertAtraction.place(x=130, y=120)


        buttonBACK = ttk.Button(self, text='BACK',
                            command=lambda: controller.show_frame(AdminMainMenu))
        buttonBACK.pack(side='bottom')

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
        password=self.password.get()

        codeList = ["12", password]
        s.send(pickle.dumps(codeList))
        adminValidate = pickle.loads(s.recv(8192))



        if adminValidate:

            # AQUI DEJA CARGAR NUEVA VENTANA
            # Set userName here:
            codeList = ["02", password]
            s.send(pickle.dumps(codeList))
            userName = pickle.loads(s.recv(8192))

            self.draw_mainMenu(controller)
            print("success")

            # Set logged flag (ESTO DEBE SER UNA VARIABLE GLOBAL)
            logged = True


        else:

            messagebox.showinfo("Access denied", "Wrong User Name or password")

            loginError = True

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
    app.resizable(0,0)
    app.mainloop()
