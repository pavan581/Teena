import datetime

def _wishMe(username = ''):
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        x = "Good Morning "

    elif hour>=12 and hour<17:
        x = "Good Afternoon "

    else:
        x = "Good Evening "
    return f'''{x}{username}!

I'm Teena. How can I help you...'''

def _hru():
    return "I'm fine. Thanks for asking. How are you"

def _close():
    
    return '''Thanks for using.
Closing...'''
