import speech_recognition as sr
import pyttsx3 as pt
import webbrowser
import os
import time as tm
from time import gmtime,strftime

def intro():
     s =int(strftime("%H"))
     str = ""
     if (s >= 6 and s < 12):
          # print("Good Morning Sir , How can I help you today")
          str = "Good Morning Sir , How can I help you today"
     elif (s > 11 and s <= 5):
          # print("Good Afternoon Sir , How can I help you today")
          str = "Good Afternoon Sir , How can I help you today"
     elif(s > 5 and s < 10):
          # print("Good Evening Sir , How can I help you today")
          str = "Good Evening Sir , How can I help you today"
     else :
          str = "Good Night Sir , How can I help you at last"
     a = pt.init()
     a.say(str)
     a.runAndWait() 

def speek(str):
     a = pt.init()
     a.say(str)
     a.runAndWait()
     return 

def recorsition():
     # Initialize recognizer
     r = sr.Recognizer()
     text = ""
     # Use microphone as source
     with sr.Microphone() as source:
     
          audio = r.listen(source)

          try:
               # Convert speech to text
               text = r.recognize_google(audio)
               # print("You said:", text)

               # Store in variable
               spoken_text = text

          except sr.UnknownValueError:
               print("Sorry, I couldn't understand.")
          except sr.RequestError as e:
               print("Request failed; check internet connection.")
     return text.lower()

def processing(str):
     with open("links.txt","r") as file:
          for line in file:
               line = line.strip()
               if (str.find(line[:line.find(":")]) != -1):
                    speek(line[line.find(",")+1:])
                    webbrowser.open(line[line.find(":")+1:line.find(",")])

def processing_1(str):
     with open("Local Folders.txt","r") as file:
          for line in file:
               line = line.strip()
               if (str.find(line[:line.find(":")]) != -1):
                    speek(line[line.find(";")+1:])
                    os.startfile(line[line.find(":")+1:line.find(";")])

def main():
     intro()
     str = recorsition()
     # speek(str)
     # print(str)
     processing(str)
     processing_1(str)
     
main()