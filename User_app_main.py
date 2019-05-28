import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import socket, os, pickle

class map(ttk.Frame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.img = Image.open("newDataFiles/Assets/europe_map(3).png")
        self.display =ImageTk.PhotoImage(self.img)
        self.map= tk.Label(self,image=self.display, bd=5, relief="ridge")
        self.map.pack()

        #Spain
        self.pin= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin = ImageTk.PhotoImage(self.pin)
        self.pinButton=ttk.Button(self, command= lambda:self.create_window("90"))
        self.pinButton.config(image=self.displayPin)
        self.pinButton.place(x=90,y=330)

        #Portugal
        self.pin2= Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin2 = ImageTk.PhotoImage(self.pin2)
        self.pinButton2=ttk.Button(self, command= lambda :self.create_window("23"))
        self.pinButton2.config(image=self.displayPin2)
        self.pinButton2.place(x=50,y=330)

        #France
        self.pin3= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin3 = ImageTk.PhotoImage(self.pin3)
        self.pinButton3=ttk.Button(self, command= lambda :self.create_window("78"))
        self.pinButton3.config(image=self.displayPin3)
        self.pinButton3.place(x=150,y=270)

        #Switzerland
        self.pin4= Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin4 = ImageTk.PhotoImage(self.pin4)
        self.pinButton4=ttk.Button(self, command= lambda :self.create_window("234"))
        self.pinButton4.config(image=self.displayPin4)
        self.pinButton4.place(x=190,y=270)

        #Jordania
        self.pin6= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin6 = ImageTk.PhotoImage(self.pin6)
        self.pinButton6=ttk.Button(self, command= lambda :self.create_window("45"))
        self.pinButton6.config(image=self.displayPin6)
        self.pinButton6.place(x=400,y=380)

        #Netherlands
        self.pin7= Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin7 = ImageTk.PhotoImage(self.pin7)
        self.pinButton7=ttk.Button(self, command= lambda :self.create_window("134"))
        self.pinButton7.config(image=self.displayPin7)
        self.pinButton7.place(x=175,y=210)

        #Turkey
        self.pin8= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin8 = ImageTk.PhotoImage(self.pin8)
        self.pinButton8=ttk.Button(self, command= lambda :self.create_window("24"))
        self.pinButton8.config(image=self.displayPin8)
        self.pinButton8.place(x=380,y=330)

        #Belgium
        self.pin10= Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin10 = ImageTk.PhotoImage(self.pin10)
        self.pinButton10=ttk.Button(self, command= lambda :self.create_window("32"))
        self.pinButton10.config(image=self.displayPin10)
        self.pinButton10.place(x=165,y=230)

        #Greece
        self.pin12= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin12 = ImageTk.PhotoImage(self.pin12)
        self.pinButton12=ttk.Button(self, command= lambda :self.create_window("02"))
        self.pinButton12.config(image=self.displayPin12)
        self.pinButton12.place(x=315,y=353)

        #Czech republic
        self.pin13= Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin13 = ImageTk.PhotoImage(self.pin13)
        self.pinButton13=ttk.Button(self, command= lambda :self.create_window("456"))
        self.pinButton13.config(image=self.displayPin13)
        self.pinButton13.place(x=235,y=240)

        #Poland
        self.pin14= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin14 = ImageTk.PhotoImage(self.pin14)
        self.pinButton14=ttk.Button(self, command= lambda :self.create_window("120"))
        self.pinButton14.config(image=self.displayPin14)
        self.pinButton14.place(x=260,y=205)

        #Romain
        self.pin15= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin15 = ImageTk.PhotoImage(self.pin15)
        self.pinButton15=ttk.Button(self, command= lambda :self.create_window("149"))
        self.pinButton15.config(image=self.displayPin15)
        self.pinButton15.place(x=315,y=270)

        #Ukraine
        self.pin16= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin16 = ImageTk.PhotoImage(self.pin16)
        self.pinButton16=ttk.Button(self, command= lambda :self.create_window("256"))
        self.pinButton16.config(image=self.displayPin16)
        self.pinButton16.place(x=350,y=220)

        #Bulgaria
        self.pin17= Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin17 = ImageTk.PhotoImage(self.pin17)
        self.pinButton17=ttk.Button(self, command= lambda :self.create_window("280"))
        self.pinButton17.config(image=self.displayPin17)
        self.pinButton17.place(x=330,y=310)

        #Finland
        self.pin18= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin18 = ImageTk.PhotoImage(self.pin18)
        self.pinButton18=ttk.Button(self, command= lambda :self.create_window("18"))
        self.pinButton18.config(image=self.displayPin18)
        self.pinButton18.place(x=280,y=90)

        #Sweden
        self.pin19= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin19 = ImageTk.PhotoImage(self.pin19)
        self.pinButton19=ttk.Button(self, command= lambda :self.create_window("180"))
        self.pinButton19.config(image=self.displayPin19)
        self.pinButton19.place(x=230,y=90)

        #Germany
        self.pin20 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin20 = ImageTk.PhotoImage(self.pin20)
        self.pinButton20 = ttk.Button(self, command= lambda : self.create_window("499"))
        self.pinButton20.config(image=self.displayPin20)
        self.pinButton20.place(x=200, y=220)

        #Eritrea
        self.pin21 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin21 = ImageTk.PhotoImage(self.pin21)
        self.pinButton21 = ttk.Button(self, command= lambda : self.create_window("05"))
        self.pinButton21.config(image=self.displayPin21)
        self.pinButton21.place(x=200, y=220)

    def addNewMenu(self):
        t = tk.Toplevel(self)
        t.img = Image.open("newDataFiles/Assets/europe_map(3).png")
        self.display =ImageTk.PhotoImage(self.img)
        #t.wm_title(country)
        l = tk.Label(t, text="This is window is country")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def create_window(self, country):
        self.newWindow = newWindow(country)

class newWindow:
    def __init__(self, country):
        self.createCountryMap(country)

    def createCountryMap(self, country):
        self._sideWindow = tk.Toplevel()
        imageURL = ""
        if country=="23":
            imageURL = "newDataFiles/Assets/portugal.png"
        elif country == "90":
            imageURL = "newDataFiles/Assets/spain.png"
        elif country == "78":
            imageURL = "newDataFiles/Assets/france.gif"
        elif country == "234":
            imageURL = "newDataFiles/Assets/switzerland.png"
        elif country == "45":
            imageURL = "newDataFiles/Assets/jordan.png"
        elif country == "134":
            imageURL = "newDataFiles/Assets/netherlands.png"
        elif country == "24":
            imageURL = "newDataFiles/Assets/turkey.gif"
        elif country == "32":
            imageURL = "newDataFiles/Assets/belgium.png"
        elif country == "02":
            imageURL = "newDataFiles/Assets/Greece.png"
        elif country == "456":
            imageURL = "newDataFiles/Assets/Czech Republic.png"
        elif country == "120":
            imageURL = "newDataFiles/Assets/poland.png"
        elif country == "149":
            imageURL = "newDataFiles/Assets/romania.png"
        elif country == "256":
            imageURL = "newDataFiles/Assets/ukraine.png"
        elif country == "280":
            imageURL = "newDataFiles/Assets/bulgaria.png"
        elif country == "18":
            imageURL = "newDataFiles/Assets/finland.png"
        elif country == "180":
            imageURL = "newDataFiles/Assets/switzerland.png"
        elif country == "499":
            imageURL = "newDataFiles/Assets/Germany.png"
        elif country == "05":
            imageURL = "newDataFiles/Assets/Eritrea.png"

        codeList = ["42", country]
        s.send(pickle.dumps(codeList))
        countryName = pickle.loads(s.recv(8192))
        amount = "Country: "+countryName
        self.imageGIF2 = tk.PhotoImage(file=imageURL)
        self.imageLabel2 = tk.Label(self._sideWindow, image=self.imageGIF2)
        tk.Label(self._sideWindow, text=amount, font="none 15 bold").grid(row=0, column=1, sticky='N', padx=10, pady=10)
        self.imageLabel2.grid(row=0, column=0, padx=10, pady=10)

        #self.imageLabel2 = tk.Label(self._sideWindow, image=self.imageGIF2)
        #self.imageLabel2.grid(row=0, column=1, padx=10, pady=10)
        #l = tk.Label(t, text="This is window is country")
        #l.pack(side="top", fill="both", expand=True, padx=100, pady=100)

    def displayCityData(self, city):
        pass


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

        self.departureCountryList = ttk.Combobox(self, state="readonly")
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.departureCountryList["values"] = pickle.loads(s.recv(8192))
        self.departureCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionFixed)
        self.departureCountryList.place(x=250, y=50)
        self.departureCountryListLabel=ttk.Label(self, text="Countries")
        self.departureCountryListLabel.place(x=100, y=50)

        self.departureCityList = ttk.Combobox(self, state="readonly")
        self.departureCityList.bind("<<ComboboxSelected>>", self.selectCityFixed)
        self.departureCityList.place(x=250, y=100)
        self.departureCityListLabel=ttk.Label(self, text="Cities")
        self.departureCityListLabel.place(x=100, y = 100)


        self.routeRecervation=ttk.Button(self, text="Continue", command=self.routeList)
        self.routeRecervation.place(x=300, y =200)

        self.backButton=ttk.Button(self, text="Back", command= self.backToLogIn)
        self.backButton.place(x=80,y=200)

    def drawCustomRecervation(self):
        for child in self.winfo_children():
            child.place_forget()

        self.searchKey=[]

        self.departureCountryList = ttk.Combobox(self, state="readonly")
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.departureCountryList["values"] = pickle.loads(s.recv(8192))
        self.departureCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionCustom1)
        self.departureCountryList.place(x=250, y=50)
        self.departureCountryListLabel=ttk.Label(self, text="Departure Country")
        self.departureCountryListLabel.place(x=100, y=50)

        self.departureCityList = ttk.Combobox(self, state="readonly")
        self.departureCityList.bind("<<ComboboxSelected>>", self.selectCityCustom1)
        self.departureCityList.place(x=250, y=100)
        self.departureCityListLabel=ttk.Label(self, text="Departure City")
        self.departureCityListLabel.place(x=100, y = 100)

        self.arrivalCountryList = ttk.Combobox(self, state="readonly")
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.arrivalCountryList["values"] = pickle.loads(s.recv(8192))

        self.arrivalCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionCustom2)
        self.arrivalCountryList.place(x=250, y=200)
        self.ArrivalCountryListLabel = ttk.Label(self, text="Arrival Country")
        self.ArrivalCountryListLabel.place(x=100, y=200)

        self.arrivalCityList = ttk.Combobox(self, state="readonly")
        self.arrivalCityList.bind("<<ComboboxSelected>>", self.selectCityCustom2)
        self.arrivalCityList.place(x=250, y=250)
        self.arrivalCityListLabel = ttk.Label(self, text="Arrival City")
        self.arrivalCityListLabel.place(x=100, y=250)

        self.routeRecervation = ttk.Button(self, text="Continue", command=self.routeList)
        self.routeRecervation.place(x=300, y=350)

        self.backButton = ttk.Button(self, text="Back", command=self.backToLogIn)
        self.backButton.place(x=80, y=350)


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
    def updateCitiesOnSelectionCustom2(self, event):

        if len(self.searchKey)==2:
            self.searchKey+=[self.arrivalCountryList.get().split(" ")[0]]
        else:
            self.searchKey[2]= self.arrivalCountryList.get().split(" ")[0]

        print(self.searchKey[0])
        codeList = ["04", self.searchKey[2]]
        s.send(pickle.dumps(codeList))
        self.arrivalCityList["values"] = pickle.loads(s.recv(8192))
        print(self.searchKey)
    def selectCityCustom2(self, event):

        if len(self.searchKey)==3:
             self.searchKey+=[self.arrivalCityList.get().split(" ")[0]]
        elif len(self.searchKey)==4:
            self.searchKey[3]=self.arrivalCityList.get().split(" ")[0]
        print(self.searchKey)


    def backToLogIn(self):
        for child in self.winfo_children():
            child.place_forget()
        self.chooseRecervation()

    def routeList(self):
        if self.searchKey==[]:
            messagebox.showinfo("","Please select a contry and a city")
        elif len(self.searchKey)==2 or len(self.searchKey)==4:
            for child in self.winfo_children():
                child.place_forget()


            self.routesListBox = tk.Listbox(self, width=69, height=20, selectmode=tk.SINGLE)

            if len(self.searchKey)==2:
                codeList = ["10", self.searchKey[0], self.searchKey[1]]
                s.send(pickle.dumps(codeList))
                tempList = pickle.loads(s.recv(8192))

                for i in tempList:
                    self.routesListBox.insert(tk.END,i)


            elif len(self.searchKey)==4:
                codeList = ["41", self.searchKey[0], self.searchKey[1], self.searchKey[2], self.searchKey[3]]
                s.send(pickle.dumps(codeList))
                routes = pickle.loads(s.recv(8192))

                for i in routes:
                    self.routesListBox.insert(tk.END,i)
                

            self.routesListBox.bind("<<ListboxSelect>>", self.getListBox )
            self.routesListBox.place(x=19,y=20)


            self.backButton=ttk.Button(self, text="Back", command=self.backToCountCitSelect)
            self.backButton.place(x=90,y=380)

            self.billingButton=ttk.Button(self, text="Continue", command = self.continueToBilling)
            self.billingButton.place(x=290, y=380)

            self.vcmd = (self.register(self.validate),'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            self.amountOfSeats = ttk.Entry (self, validate = 'key',validatecommand=self.vcmd)
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

    def backToCountCitSelect(self):
        for child in self.winfo_children():
            child.place_forget()
        if len(self.searchKey)==2:
            self.drawFixedRecervation()
        elif len(self.searchKey)==4:
            self.drawCustomRecervation()

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


class Queries(ttk.Frame):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)

        self.checkCountries=ttk.Button(self, text="Countries", command=self.countries)
        self.checkCountries.pack(pady=10)

        self.checkCities=ttk.Button(self, text="Cities", command=self.cities1)
        self.checkCities.pack(pady=10)

        self.checkConnections=ttk.Button(self, text="Conections", command=self.conections1)
        self.checkConnections.pack(pady=10)

        self.checkTrains=ttk.Button(self,text="Trains", command=self.trains1)
        self.checkTrains.pack(pady=10)

        self.checkPrices=ttk.Button(self, text="Prices", command= self.prices1)
        self.checkPrices.pack(pady=10)

        self.checkTrainSeats=ttk.Button(self, text="Train Seats", command= self.seats1)
        self.checkTrainSeats.pack(pady=10)

        self.checkRoutes=ttk.Button(self,text="Routes", command= self.routes1)
        self.checkRoutes.pack(pady=10)

    def init(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()

        self.checkCountries = ttk.Button(self, text="Countries", command=self.countries)
        self.checkCountries.pack(pady=10)

        self.checkCities = ttk.Button(self, text="Cities", command=self.cities1)
        self.checkCities.pack(pady=10)

        self.checkConnections = ttk.Button(self, text="Conections", command=self.conections1)
        self.checkConnections.pack(pady=10)

        self.checkTrains = ttk.Button(self, text="Trains", command=self.trains1)
        self.checkTrains.pack(pady=10)

        self.checkPrices = ttk.Button(self, text="Prices", command= self.prices1)
        self.checkPrices.pack(pady=10)

        self.checkTrainSeats = ttk.Button(self, text="Train Seats", command= self.seats1)
        self.checkTrainSeats.pack(pady=10)

        self.checkRoutes = ttk.Button(self, text="Routes", command= self.routes1)
        self.checkRoutes.pack(pady=10)

    def countries(self):
        for child in self.winfo_children():
            child.pack_forget()



        self.countryList=tk.Listbox(self, width=50)

        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        countryListServer = pickle.loads(s.recv(8192))

        for i in countryListServer:
            self.countryList.insert(tk.END,i)

        self.countryList.pack()

        self.back=ttk.Button(self, text="back", command= self.init)
        self.back.pack()

    def cities1(self):
        for child in self.winfo_children():
            child.pack_forget()

        self.searchKey=[]

        self.selectCountry=ttk.Combobox(self)
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.selectCountry["values"] = pickle.loads(s.recv(8192))
        self.selectCountry.bind("<<ComboboxSelected>>", self.cities1_get)
        self.selectCountry.pack()



        self.continueToCities=ttk.Button(self, text="Continue", command=self.cities2)
        self.continueToCities.pack()

        self.back = ttk.Button(self, text="back", command=self.init)
        self.back.pack()
    def cities1_get(self, event):
        self.searchKey=[self.selectCountry.get().split(" ")[0]]
        print(self.searchKey)
    def cities2(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.cityList = tk.Listbox(self, width=50)
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cityListServer = pickle.loads(s.recv(8192))

        for i in cityListServer:
            self.cityList.insert(tk.END,i)
            print(i)

        self.cityList.pack()

        self.back = ttk.Button(self, text="back", command=self.cities1)
        self.back.pack()

    def conections1(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.searchKey=[]

        self.departureCountryList = ttk.Combobox(self, state="readonly")
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.departureCountryList["values"] = pickle.loads(s.recv(8192))
        self.departureCountryList.bind("<<ComboboxSelected>>", self.conections_update)
        self.departureCountryList.place(x=250, y=50)
        self.departureCountryListLabel=ttk.Label(self, text="Countries")
        self.departureCountryListLabel.place(x=100, y=50)

        self.departureCityList = ttk.Combobox(self, state="readonly")
        self.departureCityList.bind("<<ComboboxSelected>>", self.conections_addToSearch)
        self.departureCityList.place(x=250, y=100)
        self.departureCityListLabel=ttk.Label(self, text="Cities")
        self.departureCityListLabel.place(x=100, y = 100)


        self.routeRecervation=ttk.Button(self, text="Continue", command=self.conections2)
        self.routeRecervation.place(x=300, y =200)

        self.backButton=ttk.Button(self, text="Back", command= self.init)
        self.backButton.place(x=80,y=200)
    def conections_update(self, event):


        self.searchKey=[self.departureCountryList.get().split(" ")[0]]


        print(self.searchKey[0])
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        self.departureCityList["values"] = pickle.loads(s.recv(8192))
        print(self.searchKey)
    def conections_addToSearch(self, event):

        if len(self.searchKey)==1:
             self.searchKey+=[self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1]=self.departureCityList.get().split(" ")[0]
        print(self.searchKey)
    def conections2(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.conectionsList = tk.Listbox(self, width=50)

        codeList = ["05", self.searchKey[0], self.searchKey[1]]
        s.send(pickle.dumps(codeList))
        connectionListServer = pickle.loads(s.recv(8192))

        for i in connectionListServer:
            self.conectionsList.insert(tk.END,i)

        self.conectionsList.pack()

        self.back = ttk.Button(self, text="back", command=self.conections1)
        self.back.pack()

    def trains1(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.trainType=ttk.Combobox(self)
        self.trainType["values"]=['1','2','3','4']
        self.trainType.bind("<<ComboboxSelected>>", self.trains_get)
        self.trainType.pack()

        self.continueToTrains=ttk.Button(self, text="Continue", command=self.trains2)
        self.continueToTrains.pack()


        self.back=ttk.Button(self, text="Back", command=self.init)
        self.back.pack()
    def trains_get(self, event):
        self.searchKey=self.trainType.get()
        print(self.searchKey)
    def trains2(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.trainList = tk.Listbox(self, width=50)

        codeList = ["06", self.searchKey]
        s.send(pickle.dumps(codeList))
        trainListServer = pickle.loads(s.recv(8192))

        for i in trainListServer:
            self.trainList.insert(tk.END, i)
            print(i)

        self.trainList.pack()

        self.back = ttk.Button(self, text="back", command=self.trains1)
        self.back.pack()

    def prices1(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()

        self.searchKey=[]


        self.trainCode=ttk.Entry(self)
        self.trainCode.pack()


        self.continueToRoutes=ttk.Button(self, text="Continue", command = self.prices2)
        self.continueToRoutes.pack(side=tk.BOTTOM)

        self.back=ttk.Button(self, text="Back", command=self.init)
        self.back.pack(side=tk.BOTTOM)
    def prices2(self):
        codeList = ["07", self.trainCode.get()]
        s.send(pickle.dumps(codeList))
        pricesServer = pickle.loads(s.recv(8192))
        if pricesServer==[]:
            messagebox.showinfo("","Incorrect train code")
        else:
            self.searchKey = [self.trainCode.get()]
            print(self.searchKey)

            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            self.prices=tk.Listbox(self, width=50)

            for i in pricesServer:
                self.prices.insert(tk.END,i)
                print(i)


            self.prices.pack()

            self.back = ttk.Button(self, text="back", command=self.prices1)
            self.back.pack()


    def seats1(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()

        self.searchKey = []

        self.trainCode = ttk.Entry(self)
        self.trainCode.pack()

        self.continueToRoutes = ttk.Button(self, text="Continue", command=self.seats2)
        self.continueToRoutes.pack(side=tk.BOTTOM)

        self.back = ttk.Button(self, text="Back", command=self.init)
        self.back.pack(side=tk.BOTTOM)
    def seats2(self):
        codeList = ["08", self.trainCode.get()]
        s.send(pickle.dumps(codeList))
        seatsServer = pickle.loads(s.recv(8192))

        if seatsServer == []:
            messagebox.showinfo("", "Incorrect train code")
        else:
            self.searchKey = [self.trainCode.get()]
            print(self.searchKey)

            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            self.seats = tk.Listbox(self, width=50)

            for i in seatsServer:
                self.seats.insert(tk.END, i)
                print(i)

            self.seats.pack()

            self.back = ttk.Button(self, text="back", command=self.prices1)
            self.back.pack()


    def routes1(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.searchKey=[]

        self.departureCountryList = ttk.Combobox(self, state="readonly")
        codeList = ["03"]
        s.send(pickle.dumps(codeList))
        self.departureCountryList["values"] = pickle.loads(s.recv(8192))
        self.departureCountryList.bind("<<ComboboxSelected>>", self.routesUpdate)
        self.departureCountryList.place(x=250, y=50)
        self.departureCountryListLabel=ttk.Label(self, text="Countries")
        self.departureCountryListLabel.place(x=100, y=50)

        self.departureCityList = ttk.Combobox(self, state="readonly")
        self.departureCityList.bind("<<ComboboxSelected>>", self.routesAdd)
        self.departureCityList.place(x=250, y=100)
        self.departureCityListLabel=ttk.Label(self, text="Cities")
        self.departureCityListLabel.place(x=100, y = 100)


        self.routeRecervation=ttk.Button(self, text="Continue", command=self.routes2)
        self.routeRecervation.place(x=300, y =200)

        self.backButton=ttk.Button(self, text="Back", command= self.init)
        self.backButton.place(x=80,y=200)
    def routesUpdate(self, event):

        self.searchKey = [self.departureCountryList.get().split(" ")[0]]

        print(self.searchKey[0])
        codeList = ["04", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        self.departureCityList["values"] = pickle.loads(s.recv(8192))
        print(self.searchKey)
    def routesAdd(self, event):

        if len(self.searchKey) == 1:
            self.searchKey += [self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.departureCityList.get().split(" ")[0]
        print(self.searchKey)
    def routes2(self):
        if self.searchKey==[]:
            messagebox.showinfo("","Please select a country and a city")
        else:
            print(self.searchKey)
            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            self.routeList = tk.Listbox(self, width=50)

            codeList = ["09", self.searchKey[1]]
            s.send(pickle.dumps(codeList))
            routesServer = pickle.loads(s.recv(8192))

            for i in routesServer:
                self.routeList.insert(tk.END,i)


            self.routeList.pack()

            self.back = ttk.Button(self, text="back", command=self.routes1)
            self.back.pack()

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

        self.checkDataBase=Queries(self.notebook)
        self.notebook.add(self.checkDataBase,text="Queries", padding=10)


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