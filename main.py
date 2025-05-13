import speech_recognition as sr
import pyttsx3 as pt
import webbrowser
import os
import time

def intro():
     a = pt.init()
     a.say("Hello Sir, How can I help you")
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