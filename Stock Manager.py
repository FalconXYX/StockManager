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

def close(thing):
    global close_final
    global ticker
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
    i = 1
    aapl = pdr.get_data_yahoo(ticker,

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
    close_final = closemonth[pull]

    print(close_final)
def open(thing):
    global open_final
    global ticker
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
    i = 1
    aapl = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    aapl.index
    today = date.today()
    aapl.columns
    closemonth = []
    while i <= 356:
        temp = i*-1
        close = aapl['Open'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    open_final = closemonth[pull]

    print(open_final)
def high(thing):
    global high_final
    global ticker
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
    i = 1
    aapl = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    aapl.index
    today = date.today()
    aapl.columns
    closemonth = []
    while i <= 356:
        temp = i*-1
        close = aapl['High'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    high_final = closemonth[pull]

    print(high_final)
def low(thing):
    global low_final
    global ticker
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
    i = 1
    aapl = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    aapl.index
    today = date.today()
    aapl.columns
    closemonth = []
    while i <= 356:
        temp = i*-1
        close = aapl['Low'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    low_final = closemonth[pull]

    print(low_final)
def volume(thing):
    global volume_final
    global ticker
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
    i = 1
    aapl = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    aapl.index
    today = date.today()
    aapl.columns
    closemonth = []
    while i <= 356:
        temp = i*-1
        close = aapl['Volume'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    volume_final = closemonth[pull]

    print(volume_final)
def adjclose(thing):
    global adjclose_final
    global ticker
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
    i = 1
    aapl = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    aapl.index
    today = date.today()
    aapl.columns
    closemonth = []
    while i <= 356:
        temp = i*-1
        close = aapl['Adj Close'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    adjclose_final = closemonth[pull]

    print(adjclose_final)
class App(tk.Tk):



    def go(self):
        global ticker
        global close_final
        global open_final
        global high_final
        global low_final
        global volume_final
        global adjclose_final
        datein = date_entry.get()
        datein = str(datein)
        datein = int(datein)
        ticker = stock_entry.get()
        ticker = str(ticker)
        print(ticker)
        close(datein)
        open(datein)
        high(datein)
        low(datein)
        volume(datein)
        adjclose(datein)
        close_final = str(close_final)
        open_final = str(open_final)
        high_final = str(high_final)
        low_final = str(low_final)
        volume_final = str(volume_final)
        adjclose_final = str(adjclose_final)

        start = "Stock                Open                                 Low                               High                             Close                          Ajusted Close                       Volume"
        row = ticker + "        " + open_final + "        " + low_final + "        " + high_final + "        " + close_final + "        " + adjclose_final + "         " + volume_final
        Lb1.insert(1, start)
        Lb1.insert(2, row)

    def __init__(self):
        global date_entry
        global stock_entry
        global Lb1
        selfdow_x = 1280
        selfdow_y = 700
        tk.Tk.__init__(self)
        self.title("Stock Manager")
        self.geometry("970x920")
        button = tk.Button(self, text="Submit", command=self.go)
        date_entry = tk.Entry(self)
        stock_entry = tk.Entry(self)
        datelabel = tk.Label(self, text="Enter Days Ago:",fg="Black",font=("Courier", 12))
        stocklabel = tk.Label(self, text="Enter Stock Name:",fg="Black",font=("Courier", 12))
        Lb1 = Listbox(self, width=130, height=34)
        button.place(x=150, y=80)
        date_entry.place(x=200, y=10)
        stock_entry.place(x=200, y=35)
        datelabel.place(x=0, y=10)
        stocklabel.place(x=0, y=35)
        Lb1.place(x=100, y=150)










w = App()
w.mainloop()
