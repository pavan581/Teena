import os
import time
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def _saveToFile(who,text):
    file = open("log.txt","a")
    file.write(f"{time.asctime( time.localtime(time.time()) )}\n{who}:{text}")
    file.write("\n----------------------------------------\n")
    file.close()

def _in(msg = "say something..."):

    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.2)
        
        print(msg)
        audio = r.listen(source)                            
    try:
        print('recognising...')
        voice = r.recognize_google(audio, language='en-in')
        print(f"you said {voice}.")
        
        _saveToFile("Teena",voice)

        return voice.lower()
    except:
        print("Can you say that again...")
        return 'none'

def _out(MyText):
    try:
        print(MyText)
        engine.say(MyText)
        engine.runAndWait()

        _saveToFile("you",MyText)
        
    except:
        print("Unable to speak or nothing to speak.")
