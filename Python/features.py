import os
import time
import wikipedia
import subprocess
import pyautogui as pg
import webbrowser as web
from googletrans import Translator

def _query():
    query = '''You can ask for
1. search for {something}
2.{something} wikipedia
3. play music
4. whatsapp
5. Goodnight or exit to stop program'''
    return query

def _translator(fromlang,tolang,MyText):
    translator = Translator()
    try:
        if MyText == '':
            return "Nothing to translate."
        if fromlang == 'none' or tolang == 'none':
            return translator.translate(MyText).text
        else:
            return translator.translate(MyText, src=fromlang, dest=tolang).text
    except:
        return "Unable to translate."

def _google(MyText):
    print("Searching...")
    MyText = MyText.replace("search for", "")
    #MyText = MyText.replace("in google", "")
    try:
        print(f"showing results for {MyText}...")
        web.open(f'https://www.google.com/search?q={MyText}')
    except Exception as e:
        print(e)
        print("Unable to show results.")

def _wiki(MyText):
    print("Searching...")
    MyText = MyText.replace("wikipedia", "")
    try:
        result = wikipedia.summary(MyText, sentences=1)
        return result
    except:
        print("Don't know that.")

def _spotify(MyText):
    print("Opening Spotify...")
    if 'play' in MyText:
        try:
            subprocess.Popen("%s"%r'C:\Users\91957\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe')
            print("Playing music...")
            time.sleep(5)
            pg.press('space')
        except:
            print("Seems like something went wrong or Spotify is not installed.")
    elif 'pause' in MyText:
        try:
            subprocess.Popen("%s"%r'C:\Users\91957\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe')
            time.sleep(5)
            pg.press('space')
            print("Paused.")
        except:
            print("Seems like something went wrong or Spotify is not installed.")

def _whatsapp(phonenum,msg):
    try:
        web.open('https://web.whatsapp.com/send?phone='+phonenum+'&text='+msg)
        time.sleep(10)
        pg.press('enter')
        print("message sent.")
        file = open("msglog.txt","a")
        file.write(f"{time.asctime( time.localtime(time.time()) )}\nPhone number: {phonenum}\nMessage: {msg}")
        file.write("\n--------------------\n")
        file.close()
    except Exception as e:
        print(f"Oops! something went wrong.({e})")
    
    
