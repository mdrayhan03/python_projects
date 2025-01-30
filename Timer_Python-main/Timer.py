'''
This is a timer. We can fix time here and get notification after that time.
'''

'''importing time library to get local time and counting time in second'''
import time
'''
Colour class
class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)


ansi_cyan = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(36) #cyan
ansi_blue = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(34) #blue
ansi_purple = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(35) #purple
ansi_green = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(32) #green
ansi_red = ANSI.background(0) + ANSI.color_text(49) + ANSI.style_text(91) #red
'''

'''Code start from here'''
cnt = 1
while cnt == 1 :
  '''Here we create a dictoinary which have some data that can be choosen by user.'''
  initial = {
      "Cancel" : "00:00:00" ,
      "Brush" : "00:02:00" ,
      "Breakfast" :  "00:15:00" ,
      "Test" : "00:00:03"
  }

  print("Choice    Task      Time(Sec)")
  for i in range(len(initial)) :
    print(i , (" " * 8) ,end = "")
    print(list(initial)[i] , (" " * (9 -len(list(initial)[i]))) , end = "")
    print(list(initial.values())[i] )

  '''Take input that user choice what we have or make a new choice.'''
  initial_input = int(input("Select choice(0/1...) : "))

  if initial_input == 0 :
    '''That's user making a new choice with message and set time.'''
    message = input("Enter your message : ")
    hr , min , sec = map(int , input("Enter time(hr:min:sec) : ").split(":"))
    time_ = (hr * 3600) + (min * 60) + sec

  else :
    '''That's user making choice from our selective choice.'''
    message = list(initial)[initial_input]
    hr , min , sec = map(int , list(initial.values())[initial_input].split(":"))
    time_ = (hr * 3600) + (min * 60) + sec

  '''Showing user time count and after time count show message.'''
  for i in range(time_ , 0 , -1) :
    sec = i % 60
    min = int(i / 60) % 60
    hr = int(i / 3600)
    print(f"\r{hr:02}:{min:02}:{sec:02}" , end = "")
    time.sleep(1)
  print(f"\rTimes up! {message}" , end = "")
  time.sleep(1)
  print()
  cnt = int(input("Enter choice (1.Continue  2.Exit) : "))
print("Thank you!")
time.sleep(2)