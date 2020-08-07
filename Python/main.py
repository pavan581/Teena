#Builtin or downloaded packages
import os
import datetime
import random

#User defined packages
from data import _data
import files
import voice
import wishes
import features



if __name__ == "__main__":
    username = files._read("username")
    if username == None:
        voice._out(wishes._wishMe())
        while True:
            username = voice._in("Your name___")
            if username != 'none':
                files._write("username",username)
                break
    else:
        voice._out(wishes._wishMe(username))
        
    while True:
        try:
            count = 0
            call = voice._in("Call Teena(Tina) to respond.")
            if any(a in call for a in _data["name"]):
                voice._out(random.choice(_data["wishes"]))
                while True:
                    
                    print(".-- . .-.. -.-. --- -- .   -... .- -.-. -.-")
                    MyText = voice._in()
    
                    if any(a in MyText for a in ['help','what can you do','who are you','tell me about yourself']):
                        voice._out(features._query())

                    elif any(a in MyText for a in ['what is the time now','time','can you tell me the time']):
                        voice._out(f"{int(datetime.datetime.now().hour)}:{int(datetime.datetime.now().minute)}")
            
                    elif 'how are you' in MyText:
                        voice._out(wishes._hru())
    
                    elif any(a in MyText for a in ["good night","exit","bye","close","shutdown yourself"]):
                        voice._out(wishes._close())
                        exit()

                    elif 'wikipedia' in MyText:
                        voice._out(features._wiki(MyText))

                    elif 'music' in MyText:
                        features._spotify(MyText)
    
                    elif any(a in MyText for a in ['search for','in google','google']):
                        features._google(MyText)
                    
                    elif any(a in MyText for a in ['translate','translate this']):
                        MyText = MyText.replace(a, "")
                        fromlang = voice._in("from..")
                        tolang = voice._in("to..")
                        voice._out(features._translator(fromlang,tolang,MyText))
    
                    elif any(a in MyText for a in ['send a message','send a message in whatsapp']):
                        while True:
                            phonetext = voice._in("to..")
                            if phonetext != 'none':
                                phonenum = files._read(phonetext)
                                if phonenum == None:
                                    print("Sorry! Can't get the number.")
                                    break
                                else:
                                    while True:
                                        msg = voice._in("say the message..")
                                        if msg != None and msg != 'none':
                                            features._whatsapp(phonenum,msg)
                                            break
                                break
                        
                    elif any(a in MyText for a in ['save this','new entry','take a note']):
                        voice._out("Enter with keyboard.")
                        files._write(input("Entry name___"),input("Entry value___"))
                        
                    else:
                        count += 1

                    if count >= 5:
                        print("Sleeping...")
                        break
        except Exception as e:
            print(e)
