import os
import datetime

import data
import voice
import wishes
import features



if __name__ == "__main__":
    try:
        username = data._read("username")
        voice._out(wishes._wishMe(username))
        
    except:
        data.__init__()
        while True:
            voice._out(wishes.wishMe())
            username = voice._in("Your name___")
            if username != 'none':
                data._write("username",username)
                break
    
    while True:
        print(".-- . .-.. -.-. --- -- .   -... .- -.-. -.-")
        MyText = voice._in()

        if 'help' in MyText:
            voice._out(features.help())

        elif 'new entry' in MyText:
            voice._out("Enter with keyboard.")
            data._write(input("Entry name___"),input("Entry value___"))

        elif 'time' in MyText:
            voice._out(f"{int(datetime.datetime.now().hour)}:{int(datetime.datetime.now().minute)}")
            
        elif 'how are you' in MyText:
            voice._out(wishes._hru())

        elif 'good night' in MyText or 'exit' in MyText:
            voice._out(wishes._gn())
            exit()

        elif 'wikipedia' in MyText:
            voice._out(features._wiki(MyText))

        elif 'music' in MyText:
            features._spotify(MyText)

        elif 'search for' in MyText or 'in google' in MyText:
            features._google(MyText)
                
        elif 'translate' in MyText:
            MyText = MyText.replace("translate","")
            fromlang = voice._in("from..")
            tolang = voice._in("to..")
            voice._out(features._translator(fromlang,tolang,MyText))

        elif 'whatsapp' in MyText:
            while True:
                phonetext = voice._in("to..")
                if phonetext != 'none':
                    phonenum = data._read(phonetext)
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
            
