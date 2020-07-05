import os
import time
from gtts import gTTS
from mutagen.mp3 import MP3
import speech_recognition as sr

def _out(text):
    print(text)
    myobj = gTTS(text=text, lang='en', slow=False)

    myobj.save("Teena.mp3")
    os.system("Teena.mp3")
    
    #mp3 = int(MP3("Testing.mp3").info.length)
    #print(mp3)
    time.sleep(int(MP3("Teena.mp3").info.length))


def _in():

    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source, duration=0.2)
        
        print("say something...")
        audio = r.listen(source)                            
    try:
        voice = r.recognize_google(audio, language='en-in')  
        print(f"you said {voice}.")
    except:
        print("Can you say that again...")
        return 'None'
    return voice
