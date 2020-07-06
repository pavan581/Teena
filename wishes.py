import datetime

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        x = "Good Morning!"

    elif hour>=12 and hour<17:
        x = "Good Afternoon!"

    else:
        x = "Good Evening!"
    return f'''{x}
I'm Teena. How can I help you...'''

def hru():
    return "I'm fine. Thanks for asking. How are you"

def gn():
    print("Good night :)")
    return "Good night. Sweet dreams."
