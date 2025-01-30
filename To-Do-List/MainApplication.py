from tkinter import *
import datetime
import os
import List_File 
import Add_To_Do 

class MainApplication :
    def __init__(self) :
        self.window = Tk()
        self.window.geometry("600x400+200+100")
        self.window.resizable(False , False)
        self.window.title("To-Do List")
        self.window.configure(bg="#303030")     
        self.window.iconbitmap("icon.ico")   
        # self.icon =PhotoImage(file="icon.png")
        # self.window.iconphoto(False, self.icon)
        self.create_newFile()
        List_File.List(self.window , self.fileName)
        self.window.mainloop()

    def create_newFile(self) :
        self.fileName = "./File/" + str(datetime.date.today()) + ".txt"
        if not os.path.exists(self.fileName) :
            file = open(self.fileName , "wt")
            file.close()

MainApplication()