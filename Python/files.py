import json

def _read(arg):
    #print(arg)
    try:
        fp = open("data.json","r")
        obj = json.load(fp)
    except:
        __init__()
    finally:
        fp.close()
        #print(obj.get(arg))
        return obj.get(arg)
            
def _write(key,value):
    try:
        fp = open("data.json","r")
        obj = json.load(fp)
    finally:
        fp.close()

    try:
        fp = open("data.json","w")
        obj[key] = value
        fp.write(json.dumps(obj,indent = 4))

    finally:
        fp.close()


def __init__():

    try:
        fp = open("data.json","w")
        data = {      
            "myname"        :"Teena",
            "born"          :"4th July 2020"
            }
        fp.write(json.dumps(data,indent=4))
    finally:
        fp.close()
