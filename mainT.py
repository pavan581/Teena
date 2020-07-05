import os
import time
import datetime

import voice
import wishes
import features


contacts ={

    "me"            :"+919573486634",
    "hari"          :"+919885112557",
    "raja"          :"+918106061578",
    "akka"          :"+919493605566",
    "srinu"         :"+916304571505"
    
    }


if __name__ == "__main__":
    voice._out(wishes.wishMe())
    
    while True:
        MyText = voice._in().lower()

        if 'help' in MyText:
            voice._out(features.help())

        elif 'what\'s the time' == MyText:
            voice._out(f"{int(datetime.datetime.now().hour)}:{int(datetime.datetime.now().minute)}")
            
        elif 'how are you' in MyText:
            voice._out(wishes.hru())

        elif 'good night' in MyText:
            voice._out(wishes.gn())
            exit()

        elif 'wikipedia' in MyText:
            voice._out(features.wiki(MyText))

        elif 'music' in MyText:
            features.spotify(MyText)

        elif 'whatsapp' in MyText:
            print("to...")
            while True:
                phonetext = voice._in().lower()
                if phonetext != 'none':
                    phonenum = contacts.get(phonetext)
                    if phonenum == None:
                        print("Sorry! Can't get the number.")
                        break
                    print("Message: ")
                    while True:
                        msg = voice._in()
                        if msg != 'none':
                            features.whatsapp(phonenum,msg)
                            break
                break
                    
        elif 'search for' in MyText or 'in google' in MyText:
            features.google(MyText)
            
