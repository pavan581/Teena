import math
import wikipedia as wiki

def fun(keyword):
    try:
        return wiki.summary(keyword,sentences=1)

    except Exception as e:
        return e