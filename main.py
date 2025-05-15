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
     elif (s > 11 and s <= 17):
          # print("Good Afternoon Sir , How can I help you today")
          str = "Good Afternoon Sir , How can I help you today"
     elif(s > 17 and s < 22):
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


def recorsition():
     # Initialize recognizer
     recognizer = sr.Recognizer()
     command=""
     with sr.Microphone() as source:
          print("Listening....")
          while True:
               try:
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio).lower()
                    command.lower()
                    print(f"You said: {command}")
                    processing(command)
                    processing_1(command)
                    # str = recorsition()
                    # str = str.lower()
                    if (command.find("thank you") != -1):
                         speek("Most Welcome sir ,I am very happy to help you")
                         return
     
                    # print("Trigger detected! Launching assistant...")
                    # os.startfile("main.bat")  # Or use the full path if needed
                    # tm.sleep(10)  # Delay to avoid repeated triggers
               
               except sr.UnknownValueError:
                    pass  # Ignore unknown audio
               except sr.RequestError:
                    print("Check your internet connection.")
               except Exception as e:
                    print(f"Error: {e}")

def main():
     intro()
     recorsition()
     # speek(str)
     # print(str)
     

main()