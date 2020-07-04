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
import datetime,time
import matplotlib.pyplot as plt
from datetime import date
import concurrent.futures
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
def close(thing, stype, vari):
    global closemonth
    global ticker
    global year
    global month
    global day
    closemonth = []
    today = datetime.date.today()
    t= datetime.date.today()
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
    pull = (t-thing).days
    while i <= pull+1:
        temp = i*-1
        close = stocklistinfo[stype][temp]
        store = close
        store = float(store)
        closemonth.insert(len(closemonth),store)
        i += 1

    vari.insert(len(vari),closemonth[pull])
    return str(round(vari[len(vari)-1], 3))
    print(vari)
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
    return str(round(high52_final[len(high52_final)-1], 3))
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
    return str(round(low52_final[len(low52_final)-1], 3))

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
        datein = cal.get_date()
        print(datein)
        ticker = stock_entry.get()
        ticker = str(ticker)
        startTime = time.time()
        with concurrent.futures.ThreadPoolExecutor() as executor:
                closefunction = executor.submit(close, datein, "Close", close_final)
                closetemp = closefunction.result()
                print(closetemp)
                openfunction = executor.submit(close, datein, "Open", open_final)
                opentemp = openfunction.result()
                print(opentemp)
                highfunction = executor.submit(close, datein, "High", high_final)
                hightemp = highfunction.result()
                print(hightemp)
                lowfunction = executor.submit(close, datein, "Low", low_final)
                lowtemp = openfunction.result()
                print(lowtemp)
                volumefunction = executor.submit(close, datein, "Volume", volume_final)
                volumetemp = volumefunction.result()
                print(volumetemp)
                adjclosefunction = executor.submit(close, datein, "Adj Close", adjclose_final)
                adjclosetemp = adjclosefunction.result()
                print(adjclosetemp)
        h52temp = high52()
        l52temp = low52()
        endTime = time.time()
        print('Took %s seconds to calculate.' % (endTime - startTime))



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
        global cal
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
        datelabel = tk.Label(self, text="Enter Date:",fg="Black",font=("Courier", 12))
        stocklabel = tk.Label(self, text="Enter Stock Name:",fg="Black",font=("Courier", 12))
        typelabel = tk.Label(self, text="Enter Type:",fg="Black",font=("Courier", 12))
        stocklabel2 = tk.Label(self, text="Enter Stock Names:",fg="Black",font=("Courier", 12))
        Lb1 = Listbox(self, width=130, height=34, yscrollcommand=True)
        start = "Stock           Open           Low            High            Close            Ajusted Close            Volume          W52 High         W52 Low"
        Lb1.insert(1, start)
        cal = DateEntry(self, width=12, background='black', foreground='white', borderwidth=2)
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
        button2.place(x=1600, y=230)
        cal.place(x=200, y=10)
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
