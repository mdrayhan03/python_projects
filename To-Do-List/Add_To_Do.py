from tkinter import *
from tktimepicker import AnalogPicker, AnalogThemes
import datetime
import List_File

class Add :
    def __init__(self , window , fileName) :
        self.window = window 
        self.fileName = fileName
        self.main_frame = Frame(self.window , width=600 , height=400 , bg='#303030')
        self.first_frame()
        self.main()
        self.main_frame.pack()
    
    def first_frame(self) :
        self.first = Frame(self.main_frame , bg="#303030")
        Label(self.first , text="Add To-Do" , bg="#303030" , fg="hotpink" , font=("Arial" , 28)).pack(pady=20)
        self.first.pack(pady=(0 , 20))
    
    def main(self) :
        self.frame = Frame(self.main_frame , bg="#303030")

        Label(self.frame , text="To Do" , bg="#303030" , fg="hotpink" , font=("Arial" , 14)).grid(row=0 , column=0 , sticky=W)
        self.todoEntry = StringVar()
        self.entry = Entry(self.frame , bg="#303030" , fg="pink" , textvariable=self.todoEntry , font=("Arial" , 14) , width=30)
        self.entry.grid(row=0 , column=1)
        Label(self.frame , text="Start Time" , bg="#303030" , fg="hotpink" , font=("Arial" , 14)).grid(row=1 , column=0 , sticky=W)
        self.stLabel = Label(self.frame , bg="#303030" , fg="pink" , font=("Arial" , 14))
        self.stLabel.grid(row=1 , column=1 , sticky=W)
        self.starttime = ""
        Label(self.frame , text="End Time" , bg="#303030" , fg="hotpink" , font=("Arial" , 14)).grid(row=2 , column=0 , sticky=W)
        self.etLabel = Label(self.frame , bg="#303030" , fg="pink" , font=("Arial" , 14))
        self.etLabel.grid(row=2 , column=1 , sticky=W)
        self.endtime = ""

        self.setTime = Button(self.frame , text="Set Time" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.timerTop)
        self.setTime.grid(row=3 , column=0 , sticky='news')
        self.buttonBind(self.setTime)

        self.show = Button(self.frame , text="Show List" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.sceneSwitch)
        self.show.grid(row=3 , column=1 ,sticky='news')
        self.buttonBind(self.show)

        self.add = Button(self.frame , text="Add To Do List" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.writeTodo)
        self.add.grid(row=4 , column=0 , columnspan=2 , sticky='news')
        self.buttonBind(self.add)

        Label(self.frame , text="Total : " , bg="#303030" , fg="hotpink" , font=("Arial" , 14)).grid(row=5 , column=0 , sticky="e")
        self.total = Label(self.frame , text=self.read_file() , bg="#303030" , fg="hotpink" , font=("Arial" , 14))
        self.total.grid(row=5 , column=1 , sticky="w")
        
        self.frame.pack()

        for child in self.frame.winfo_children():
            child.grid_configure(padx=5 , pady=5)

    def timerTop(self) :
        self.timerTop = Toplevel(self.frame , bg='#303030')

        self.time_picker = AnalogPicker(self.timerTop)
        self.time_picker.pack(expand=True, fill="both")

        theme = AnalogThemes(self.time_picker)
        theme.setDracula()

        button = Button(self.timerTop , text="Start Time" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.starttimer)
        button.pack(side="left" , padx=10 , pady=10)
        self.buttonBind(button)

        button = Button(self.timerTop , text="End Time" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.endtimer)
        button.pack(side="right" , padx=10 , pady=10)
        self.buttonBind(button)

        button = Button(self.timerTop , text="Set" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.timerTop.destroy)
        button.pack(padx=10 , pady=10)
        self.buttonBind(button)
    
    def starttimer(self) :
        self.starttime = self.time_picker.time()
        self.stLabel.config(text=self.starttime)
    
    def endtimer(self) :
        self.endtime = self.time_picker.time()
        self.etLabel.config(text=self.endtime)

    
    def sceneSwitch(self) : 
        self.main_frame.destroy()
        List_File.List(self.window , self.fileName)
    
    def write_file(self , todo) :        
        file = open(self.fileName , "at")
        file.write(todo)
        file.close()

    def writeTodo(self) :
        if self.starttime == "" and self.endtime == "" :
            todo = f"{self.todoEntry.get()}\n"
        elif self.starttime == "" :
            todo = f"{self.todoEntry.get()}[ET:{self.endtime}]\n"
        elif self.endtime == "" :
            todo = f"{self.todoEntry.get()}[ST:{self.starttime}]\n"
        elif self.starttime != "" and self.endtime != "" :
            todo = f"{self.todoEntry.get()}[ST:{self.starttime}, ET:{self.endtime}]\n"

        self.write_file(todo)
        self.total.config(text=self.read_file())
        self.todoEntry.set("")
        self.stLabel.config(text="")
        self.etLabel.config(text="")

    def read_file(self) :
        cnt = 0        
        file = open(self.fileName , "rt")
        for line in file :
            cnt += 1  
        file.close()
        return cnt

    def buttonBind(self , button) :
        button.bind("<Enter>", func=lambda e: button.config(
        background="#303030" , foreground="hotpink"))

        button.bind("<Leave>", func=lambda e: button.config(
        background="hotpink" , foreground="#303030"))
    
    
