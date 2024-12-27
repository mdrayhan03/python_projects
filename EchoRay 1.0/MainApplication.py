"""
EchoRay: A personal voice assistant built with Python 3
Features:
- Utilizes text-to-speech and speech recognition libraries for interaction.
- Can listen, speak, and perform limited tasks.
- Designed to enhance productivity and provide hands-free assistance.

Libraries used:
- pyttsx3 for text-to-speech conversion
- speech_recognition for speech-to-text processing
- Additional useful libraries for task execution
"""

import pyttsx3, webbrowser, speech_recognition as sr # pyttsx3 for text to speech, speech_recognition for speech to text and webbrowser to open link in browser
from datetime import datetime # datetime library

class Assistant : # Assistant class
    def __init__(self) -> None: # initiate function
        self.name = "EchoRay"
        self.version = "1.0"
        print("Initializing...")
        self.engine = pyttsx3.init(self.get_driver()) # initializing text to speech engine
        self.voice = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voice[1].id) # setting female voice as start

        self.r = sr.Recognizer() # initializing speech to text engine

        self.initializer() # calling function

        while True : # infinity loop
            query = self.takeCommand() # calling function

            if "change voice" in query or "change your voice" in query : # for voice change
                self.speak("Which voice do you want? male or female.")
                query = self.takeCommand()
                if "female" in query :
                    self.change_voiceID(1)
                elif "male" in query :
                    self.change_voiceID(0)
            
            elif "change your name" in query : # for name change
                self.speak("Which name do you want?")
                query = self.takeCommand()
                self.name = query
                if self.name != None :
                    self.speak("My name changed successfully")
                else :
                    self.speak("I did not hear please say again.")

            elif "your name" in query : # say name
                self.speak(f"My name is {self.name} {self.version}.")

            elif "search a song in youtube" in query : # search song in youtube
                self.speak("Which song you want to listen?")
                query = self.takeCommand()
                url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                webbrowser.open(url)

            elif "open youtube" in query : # open youtube in browser
                webbrowser.open("https://www.youtube.com/")            

            elif "open facebook" in query : # open facebook in browser
                webbrowser.open("https://www.facebook.com/rayhan.philosopher.03")

            elif "open instagram" in query : # open instagram in browser
                webbrowser.open("https://www.instagram.com/md_rayhan_philosopher/")
            
            elif "open github" in query : # open github in browser
                webbrowser.open("https://www.github.com/")

            elif "open linkedin" in query : # open linkedin in browser
                webbrowser.open("https://www.linkedin.com/in/md-rayhan-hossain-619a5b2a5/")

            elif "open messenger" in query : # open messenger in browser
                webbrowser.open("https://www.messenger.com/")
            
            elif "open whatsapp" in query : # open whatsapp in browser
                webbrowser.open("https://web.whatsapp.com/")
            
            elif "open mail" in query : # open mail in browser
                webbrowser.open("https://mail.google.com/")

            elif "about your owner" in query : # say about ownself
                self.speak("My owner’s name is Rayhan, and he lives in Dhaka, Bangladesh. He is currently studying Computer Science and Engineering at Independent University, Bangladesh. Rayhan is a skilled full-stack developer with a keen interest in Machine Learning and Artificial Intelligence. He created me to assist him in his daily tasks and help streamline his work and studies. I’m here to make his life easier and support him in achieving his goals!")
            
            elif "about you" in query : # say about owner
                self.speak(f"Hello! I am {self.name}, a personal assistant created to assist my owner. Currently running on version 1.0, I can listen, speak, and perform limited tasks. My creator is constantly working on upgrading me to expand my functionalities and make me smarter, faster, and more versatile. Stay tuned as I evolve to better serve. I am here to make a difference, one step at a time!")
            
            elif "time" in query : # say time
                time = datetime.now().strftime("%H:%M:%S %p")
                self.speak(f"Time is {time}")

            elif "date" in query : # say date
                date = datetime.now().strftime("%A, %B %d, %Y")
                self.speak(f"Date is {date}")

            elif "today" in query : # say today
                today = datetime.now().strftime("%A, %B %d, %Y %H:%M:%S %p")
                self.speak(f"Today is {today}")

            elif "exit" in query :  # exiting the program
                self.speak("Thank you. Have a nice day.")
                break
    
    # getting system and driver
    def get_driver(self) :
        if self.system == 'Windows':   # windows
            return 'sapi5'
        elif self.system == 'Darwin':  # macOS
            return 'nsss'
        else:  # Linux
            return 'espeak'
        
    # speaking the given text
    def speak(self, text) :
        print(f"{self.name} said: ", text)
        self.engine.say(text) # speak builtin function
        self.engine.runAndWait()

        return text
        
    # first apperance function
    def initializer(self) :
        self.speak(f"Hello sir, I'm {self.name} {self.version}. How can I help you?")

    # get human voice and turned into text
    def takeCommand(self):
        #It takes microphone input from the user and returns string output
        with sr.Microphone() as source:
            print("Listening...")
            self.r.pause_threshold = 1
            audio = self.r.listen(source)

            try:
                print("Recognizing...")    
                query = self.r.recognize_google(audio, language='en-in') #Using google for voice recognition.
                print(f"User said: {query}")  #User query will be printed.

            except Exception as e:
                print("Say that again please...")   #Say that again will be printed in case of improper voice
                return "None" #None string will be returned
            
            return query.lower()
        
    # change voice of assistant
    def change_voiceID(self, id) :
            self.engine.setProperty("voice", self.voice[id].id)
            self.speak("Voice changed successfully.")

# instantiate the 'Assistant' class
if __name__ == "__main__" :
    Assistant()