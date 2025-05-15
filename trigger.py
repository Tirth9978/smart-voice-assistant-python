import speech_recognition as sr
import pyttsx3 as pt
import webbrowser
import os
import time as tm
from time import gmtime,strftime

def listen_for_trigger():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for trigger ....")
        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                if "hello mm" in command:
                    print("Trigger detected! Launching assistant...")
                    os.startfile("main.bat")  # Or use the full path if needed
                    return
               #      tm.sleep(10)  # Delay to avoid repeated triggers
            except sr.UnknownValueError:
                pass  # Ignore unknown audio
            except sr.RequestError:
                print("Check your internet connection.")
            except Exception as e:
                print(f"Error: {e}")

listen_for_trigger()
