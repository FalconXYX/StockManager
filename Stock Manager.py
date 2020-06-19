#imports/varaibles
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import pandas_datareader as pdr
import datetime
from datetime import date
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
from datetime import date
global close_final
global open_final
global high_final
global low_final
global volume_final
global adjclose_final
global l
global low52_final
global high52_final
close_final = []
open_final = []
low_final = []
high_final = []
volume_final = []
adjclose_final = []
high52_final = []
low52_final = []
l = 2
# historical average functions
def close(thing):
    global closemonth
    global close_final
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    stocklistinfo.index
    today = date.today()
    stocklistinfo.columns
    while i <= 1000:
        temp = i*-1
        close = stocklistinfo['Close'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    close_final.insert(len(close_final),closemonth[pull])
    print(close_final)
def open(thing):
    global open_final
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    stocklistinfo.index
    today = date.today()
    stocklistinfo.columns
    while i <= 1000:
        temp = i*-1
        close = stocklistinfo['Open'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    open_final = []
    open_final.insert(len(open_final), closemonth[pull])
def high(thing):
    global high_final
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    i = 1
    l =2
    stocklistinfo = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    stocklistinfo.index
    today = date.today()
    stocklistinfo.columns
    while i <= 1000:
        temp = i*-1
        close = stocklistinfo['High'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    high_final = []
    high_final.insert(len(high_final), closemonth[pull])
def low(thing):
    global low_final
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    stocklistinfo.index
    today = date.today()
    stocklistinfo.columns
    while i <= 1000:
        temp = i*-1
        close = stocklistinfo['Low'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    low_final = closemonth[pull]
    low_final = []
    low_final.insert(len(low_final), closemonth[pull])
def volume(thing):
    global volume_final
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    stocklistinfo.index
    today = date.today()
    stocklistinfo.columns
    closemonth = []
    while i <= 1000:
        temp = i*-1
        close = stocklistinfo['Volume'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    volume_final.insert(len(volume_final), closemonth[pull])
def adjclose(thing):
    global adjclose_final
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,

                              end=datetime.datetime(year, month, day),
                             )
    stocklistinfo.index
    today = date.today()
    stocklistinfo.columns
    closemonth = []
    while i <= 1000:
        temp = i*-1
        close = stocklistinfo['Adj Close'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    pull = thing
    adjclose_final.insert(len(adjclose_final), closemonth[pull])
def high52():
    global ticker
    global year
    global month
    global day
    global high52_final
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    year -= 1
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,
                              start=datetime.datetime(year, 1, 1),
                              end=datetime.datetime(year, 12, 31),
                             )
    stocklistinfo.index
    stocklistinfo.columns
    closemonth = []
    while i <= 250:
        temp = i*-1
        close = stocklistinfo['High'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    closemonth.sort()
    pull = closemonth[-1]
    high52_final.insert(len(adjclose_final), pull)
def low52():
    global ticker
    global year
    global month
    global day
    global low52_final
    closemonth = []
    today = datetime.date.today()
    today = str(today)
    day = today[-2:]
    year, month, lol  = today.split('-')
    year = int(year)
    year -= 1
    month = int(month)
    day = int(day)
    i = 1
    stocklistinfo = pdr.get_data_yahoo(ticker,
                              start=datetime.datetime(year, 1, 1),
                              end=datetime.datetime(year, 12, 31),
                             )
    stocklistinfo.index
    stocklistinfo.columns
    closemonth = []
    while i <= 250:
        temp = i*-1
        close = stocklistinfo['Low'][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1
    closemonth.sort()
    pull = closemonth[1]
    low52_final.insert(len(adjclose_final), pull)

# graph functions
def infograph(type, stockname, stockname2):
    global endcal
    global startcal
    global stocklistinfo
    date1 = str(startcal.get_date())
    date2 = str(endcal.get_date())
    day1 = date1[-2:]
    year1, month1, lol  = date1.split('-')
    year1 = int(year1)
    month1 = int(month1)
    day1 = int(day1)
    day2 = date2[-2:]
    year2, month2, lol  = date2.split('-')
    year2 = int(year2)
    month2 = int(month2)
    day2 = int(day2)
    stocklistinfo = pdr.get_data_yahoo(stockname,
                              start=datetime.datetime(year1, month1, day1),
                              end=datetime.datetime(year2, month2, day2),
                             )
    stocklistinfo2 = pdr.get_data_yahoo(stockname2,
                              start=datetime.datetime(year1, month1, day1),
                              end=datetime.datetime(year2, month2, day2),
                             )
    stocklistinfo.index
    stocklistinfo.columns
    stocklistinfo[type].plot(grid=True)
    stocklistinfo2[type].plot(grid=True)
    plt.show()


class App(tk.Tk):
    def go(self):
        global l
        global ticker
        global close_final
        global open_final
        global high_final
        global low_final
        global volume_final
        global adjclose_final
        global high52_final
        global low52_final
        datein = date_entry.get()
        datein = str(datein)
        datein = int(datein)
        ticker = stock_entry.get()
        ticker = str(ticker)
        close(datein)
        open(datein)
        high(datein)
        low(datein)
        volume(datein)
        adjclose(datein)
        high52()
        low52()

        closetemp = str(round(close_final[len(close_final)-1], 3))
        opentemp = str(round(open_final[len(open_final)-1], 3))
        hightemp = str(round(high_final[len(high_final)-1], 3))
        lowtemp = str(round(low_final[len(low_final)-1], 3))
        volumetemp = str(round(volume_final[len(volume_final)-1], 3))
        adjclosetemp = str(round(adjclose_final[len(adjclose_final)-1], 3))
        h52temp = str(round(high52_final[len(high52_final)-1], 3))
        l52temp = str(round(low52_final[len(low52_final)-1], 3))



        row = ticker + "        " + opentemp + "              " + lowtemp + "              " + hightemp + "              " + closetemp + "              " + adjclosetemp + "                  " + volumetemp + "                 "+ h52temp + "                   " + l52temp
        Lb1.insert(l, row)
        l += 1
    def graph(self):
        global type_entry
        global stock_entry2
        global stock_entry3
        global stocklistinfo
        temptype = type_entry.get()
        tempstock = stock_entry2.get()
        tempstock2 = stock_entry3.get()
        if (tempstock2 != ""):
            infograph(temptype, tempstock, tempstock2)
    def __init__(self):
        global endcal
        global startcal
        global date_entry
        global stock_entry
        global type_entry
        global stock_entry2
        global Lb1
        global stock_entry3
        selfdow_x = 1780
        selfdow_y = 1700
        tk.Tk.__init__(self)
        self.title("Stock Manager")
        self.geometry("1920x1080")
        button = tk.Button(self, text="Submit", command=self.go)
        button2 = tk.Button(self, text="Submit", command=self.graph)
        date_entry = tk.Entry(self)
        stock_entry = tk.Entry(self)
        type_entry = tk.Entry(self)
        stock_entry2 = tk.Entry(self)
        stock_entry3 = tk.Entry(self)
        datelabel = tk.Label(self, text="Enter Days Ago:",fg="Black",font=("Courier", 12))
        stocklabel = tk.Label(self, text="Enter Stock Name:",fg="Black",font=("Courier", 12))
        typelabel = tk.Label(self, text="Enter Type:",fg="Black",font=("Courier", 12))
        stocklabel2 = tk.Label(self, text="Enter Stock Name:",fg="Black",font=("Courier", 12))
        Lb1 = Listbox(self, width=130, height=34, yscrollcommand=True)
        start = "Stock           Open           Low            High            Close            Ajusted Close            Volume          W52 High         W52 Low"
        Lb1.insert(1, start)
        startcal = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2)
        endcal = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2)
        startlabelcal = tk.Label(self, text="Enter Start Date:",fg="Black",font=("Courier", 12))
        endlabelcal = tk.Label(self, text="Enter End Date:",fg="Black",font=("Courier", 12))
        #placing
        startcal.place(x=1650, y=40)
        endcal.place(x=1650, y=80)
        startlabelcal.place(x=1450, y=40)
        endlabelcal.place(x=1450, y=80)
        button.place(x=150, y=80)
        button2.place(x=1600, y=200)
        date_entry.place(x=200, y=10)
        stock_entry.place(x=200, y=35)
        datelabel.place(x=0, y=10)
        stocklabel.place(x=0, y=35)
        Lb1.place(x=100, y=150)
        typelabel.place(x=1450, y=120)
        stocklabel2.place(x=1450, y=160)
        type_entry.place(x=1650, y=120)
        stock_entry2.place(x=1650, y=160)
        stock_entry3.place(x=1650, y=200)










w = App()
w.mainloop()
