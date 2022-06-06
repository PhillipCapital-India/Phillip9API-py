from NorenRestApiPy.NorenApi import  NorenApi
from threading import Timer
import pandas as pd
import time

class SymbolItem:
    def __init__(self):
        self.df = None
        self.key = None
        self.counter  = 0
        self.lasttime = 0    

def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)


class P9ApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://p9betanoren.phillipcapital.in/NorenWClientTP/', websocket='wss://p9betanoren.phillipcapital.in/NorenWSTP/', eodhost='https://p9betanoren.phillipcapital.in/chartApi/getdata/')

    
    