import time
import datetime

def getToday():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))



def getDayAfter(after_):
    d1 = datetime.datetime.now()
    d3 = d1 + datetime.timedelta(days =after_)
    return str(d3)[0:19]
