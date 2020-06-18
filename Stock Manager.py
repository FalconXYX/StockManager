import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import pandas_datareader as pdr
import datetime
from datetime import date
import pandas_datareader as pdr
import datetime
from datetime import date


ticker = "AAPL"
class App(tk.Tk):
    ticker = "AAPL"
    def dates(self):
        global year
        global month
        global day
        today = datetime.date.today()
        today = str(today)
        day = today[-2:]
        year, month, lol  = today.split('-')
        year = int(year)
        month = int(month)
        day = int(day)
    def close(thing, stock, self):
        dates(self)
        i = 1
        aapl = pdr.get_data_yahoo(stock,

                                  end=datetime.datetime(year, month, day),
                                 )
        aapl.index
        today = date.today()
        aapl.columns
        closemonth = []
        while i <= 356:
            temp = i*-1
            close = aapl['Close'][temp]
            store = close
            store = float(store)
            closemonth.insert(len(closemonth),store)
            i += 1
        pull = thing
        push = closemonth[pull]

        print(push)
    def __init__(self):
        selfdow_x = 1280
        selfdow_y = 720
        tk.Tk.__init__(self)
        self.title("Stock Manager")
        self.geometry("720x720")
        button = tk.Button(self, text="Click", command=self.close(9, ticker))








w = App()
w.mainloop()
