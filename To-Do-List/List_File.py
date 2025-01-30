from tkinter import *
import datetime
from Add_To_Do import Add

class List :
    def __init__(self , window , fileName) :
        self.window = window
        self.fileName = fileName
        self.main_frame = Frame(self.window , width=600 , height=400 , bg='#303030')
        Label(self.main_frame , text="To Do List" , bg="#303030" , fg="hotpink" , font=("Arial" , 28)).pack(pady=(15,0))
        self.main()
        self.read_file()
        self.main_frame.pack()

    def main(self) :
        self.aFrame = Frame(self.main_frame , bg="#303030")                
        self.other = Frame(self.aFrame , bg="#303030")                
        date = datetime.date.today()
        Label(self.other , text=f'Date : {date}' , bg="#303030" , fg="hotpink" , font=("Arial" , 14)).pack(side="left")
        Label(self.other , text=f'{self.fileName[7:]} : File Name' , bg="#303030" , fg="hotpink" , font=("Arial" , 14)).pack(side="right")
        self.other.pack(fill="x")
        
        self.listFrame = Frame(self.aFrame , bg="#303030")                
        self.myListBoxTo_Do = Listbox(self.listFrame , borderwidth=0 , width=50 , justify='center' ,
                    background= "#303030",
                    foreground= "pink",
                    font=("Arial",14),)
        self.myListBoxTo_Do.pack(side="left")
        
        myScrollBar = Scrollbar(self.listFrame,orient="vertical",command=self.myListBoxTo_Do.yview)
        myScrollBar.pack(side ="right", fill = "y" )
        self.myListBoxTo_Do.configure(yscrollcommand=myScrollBar.set)
        self.listFrame.pack(pady=(0 , 10))
        
        self.todoButton = Button(self.aFrame , text="Add To Do" , bg="hotpink" , fg="#303030" , activebackground="#572649" , activeforeground="white" , font=("Arial" , 14) , command=self.sceneSwitch)
        self.todoButton.pack(fill="x")
        self.buttonBind(self.todoButton)
        self.aFrame.pack(pady=(20 , 0))
    
    def sceneSwitch(self) :
        self.main_frame.destroy()
        Add(self.window , self.fileName)

    def read_file(self) :        
        file = open(self.fileName , "rt")
        for line in file :
            self.myListBoxTo_Do.insert(END , line)  
        file.close()

    def buttonBind(self , button) :
        button.bind("<Enter>", func=lambda e: button.config(
        background="#303030" , foreground="hotpink"))

        button.bind("<Leave>", func=lambda e: button.config(
        background="hotpink" , foreground="#303030"))

    


    