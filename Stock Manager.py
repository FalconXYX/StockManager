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
def close(thing):
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
    push = closemonth[pull]

    print(push)





ticker = "AAPL"
class App(tk.Tk):



    def go(self):
        datein = date_entry.get()
        datein = str(datein)
        datein = int(datein)
        ticker = stock_entry.get()
        ticker = str(ticker)
        close(datein)
    def __init__(self):
        global date_entry
        global stock_entry
        selfdow_x = 1280
        selfdow_y = 720
        tk.Tk.__init__(self)
        self.title("Stock Manager")
        self.geometry("720x720")
        button = tk.Button(self, text="Click", command=self.go)
        date_entry = tk.Entry(self)
        stock_entry = tk.Entry(self)
        button.place(x=340, y=280)
        date_entry.place(x=280, y=380)
        stock_entry.place(x=280, y=480)









w = App()
w.mainloop()
