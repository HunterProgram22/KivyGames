import kivy
import win32com.client as win

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang.builder import Builder


from os import listdir

PATH = './kv/'
for kv in listdir(PATH):
    Builder.load_file(PATH + kv)

class HomeScreen(GridLayout):

    def hello_Hunter(self):
        speaker = win.Dispatch("SAPI.SpVoice")
        speaker.Speak("Hello Hunter, would you like to play a game?")
        clear_widgets()

    def hello_Tyler(self):
        speaker = win.Dispatch("SAPI.SpVoice")
        speaker.Speak("Hello Tyler, would you like to play a game?")
        clear_widgets()

    speaker = win.Dispatch("SAPI.SPvoice")
    speaker.Speak("Hello, is this Hunter or Tyler? Please press you name.")


# class HunterScreen(GridLayout):
#
#     def paper_rock_scissors(self):
#         pass
#
#     speaker = win.Dispatch("SAPI.SPvoice")
#     speaker.Speak("Would you like to play Paper Rock Scissors," +\
#         " or Guess a Number, or Tic Tac Toe.")

class MyApp(App):
    title = 'Paper Rock Scissors'
    
    def build(self):
        return HomeScreen()




if __name__ == '__main__':
    MyApp().run()
