import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import socket, os, pickle

#
reservations=[]
userID=str
#

class Map(ttk.Frame):
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

        #UK
        self.pin6= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin6 = ImageTk.PhotoImage(self.pin6)
        self.pinButton6=ttk.Button(self, command= lambda :self.create_window("123"))
        self.pinButton6.config(image=self.displayPin6)
        self.pinButton6.place(x=120,y=210)

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

        #ITALY
        self.pin21= Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin21 = ImageTk.PhotoImage(self.pin21)
        self.pinButton21=ttk.Button(self, command= lambda :self.create_window("05"))
        self.pinButton21.config(image=self.displayPin21)
        self.pinButton21.place(x=220,y=320)

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

        codeList = ["42", "", country]
        s.send(pickle.dumps(codeList))
        countryName = pickle.loads(s.recv(8192))
        self._sideWindow.title(countryName)

        imageURL = ""
        if country=="23":
            imageURL = "newDataFiles/Assets/resized/portugal.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            #LISBOA
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("14", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=90, y=330)

            #SANTAREM
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("45", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=150, y=170)

            #ALBUFEIRA
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("90", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=140, y=300)

            # CASTELO BRANCO
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("20", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=170, y=330)

            # SEVILLA
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("100", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=110, y=290)

            # OPORTP
            self.pin6 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin6 = ImageTk.PhotoImage(self.pin6)
            self.pinButton6 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("10", country))
            self.pinButton6.config(image=self.displayPin6)
            self.pinButton6.place(x=120, y=90)
        elif country == "90":
            imageURL = "newDataFiles/Assets/resized/spain.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            #MADRID
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("11", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            #VALLADOLID
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("99", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            #SANTIAGO
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("124", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=30, y=75)

            # COMPOSTELA
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("134", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=170, y=200)

            # MALAGA
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("59", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=110, y=290)

            # VALENCIA
            self.pin6 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin6 = ImageTk.PhotoImage(self.pin6)
            self.pinButton6 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("78", country))
            self.pinButton6.config(image=self.displayPin6)
            self.pinButton6.place(x=250, y=190)
        elif country == "78":
            imageURL = "newDataFiles/Assets/resized/france.gif"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            #TOULOUSE
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("302", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            #MONTPELLIER
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("7", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            #MARSELLA
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("32", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=75)

            # LYON
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("40", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=170, y=200)

            # NANTES
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("16", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=110, y=290)

            # PARIS
            self.pin6 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin6 = ImageTk.PhotoImage(self.pin6)
            self.pinButton6 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("17", country))
            self.pinButton6.config(image=self.displayPin6)
            self.pinButton6.place(x=250, y=190)
        elif country == "234":
            imageURL = "newDataFiles/Assets/resized/switzerland.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # LICHTENSTEIN
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("115", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # ZURICH
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("116", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            # BERNA
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("176", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=75)

            # GINEBRA
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("89", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=250, y=170)
        elif country == "123":
            imageURL = "newDataFiles/Assets/resized/UK.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()
        elif country == "134":
            imageURL = "newDataFiles/Assets/resized/netherlands.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # ROTERDAM
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("466", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # LA HAYA
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("963", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=300, y=120)

            # AMSTERDAM
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("470", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=75)
        elif country == "24":
            imageURL = "newDataFiles/Assets/resized/turkey.gif"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # ANKARA
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("220", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # ESTAMBUL
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("451", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            # BURSA
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("852", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=75)

            # ANTALYA
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("456", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=300, y=120)

            # ADANA
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("198", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=250, y=120)
        elif country == "32":
            imageURL = "newDataFiles/Assets/resized/belgium.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # GANTE
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("489", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # BRUJAS
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("159", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            # AMBERES
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("13", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=75)
        elif country == "02":
            imageURL = "newDataFiles/Assets/resized/Greece.png"
            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # ATENAS
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("220", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=130, y=150)
        elif country == "456":
            imageURL = "newDataFiles/Assets/resized/Czech Republic.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # OSTRAVA
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("874", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # PRAGA
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("95", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)
        elif country == "120":
            imageURL = "newDataFiles/Assets/resized/poland.png"
            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # KATOWICE
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("781", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=50, y=50)

            # VARSOVIA
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("472", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=150)

            # BRESLAVIA
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("632", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=180, y=75)

            # BIALYSTOCK
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("459", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=100, y=120)

            # CRACOVIA
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("596", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=170, y=120)
        elif country == "149":
            imageURL = "newDataFiles/Assets/resized/romania.png"
            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # TIMISOARA
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("123", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=250, y=50)

            # IASI
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("9", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=150)
        elif country == "256":
            imageURL = "newDataFiles/Assets/resized/ukraine.png"
            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # KIEV
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("321", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=110, y=50)

            # LEOPOLIS
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("999", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=180, y=150)

            # KRIVOU ROG
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("753", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=220, y=75)
        elif country == "280":
            imageURL = "newDataFiles/Assets/resized/bulgaria.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # SOFIA
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("921", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=100, y=150)
        elif country == "18":
            imageURL = "newDataFiles/Assets/resized/finland.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # TURKU
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("42", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=110, y=50)

            # HELSINSKI
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("413", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=180, y=150)
        elif country == "180":
            imageURL = "newDataFiles/Assets/resized/sweden.png"

            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # ESTOCOLMO
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("291", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=110, y=250)
        elif country == "499":
            imageURL = "newDataFiles/Assets/resized/Germany.png"
            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # MUNICH
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("140", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # HANNOVER
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("43", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            # STTUGART
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("23", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=45)

            # FRANKFORT
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("178", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=170, y=75)

            # BREMEN
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("150", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=210, y=230)

            # BERLIN
            self.pin6 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin6 = ImageTk.PhotoImage(self.pin6)
            self.pinButton6 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("493", country))
            self.pinButton6.config(image=self.displayPin6)
            self.pinButton6.place(x=265, y=270)

            # NUREMBERG
            self.pin7 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin7 = ImageTk.PhotoImage(self.pin7)
            self.pinButton7 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("130", country))
            self.pinButton7.config(image=self.displayPin7)
            self.pinButton7.place(x=210, y=190)
        elif country == "05":
            imageURL = "newDataFiles/Assets/resized/italy.png"
            self.img = Image.open(imageURL)
            self.display = ImageTk.PhotoImage(self.img)
            self.map = tk.Label(self._sideWindow, image=self.display, bd=5, relief="ridge")
            self.map.pack()

            # NAPOLES
            self.pin = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin = ImageTk.PhotoImage(self.pin)
            self.pinButton = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("111", country))
            self.pinButton.config(image=self.displayPin)
            self.pinButton.place(x=160, y=150)

            # FLORENCIA
            self.pin2 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin2 = ImageTk.PhotoImage(self.pin2)
            self.pinButton2 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("190", country))
            self.pinButton2.config(image=self.displayPin2)
            self.pinButton2.place(x=120, y=120)

            # GENOVA
            self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin3 = ImageTk.PhotoImage(self.pin3)
            self.pinButton3 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("47", country))
            self.pinButton3.config(image=self.displayPin3)
            self.pinButton3.place(x=210, y=45)

            # SAN MARINO
            self.pin4 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin4 = ImageTk.PhotoImage(self.pin4)
            self.pinButton4 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("579", country))
            self.pinButton4.config(image=self.displayPin4)
            self.pinButton4.place(x=170, y=75)

            # VENECIA
            self.pin5 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin5 = ImageTk.PhotoImage(self.pin5)
            self.pinButton5 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("888", country))
            self.pinButton5.config(image=self.displayPin5)
            self.pinButton5.place(x=210, y=230)

            # ROMA
            self.pin6 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin6 = ImageTk.PhotoImage(self.pin6)
            self.pinButton6 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("258", country))
            self.pinButton6.config(image=self.displayPin6)
            self.pinButton6.place(x=265, y=270)

            # TURIN
            self.pin7 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin7 = ImageTk.PhotoImage(self.pin7)
            self.pinButton7 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("119", country))
            self.pinButton7.config(image=self.displayPin7)
            self.pinButton7.place(x=210, y=190)

            # BOLONIA
            self.pin8 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin8 = ImageTk.PhotoImage(self.pin8)
            self.pinButton8 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("133", country))
            self.pinButton8.config(image=self.displayPin8)
            self.pinButton8.place(x=310, y=280)

            # BARI
            self.pin9 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin9 = ImageTk.PhotoImage(self.pin9)
            self.pinButton9 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("795", country))
            self.pinButton9.config(image=self.displayPin9)
            self.pinButton9.place(x=80, y=300)

            # MILAN
            self.pin10 = Image.open("newDataFiles/Assets/pin(2).png")
            self.displayPin10 = ImageTk.PhotoImage(self.pin10)
            self.pinButton10 = ttk.Button(self._sideWindow, command=lambda: self.createCityWindow("122", country))
            self.pinButton10.config(image=self.displayPin10)
            self.pinButton10.place(x=310, y=400)


    def createCityWindow(self, cityCode, countryCode):
        self.cityWindow = cityWindow(cityCode,countryCode)


class cityWindow:

    def __init__(self,cityCode, countryCode):
        self.createList(cityCode, countryCode)

    def createList(self,cityCode, countryCode):
        self.sideWindow=tk.Toplevel()
        self.sideWindow.title("Attractions")

        codeList = ["42", "", countryCode]
        s.send(pickle.dumps(codeList))
        countryName = pickle.loads(s.recv(8192))

        codeList = ["53", "", cityCode]
        s.send(pickle.dumps(codeList))
        cityName = pickle.loads(s.recv(8192))

        self.placeLabel=tk.Label(self.sideWindow,text="Country: "+countryName+" - "+"City: "+cityName)
        self.placeLabel.pack()

        self.attractionsList=tk.Listbox(self.sideWindow, selectmode=tk.SINGLE, width = 40)

        codeList = ["48", "", cityCode]
        s.send(pickle.dumps(codeList))
        attractions = pickle.loads(s.recv(8192))

        for i in attractions:
            self.attractionsList.insert(tk.END,i)

        self.attractionsList.pack(pady=20)








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
        global userID
        userID=self.userID.get()

        codeList = ["00", "", userID]
        s.send(pickle.dumps(codeList))
        userValidated = pickle.loads(s.recv(8192))

        if userValidated != "1":
            if userValidated:

                codeList = ["01", "", userID]
                s.send(pickle.dumps(codeList))
                userStatus = pickle.loads(s.recv(8192))

                if userStatus == "0":
                    # AQUI DEJA CARGAR NUEVA VENTANA
                    # Set userName here:
                    codeList = ["02", "", userID]
                    s.send(pickle.dumps(codeList))
                    userName = pickle.loads(s.recv(8192))
                    for child in self.winfo_children():
                        child.place_forget()
                    self.chooseRecervation()
                    print("Success")



                else:

                    messagebox.showinfo("Access denied", "User with migration issues")

                    loginError = False
                    blocked = True
            else:

                messagebox.showinfo("Access denied", "Wrong User Name or password")

        else:
            messagebox.showinfo("Access denied", "Server is blocked")


        self.userID.delete(0, tk.END)

    def chooseRecervation(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()


        self.fixedRouteRecervation=ttk.Button(self, text="Fixed route recervation", command=self.drawFixedRecervation)
        self.fixedRouteRecervation.pack(pady=40)

        self.customRecervation = ttk.Button(self, text="Custom route recervation", command=self.drawCustomRecervation)
        self.customRecervation.pack(pady=40)

        self.viewBill=ttk.Button(self, text="View bill", command=self.drawBilling)
        self.viewBill.pack(pady=40)

    def drawFixedRecervation(self):
        codeList = ["03", ""]
        s.send(pickle.dumps(codeList))
        country = pickle.loads(s.recv(8192))

        if country != "1":

            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()
            self.searchKey = []

            self.departureCountryList = ttk.Combobox(self, state="readonly")

            self.departureCountryList["values"] = country
            self.departureCountryList.bind("<<ComboboxSelected>>", self.updateCitiesOnSelectionFixed)
            self.departureCountryList.place(x=250, y=50)
            self.departureCountryListLabel=ttk.Label(self, text="Countries")
            self.departureCountryListLabel.place(x=100, y=50)

            self.departureCityList = ttk.Combobox(self, state="readonly")
            self.departureCityList.bind("<<ComboboxSelected>>", self.selectCityFixed)
            self.departureCityList.place(x=250, y=100)
            self.departureCityListLabel=ttk.Label(self, text="Cities")
            self.departureCityListLabel.place(x=100, y = 100)


            self.routeRecervation=ttk.Button(self, text="Continue", command=self.routeListsFixed)
            self.routeRecervation.place(x=300, y =200)

            self.backButton=ttk.Button(self, text="Back", command= self.backToLogIn)
            self.backButton.place(x=80,y=200)
        else:
            messagebox.showinfo("Access denied", "Server is blocked")

    def drawCustomRecervation(self):
        self.pinCount = 0

        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.byPriceVar=tk.IntVar()
        self.byTimeVar=tk.IntVar()
        self.byPrice=ttk.Checkbutton(self, text="Route by price", variable=self.byPriceVar,onvalue=1, offvalue=0, command=self.getCheckBox)
        self.byPrice.place(x=70,y=420)
        self.byTime=ttk.Checkbutton(self, text="Route by Time", variable=self.byTimeVar,onvalue=1, offvalue=0, command=self.getCheckBox)
        self.byTime.place(x=290,y=420)

        self.cities1=ttk.Combobox(self, state="readonly")

        """
        self.cities1["values"]= #la lista que le de la gana
        """

        self.cities1.place(x=70,y=460)

        self.cities2 = ttk.Combobox(self, state="readonly")

        """
        self.cities1["values"]= #la lista que le de la gana
        """

        self.cities2.place(x=290, y=460)

        self.img = Image.open("newDataFiles/Assets/europe_map(3).png")
        self.display = ImageTk.PhotoImage(self.img)
        self.map = tk.Label(self, image=self.display, bd=5, relief="ridge")
        self.map.pack()

        # Spain
        self.pin = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin = ImageTk.PhotoImage(self.pin)
        self.pinButton = ttk.Button(self, command=lambda: self.openSelectCity("90", 90, 330))
        self.pinButton.config(image=self.displayPin)
        self.pinButton.place(x=90, y=330)

        # Portugal
        self.pin2 = Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin2 = ImageTk.PhotoImage(self.pin2)
        self.pinButton2 = ttk.Button(self, command=lambda: self.openSelectCity("23", 50, 330))
        self.pinButton2.config(image=self.displayPin2)
        self.pinButton2.place(x=50, y=330)

        # France
        self.pin3 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin3 = ImageTk.PhotoImage(self.pin3)
        self.pinButton3 = ttk.Button(self, command=lambda: self.openSelectCity("78", 150, 270))
        self.pinButton3.config(image=self.displayPin3)
        self.pinButton3.place(x=150, y=270)

        # Switzerland
        self.pin4 = Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin4 = ImageTk.PhotoImage(self.pin4)
        self.pinButton4 = ttk.Button(self, command=lambda: self.openSelectCity("234", 190, 270))
        self.pinButton4.config(image=self.displayPin4)
        self.pinButton4.place(x=190, y=270)

        # UK
        self.pin6 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin6 = ImageTk.PhotoImage(self.pin6)
        self.pinButton6 = ttk.Button(self, command=lambda: self.openSelectCity("123", 120, 210))
        self.pinButton6.config(image=self.displayPin6)
        self.pinButton6.place(x=120, y=210)

        # Netherlands
        self.pin7 = Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin7 = ImageTk.PhotoImage(self.pin7)
        self.pinButton7 = ttk.Button(self, command=lambda: self.openSelectCity("134", 175, 210))
        self.pinButton7.config(image=self.displayPin7)
        self.pinButton7.place(x=175, y=210)

        # Turkey
        self.pin8 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin8 = ImageTk.PhotoImage(self.pin8)
        self.pinButton8 = ttk.Button(self, command=lambda: self.openSelectCity("24", 380, 330))
        self.pinButton8.config(image=self.displayPin8)
        self.pinButton8.place(x=380, y=330)

        # Belgium
        self.pin10 = Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin10 = ImageTk.PhotoImage(self.pin10)
        self.pinButton10 = ttk.Button(self, command=lambda: self.openSelectCity("32", 165, 230))
        self.pinButton10.config(image=self.displayPin10)
        self.pinButton10.place(x=165, y=230)

        # ITALY
        self.pin21 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin21 = ImageTk.PhotoImage(self.pin21)
        self.pinButton21 = ttk.Button(self, command=lambda: self.openSelectCity("05", 220, 320))
        self.pinButton21.config(image=self.displayPin21)
        self.pinButton21.place(x=220, y=320)

        # Greece
        self.pin12 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin12 = ImageTk.PhotoImage(self.pin12)
        self.pinButton12 = ttk.Button(self, command=lambda: self.openSelectCity("02", 315, 353))
        self.pinButton12.config(image=self.displayPin12)
        self.pinButton12.place(x=315, y=353)

        # Czech republic
        self.pin13 = Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin13 = ImageTk.PhotoImage(self.pin13)
        self.pinButton13 = ttk.Button(self, command=lambda: self.openSelectCity("456", 235, 240))
        self.pinButton13.config(image=self.displayPin13)
        self.pinButton13.place(x=235, y=240)

        # Poland
        self.pin14 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin14 = ImageTk.PhotoImage(self.pin14)
        self.pinButton14 = ttk.Button(self, command=lambda: self.openSelectCity("120", 260, 205))
        self.pinButton14.config(image=self.displayPin14)
        self.pinButton14.place(x=260, y=205)

        # Romain
        self.pin15 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin15 = ImageTk.PhotoImage(self.pin15)
        self.pinButton15 = ttk.Button(self, command=lambda: self.openSelectCity("149", 315, 270))
        self.pinButton15.config(image=self.displayPin15)
        self.pinButton15.place(x=315, y=270)

        # Ukraine
        self.pin16 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin16 = ImageTk.PhotoImage(self.pin16)
        self.pinButton16 = ttk.Button(self, command=lambda: self.openSelectCity("256", 350, 220))
        self.pinButton16.config(image=self.displayPin16)
        self.pinButton16.place(x=350, y=220)

        # Bulgaria
        self.pin17 = Image.open("newDataFiles/Assets/rsz_pin2.png")
        self.displayPin17 = ImageTk.PhotoImage(self.pin17)
        self.pinButton17 = ttk.Button(self, command=lambda: self.openSelectCity("280", 330, 310))
        self.pinButton17.config(image=self.displayPin17)
        self.pinButton17.place(x=330, y=310)

        # Finland
        self.pin18 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin18 = ImageTk.PhotoImage(self.pin18)
        self.pinButton18 = ttk.Button(self, command=lambda: self.openSelectCity("18", 280, 90))
        self.pinButton18.config(image=self.displayPin18)
        self.pinButton18.place(x=280, y=90)

        # Sweden
        self.pin19 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin19 = ImageTk.PhotoImage(self.pin19)
        self.pinButton19 = ttk.Button(self, command=lambda: self.openSelectCity("180", 230, 90))
        self.pinButton19.config(image=self.displayPin19)
        self.pinButton19.place(x=230, y=90)

        # Germany
        self.pin20 = Image.open("newDataFiles/Assets/pin(2).png")
        self.displayPin20 = ImageTk.PhotoImage(self.pin20)
        self.pinButton20 = ttk.Button(self, command=lambda: self.openSelectCity("499", 200, 220))
        self.pinButton20.config(image=self.displayPin20)
        self.pinButton20.place(x=200, y=220)

        self.SeatLabel = ttk.Label(self,text="Seats")
        self.SeatLabel.place(x=50, y=545)

        self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.amountOfSeats = ttk.Entry(self, validate='key', validatecommand=self.vcmd)
        self.amountOfSeats.place(x=70, y=500)

        backButton=ttk.Button(self, text="Back", command= lambda : self.chooseRecervation())
        backButton.place(x=290,y=500)
        self.sendCustomRoutesButton = ttk.Button(self, text = "Find Routes", command= lambda: self.sendCustomToServer())
        self.sendCustomRoutesButton.place(x=380, y=500)


    def sendCustomToServer(self):

        global reservations

        print(self.byPriceVar.get())
        print(self.byTimeVar.get())
        print(self.departCountry)
        print(self.departCity[0])
        print(self.arriveCountry)
        print(self.arriveCity[0])
        print(self.amountOfSeats.get())

        if self.byTimeVar.get():
            timeFlag = True
        else:
            timeFlag = False

        codeList = ["41", "", self.departCountry, self.departCity[0], self.arriveCountry, self.arriveCity[0], timeFlag]
        s.send(pickle.dumps(codeList))
        possibleLists = pickle.loads(s.recv(8192))
        print(possibleLists)
        if possibleLists != "1" and possibleLists!=[]:
            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()


            self.showRoutes=tk.Listbox(self, width=50)
            for i in possibleLists[:len(possibleLists)-1]:#Que no entre el precio aqui
                self.showRoutes.insert(tk.END,i)

            self.showRoutes.pack(pady=10)

            self.priceTag=ttk.Label(self, text="The price is: "+"META AQUI EL PRECIO")
            self.priceTag.pack(pady=20)

            acceptReservation=ttk.Button(self, text="Accept", command= self.getCustomRoute)
            acceptReservation.pack(pady=10)

            cancelReservation = ttk.Button(self, text="Cancel", command= self.drawCustomRecervation)
            cancelReservation.pack(pady=10)




        else:
            if possibleLists=="1":
                messagebox.showinfo("Access denied","Server is blocked")
            elif possibleLists==[]:
                messagebox.showinfo("","There is no posible routes")

    def getCustomRoute(self):
        global reservations
        print(self.showRoutes.get(self.showRoutes.curselection()))

        reservations += [self.showRoutes.get(self.showRoutes.curselection())]
        self.chooseRecervation()
        messagebox.showinfo("", "Reservation added")


    def getCheckBox(self):
        if self.byPriceVar.get()==1:
            self.byTime.config(state="disabled")
        elif self.byPriceVar.get()==0:
            self.byTime.config(state="normal")
        if self.byTimeVar.get()==1:
            self.byPrice.config(state="disabled")
        elif self.byTimeVar.get()==0:
            self.byPrice.config(state="normal")

    def openSelectCity(self, countryCode, x, y):
        if self.pinCount == 0:
            self.pinM = Image.open("newDataFiles/Assets/resized/redPin.png")
            self.displayPinM = ImageTk.PhotoImage(self.pinM)
            self.pinButtonM = ttk.Button(self, command=lambda: self.deletePinM())
            self.pinButtonM.config(image=self.displayPinM)
            self.pinButtonM.place(x=x, y=y)
            self.pinCount+=1
            self.departCountry = countryCode

            codeList = ["04", "", countryCode]
            s.send(pickle.dumps(codeList))
            self.cities1["values"] = pickle.loads(s.recv(8192))
            self.cities1.bind("<<ComboboxSelected>>", self.setDepartCity)
        elif self.pinCount == 1:
            self.pinN = Image.open("newDataFiles/Assets/resized/redPin.png")
            self.displayPinN = ImageTk.PhotoImage(self.pinM)
            self.pinButtonN = ttk.Button(self, command=lambda: self.deletePinN())
            self.pinButtonN.config(image=self.displayPinN)
            self.pinButtonN.place(x=x, y=y)
            self.pinCount += 1
            self.arriveCountry = countryCode

            codeList = ["04", "", countryCode]
            s.send(pickle.dumps(codeList))
            self.cities2["values"] = pickle.loads(s.recv(8192))
            self.cities2.bind("<<ComboboxSelected>>", self.setArriveCity)

    def setArriveCity(self,event):
        self.arriveCity = [self.cities2.get().split(" ")[0]]


    def setDepartCity(self,event):
        self.departCity = [self.cities1.get().split(" ")[0]]

    def deletePinM(self):
        self.pinButtonM.place_forget()
        self.pinCount -=1
        self.cities1.set('')
        self.cities1["values"] = []

    def deletePinN(self):
        self.pinButtonN.place_forget()
        self.pinCount -=1
        self.cities2.set('')
        self.cities2["values"] = []

    def drawBilling(self):
        global reservations
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()

        self.billList=tk.Listbox(self, width=60)
        for i in reservations:
            self.billList.insert(tk.END,i)

        self.billList.pack()

        #TODO
        #HACER BOTON
        #Agarrar UserId
        self.acceptReservation=ttk.Button(self, text="Accept", command=self.acceptReservations)
        self.acceptReservation.pack()

        self.eraseReservation=ttk.Button(self, text="Errase reservations", command=self.eraseReservations)
        self.eraseReservation.pack()
        self.backButton=ttk.Button(self,text="Back", command=self.chooseRecervation)
        self.backButton.pack(side=tk.BOTTOM)
    def acceptReservations(self):
        print("meta aqui la ostia")
        global reservations
        global userID
        codeList = ["11", "", reservations, userID]
        s.send(pickle.dumps(codeList))
        confirmation = pickle.loads(s.recv(8192))
        if confirmation:
            reservations = []
            self.chooseRecervation()
            messagebox.showinfo("","Done")
    def eraseReservations(self):
        global reservations
        global userID
        reservations=[]
        self.chooseRecervation()
        messagebox.showinfo("","All reservations have been removed")
        print(reservations)
        print(userID)

    def updateCitiesOnSelectionFixed(self, event):


        self.searchKey=[self.departureCountryList.get().split(" ")[0]]


        print(self.searchKey[0])
        codeList = ["04", "", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities= pickle.loads(s.recv(8192))
        if cities!="1":
            self.departureCityList["values"] = cities
            print(self.searchKey)
        else:
            messagebox.showinfo("Access denied", "Server is blocked")
    def selectCityFixed(self, event):

        if len(self.searchKey)==1:
             self.searchKey+=[self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1]=self.departureCityList.get().split(" ")[0]
        print(self.searchKey)
    def updateCitiesOnSelectionCustom1(self, event):


        self.searchKey=[self.departureCountryList.get().split(" ")[0]]

        print(self.searchKey[0])
        codeList = ["04", "", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        if cities!="1":
            self.departureCityList["values"] = cities
            print(self.searchKey)
        else:
            messagebox.showinfo("Access denied", "Server is blocked")
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
        codeList = ["04", "", self.searchKey[2]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))
        if cities!="1":
            self.arrivalCityList["values"] = cities
            print(self.searchKey)
        else:
            messagebox.showinfo("Access denied", "Server is blocked")
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

    def routeListsFixed(self):
        #Fixed
        codeList = ["10", "", self.searchKey[0], self.searchKey[1]]
        s.send(pickle.dumps(codeList))
        tempList = pickle.loads(s.recv(8192))


        if self.searchKey==[]:
            messagebox.showinfo("","Please select a contry and a city")
            print("HERE2")
        elif tempList =="1":
            messagebox.showinfo("Access denied", "Server is blocked")
            print("HERE3")
        elif len(self.searchKey)==2:
            for child in self.winfo_children():
                child.place_forget()

            self.routesListBox = tk.Listbox(self, width=69, height=20, selectmode=tk.SINGLE)


            for i in tempList:
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

    def routeListsCustom(self):

        codeList = ["41", "", self.searchKey[0], self.searchKey[1], self.searchKey[2], self.searchKey[3]]
        s.send(pickle.dumps(codeList))
        routes = pickle.loads(s.recv(8192))

        if self.searchKey == []:
            messagebox.showinfo("", "Please select a contry and a city")
            print("HERE2")
        elif routes == "1":
            messagebox.showinfo("Access denied", "Server is blocked")
            print("HERE3")
        elif  len(self.searchKey) == 4:
            print("HERE4")
            for child in self.winfo_children():
                child.place_forget()

            self.routesListBox = tk.Listbox(self, width=69, height=20, selectmode=tk.SINGLE)



            for i in routes:
                self.routesListBox.insert(tk.END, i)

            self.routesListBox.bind("<<ListboxSelect>>", self.getListBox)
            self.routesListBox.place(x=19, y=20)

            self.backButton = ttk.Button(self, text="Back", command=self.backToCountCitSelect)
            self.backButton.place(x=90, y=380)

            self.billingButton = ttk.Button(self, text="Continue", command=self.continueToBilling)
            self.billingButton.place(x=290, y=380)

            self.vcmd = (self.register(self.validate), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            self.amountOfSeats = ttk.Entry(self, validate='key', validatecommand=self.vcmd)
            self.amountOfSeats.place(x=165, y=350)

    def getListBox(self, event):
        if len(self.searchKey)==2 or len(self.searchKey)==4:
            self.searchKey+=[list(self.routesListBox.get(self.routesListBox.curselection()))]

        if len(self.searchKey)==2:
            self.searchKey[2]=list(self.routesListBox.get(self.routesListBox.curselection()))
        elif len(self.searchKey)==4:
            self.searchKey[4] = list(self.routesListBox.get(self.routesListBox.curselection()))

        print(self.searchKey)

    def continueToBilling(self):
        global reservations
        seatsToBuy=self.amountOfSeats.get()
        canRecerve=False
        print(seatsToBuy)
        print(self.searchKey[2][7])
        try:
            if int(seatsToBuy) > int(self.searchKey[2][7]) or seatsToBuy=="0":
                messagebox.showinfo("","Invalid amount of seats")
                canRecerve=False
        except:
            messagebox.showinfo("","Invalid amount of seats")
            seatsToBuy=0
            canRecerve=False
        if len(self.searchKey)==2:
            messagebox.showinfo("","Please select a route")
            canRecerve=False
        elif int(seatsToBuy) > 0 and int(seatsToBuy) < int(self.searchKey[2][7]) :
            canRecerve=True
        if canRecerve:
            self.searchKey[2]+=[int(seatsToBuy)]
            self.searchKey[2]+=[int(seatsToBuy)*int(self.searchKey[2][8])]
            reservations.append(self.searchKey[2])
            print(reservations)
            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()
            self.chooseRecervation()
            messagebox.showinfo("", "Recervation added")

    def backToCountCitSelect(self):
        for child in self.winfo_children():
            child.place_forget()
        if len(self.searchKey)==3 or len(self.searchKey)==2:
            self.drawFixedRecervation()
        elif len(self.searchKey)==5 or len(self.searchKey)==4:
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
        codeList = ["03", ""]
        s.send(pickle.dumps(codeList))
        countryListServer = pickle.loads(s.recv(8192))
        if countryListServer!="1":

            for child in self.winfo_children():
                child.pack_forget()

            self.countryLabel=ttk.Label(self,text="Countries")
            self.countryLabel.pack(pady=10)

            self.countryList=tk.Listbox(self, width=50)

            for i in countryListServer:
                self.countryList.insert(tk.END,i)

            self.countryList.pack()

            self.back=ttk.Button(self, text="back", command= self.init)
            self.back.pack()
        else:
            messagebox.showinfo("Access denied", "Server is blocked")

    def cities1(self):
        codeList = ["03", ""]
        s.send(pickle.dumps(codeList))
        countriesServerList = pickle.loads(s.recv(8192))

        if countriesServerList!="1":
            for child in self.winfo_children():
                child.pack_forget()

            self.searchKey=[]

            label=ttk.Label(self,text="Select a country")
            label.pack(pady=10)

            self.selectCountry=ttk.Combobox(self)

            self.selectCountry["values"] = countriesServerList
            self.selectCountry.bind("<<ComboboxSelected>>", self.cities1_get)
            self.selectCountry.pack()


            self.continueToCities=ttk.Button(self, text="Continue", command=self.cities2)
            self.continueToCities.pack(pady=10)

            self.back = ttk.Button(self, text="back", command=self.init)
            self.back.pack()
        else:
            messagebox.showinfo("Access denied","Server is blocked")
    def cities1_get(self, event):
        self.searchKey=[self.selectCountry.get().split(" ")[0]]
        print(self.searchKey)
    def cities2(self):
        codeList = ["04", "", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cityListServer = pickle.loads(s.recv(8192))
        
        if cityListServer!="1":
            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            label=ttk.Label(self, text="Cities")
            label.pack(pady=10)

            self.cityList = tk.Listbox(self, width=50)


            for i in cityListServer:
                self.cityList.insert(tk.END,i)
                print(i)

            self.cityList.pack()

            self.back = ttk.Button(self, text="back", command=self.cities1)
            self.back.pack()
        else:
            messagebox.showinfo("Access denied", "Server is blocked")

    def conections1(self):
        for child in self.winfo_children():
            child.place_forget()
            child.pack_forget()

        self.searchKey=[]

        self.departureCountryList = ttk.Combobox(self, state="readonly")
        codeList = ["03", ""]
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
        codeList = ["04", "", self.searchKey[0]]
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

        label = ttk.Label(self, text="Conections")
        label.pack(pady=10)

        self.conectionsList = tk.Listbox(self, width=50)

        codeList = ["05", "", self.searchKey[0], self.searchKey[1]]
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

        label1 = ttk.Label(self, text="Select train type")
        label1.pack(pady=10)

        self.trainType=ttk.Combobox(self)
        self.trainType["values"]=['01','02','03','04']
        self.trainType.bind("<<ComboboxSelected>>", self.trains_get)
        self.trainType.pack()

        self.continueToTrains=ttk.Button(self, text="Continue", command=self.trains2)
        self.continueToTrains.pack(pady=10)


        self.back=ttk.Button(self, text="Back", command=self.init)
        self.back.pack()
    def trains_get(self, event):
        self.searchKey=self.trainType.get()
        print(self.searchKey)
    def trains2(self):
        codeList = ["06", "", self.searchKey]
        print(self.searchKey)
        s.send(pickle.dumps(codeList))
        trainListServer = pickle.loads(s.recv(8192))
        print(trainListServer)
        if trainListServer!="1":
            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            label = ttk.Label(self, text="Trains")
            label.pack(pady=10)

            self.trainList = tk.Listbox(self, width=50)

            for i in trainListServer:
                self.trainList.insert(tk.END, i[0:5])
                print(i)

            self.trainList.pack()

            self.back = ttk.Button(self, text="back", command=self.trains1)
            self.back.pack()
        else:
            messagebox.showinfo("Access denied","Server is blocked")

    def prices1(self):
        for child in self.winfo_children():
            child.pack_forget()
            child.place_forget()

        self.searchKey=[]

        label = ttk.Label(self, text="Enter train code")
        label.pack(pady=10)

        self.trainCode=ttk.Entry(self)
        self.trainCode.pack()


        self.continueToRoutes=ttk.Button(self, text="Continue", command = self.prices2)
        self.continueToRoutes.pack(pady=10)

        self.back=ttk.Button(self, text="Back", command=self.init)
        self.back.pack()
    def prices2(self):
        codeList = ["07", "", self.trainCode.get()]
        s.send(pickle.dumps(codeList))
        pricesServer = pickle.loads(s.recv(8192))
        if pricesServer==[]:
            messagebox.showinfo("","Incorrect train code")
        elif pricesServer=="1":
            messagebox.showinfo("Access denied", "Server is blocked")
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

        label = ttk.Label(self, text="Enter train code")
        label.pack(pady=10)

        self.trainCode = ttk.Entry(self)
        self.trainCode.pack()

        self.continueToRoutes = ttk.Button(self, text="Continue", command=self.seats2)
        self.continueToRoutes.pack(pady=10)

        self.back = ttk.Button(self, text="Back", command=self.init)
        self.back.pack()
    def seats2(self):
        codeList = ["08", "", self.trainCode.get()]
        s.send(pickle.dumps(codeList))
        seatsServer = pickle.loads(s.recv(8192))

        if seatsServer == []:
            messagebox.showinfo("", "Incorrect train code")
        elif seatsServer=="1":
            messagebox.showinfo("Access denied", "Server is blocked")
        else:
            self.searchKey = [self.trainCode.get()]
            print(self.searchKey)

            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            label = ttk.Label(self, text="Seats")
            label.pack(pady=10)

            self.seats = tk.Listbox(self, width=50)

            for i in seatsServer:
                self.seats.insert(tk.END, i)
                print(i)

            self.seats.pack()

            self.back = ttk.Button(self, text="back", command=self.prices1)
            self.back.pack()


    def routes1(self):
        codeList = ["03", ""]
        s.send(pickle.dumps(codeList))
        countries=pickle.loads(s.recv(8192))

        if countries!="1":

            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            self.searchKey=[]

            self.departureCountryList = ttk.Combobox(self, state="readonly")

            self.departureCountryList["values"] =countries
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
        else:
            messagebox.showinfo("Access denied", "Server is blocked")
    def routesUpdate(self, event):
        self.searchKey = [self.departureCountryList.get().split(" ")[0]]

        codeList = ["04", "", self.searchKey[0]]
        s.send(pickle.dumps(codeList))
        cities = pickle.loads(s.recv(8192))

        if cities!="1":


            print(self.searchKey[0])
            self.departureCityList["values"] = cities
            print(self.searchKey)

        else:
            messagebox.showinfo("Access denied", "Server is blocked")
    def routesAdd(self, event):

        if len(self.searchKey) == 1:
            self.searchKey += [self.departureCityList.get().split(" ")[0]]
        else:
            self.searchKey[1] = self.departureCityList.get().split(" ")[0]
        print(self.searchKey)
    def routes2(self):
        codeList = ["09", "", self.searchKey[1]]
        s.send(pickle.dumps(codeList))
        routesServer = pickle.loads(s.recv(8192))

        if self.searchKey==[]:
            messagebox.showinfo("","Please select a country and a city")
        elif routesServer=="1":
            messagebox.showinfo("Access denied", "Server is blocked")
        else:
            print(self.searchKey)
            for child in self.winfo_children():
                child.place_forget()
                child.pack_forget()

            label = ttk.Label(self, text="Routes")
            label.pack(pady=10)
            
            self.routeList = tk.Listbox(self, width=50)

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
        self.map=Map(self.notebook)
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

    # codeList = ["41", "", "78", "302", "02", "67", True]
    # # codeList = ["41", "", "02", "67", "24", "451", True]
    # s.send(pickle.dumps(codeList))
    # possibleLists = pickle.loads(s.recv(8192))
    # print(possibleLists)


    print(possibleLists)
    app.mainloop()