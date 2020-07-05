import os
import time
import wikipedia
import subprocess
import webbrowser as web
import pyautogui as pg

def help():
    _help = '''You can ask for
1. search for {something}
2.{something} wikipedia
3. play music
4. whatsapp'''
    return _help

def google(MyText):
    print("Searching...")
    MyText = MyText.replace("search for", "")
    #MyText = MyText.replace("in google", "")
    try:
        print(f"showing results for {MyText}...")
        web.open(f'https://www.google.com/search?q={MyText}')
    except:
        print("Unable to show results.")

def wiki(MyText):
    print("Searching...")
    MyText = MyText.replace("wikipedia", "")
    try:
        result = wikipedia.summary(MyText, sentences=1)
        return result
    except:
        print("Don't know that.")

def spotify(MyText):
    print("Opening Spotify...")
    if 'play' in MyText:
        subprocess.Popen("%s"%r'C:\Users\91957\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe')
        print("Playing music...")
        time.sleep(5)
        pg.press('space')
    elif 'pause' in MyText:
        subprocess.Popen("%s"%r'C:\Users\91957\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\\Spotify.exe')
        time.sleep(5)
        pg.press('space')
        print("Paused.")

def whatsapp(phonenum,msg):
    web.open('https://web.whatsapp.com/send?phone='+phonenum+'&text='+msg)
    time.sleep(10)
    pg.press('enter')
    print("message sent.")
    file = open("msglog.txt","a")
    file.write(f"{time.asctime( time.localtime(time.time()) )}\nPhone number: {phonenum}\nMessage: {msg}")
    file.write("\n--------------------\n")
    file.close()
    
    
