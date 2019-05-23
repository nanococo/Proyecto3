import tkinter as tk
from PIL import Image,ImageTk

class MainApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        container= tk.Frame(self)
        container.pack()

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames={}

        for Frame in (StartPage,PageOne):

            frame=Frame(container,self)

            self.frames[Frame] = frame

            frame.grid(row=0,column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf():
    print("It works")
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.img = Image.open("newDataFiles/Assets/europe_map(2).png")
        self.display = ImageTk.PhotoImage(self.img)
        self.imgLabel = tk.Label(self,image=self.display,bd=5,relief="ridge")
        self.imgLabel.pack()

        self.reservar= tk.Button(self, text="Reservar", command=lambda: controller.show_frame(PageOne))
        self.reservar.pack()

class PageOne(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        self.label = tk.Label(self, text="Reservaciones")
        self.label.pack()

        self.options=[1,
                      2,
                      3,
                      4,
                      5]
        self.var= tk.IntVar(self)
        self.var.set([])
        self.countryOption=tk.OptionMenu(self,self.var, *self.options)
        self.countryOption.pack()


        self.get = tk.Button(self, text="test", command=lambda: print("value is"+str(self.var.get())))
        self.get.pack(side=tk.LEFT)

        self.back = tk.Button(self, text="Atrás", command=lambda: controller.show_frame(StartPage))
        self.back.pack(side=tk.LEFT)

app=MainApp()
app.title("test")
app.geometry("500x600")

app.mainloop()
