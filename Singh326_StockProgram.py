###INST 326 Final Project

from tkinter import *
from tkinter import ttk
import random


# Functions for buy and sell buttons
def buy(stock, bp):
    b_price = stock['text']
    bp.config(text=b_price)


def sell(stock, sp, ):
    s_price = stock['text']
    sp.config(text=s_price)


# Function to calculate total P/L
def calc():
    lab_total_pl['text'] = lab_total_pl['text'] + (
                (lab_s1['text'] - lab_b1['text']) + (lab_s2['text'] - lab_b2['text']) + (
                    lab_s3['text'] - lab_b3['text']) + (lab_s4['text'] - lab_b4['text']) + (
                            lab_s5['text'] - lab_b5['text']))
    calculate.config(state=DISABLED)


# Function to move to next day
def next():
    if lab_day_num['text'] < 7:
        lab_price1.config(text=random.randint(0, 1001))
        lab_price2.config(text=random.randint(0, 1001))
        lab_price3.config(text=random.randint(0, 1001))
        lab_price4.config(text=random.randint(0, 1001))
        lab_price5.config(text=random.randint(0, 1001))
        lab_day_num.config(text=lab_day_num['text'] + 1)
    calculate.config(state=ACTIVE)


# create a window
# https://www.youtube.com/watch?v=ddoPYppcppc
window = Tk()
window.title('DR Stock Simulation')
window.geometry("500x500")
window.resizable(width=True, height=True)  # https://www.youtube.com/watch?v=SVW0ofsBKCU

# create notebook object in order to have tabs for gui
# https://www.youtube.com/watch?v=UhHWAfIbOy4
nb = ttk.Notebook(window)
frame1 = ttk.Frame(nb)
frame2 = ttk.Frame(nb)
nb.add(frame1, text='Simulation')
nb.add(frame2, text='Results')
nb.pack()

# define labels
# https://www.youtube.com/watch?v=ddoPYppcppc
lab1 = Label(frame1, text='Apple')
lab1.grid(row=1, column=0)

lab2 = Label(frame1, text='Amazon')
lab2.grid(row=2, column=0)

lab3 = Label(frame1, text='Tesla')
lab3.grid(row=3, column=0)

lab4 = Label(frame1, text='Nike')
lab4.grid(row=4, column=0)

lab5 = Label(frame1, text='Microsoft')
lab5.grid(row=5, column=0)

lab_day = Label(frame1, text='Day')
lab_day.grid(row=6, column=0)

# keeps track of what day simulation is on
lab_day_num = Label(frame1, text=1)
lab_day_num.grid(row=6, column=1)

lab_price = Label(frame1, text='Price ($)')
lab_price.grid(row=0, column=1)

# Sets prices of stocks to a random number for day 1 of simulation
lab_price1 = Label(frame1, text=random.randint(0, 1001))
lab_price1.grid(row=1, column=1)

lab_price2 = Label(frame1, text=random.randint(0, 1001))
lab_price2.grid(row=2, column=1)

lab_price3 = Label(frame1, text=random.randint(0, 1001))
lab_price3.grid(row=3, column=1)

lab_price4 = Label(frame1, text=random.randint(0, 1001))
lab_price4.grid(row=4, column=1)

lab_price5 = Label(frame1, text=random.randint(0, 1001))
lab_price5.grid(row=5, column=1)

# define labels for watchlist
# https://www.youtube.com/watch?v=ddoPYppcppc
lab1_res = Label(frame2, text='Apple')
lab1_res.grid(row=1, column=0)

lab2_res = Label(frame2, text='Amazon')
lab2_res.grid(row=2, column=0)

lab3_res = Label(frame2, text='Tesla')
lab3_res.grid(row=3, column=0)

lab4_res = Label(frame2, text='Nike')
lab4_res.grid(row=4, column=0)

lab5_res = Label(frame2, text='Microsoft')
lab5_res.grid(row=5, column=0)

# keeps track of price that stock was bought at
lab_b = Label(frame2, text='Buy Price ($)')
lab_b.grid(row=0, column=1)

lab_b1 = Label(frame2, text=0)
lab_b1.grid(row=1, column=1)

lab_b2 = Label(frame2, text=0)
lab_b2.grid(row=2, column=1)

lab_b3 = Label(frame2, text=0)
lab_b3.grid(row=3, column=1)

lab_b4 = Label(frame2, text=0)
lab_b4.grid(row=4, column=1)

lab_b5 = Label(frame2, text=0)
lab_b5.grid(row=5, column=1)

# Keeps track of what stock was sold at
lab_s = Label(frame2, text='Sell Price ($)')
lab_s.grid(row=0, column=2)

lab_s1 = Label(frame2, text=0)
lab_s1.grid(row=1, column=2)

lab_s2 = Label(frame2, text=0)
lab_s2.grid(row=2, column=2)

lab_s3 = Label(frame2, text=0)
lab_s3.grid(row=3, column=2)

lab_s4 = Label(frame2, text=0)
lab_s4.grid(row=4, column=2)

lab_s5 = Label(frame2, text=0)
lab_s5.grid(row=5, column=2)

# Calculates the total p/l of simulation by finding difference in buy and sell price and summation
calculate = Button(frame2, text="Calc. P/L($)", command=lambda: calc(), width=10)
calculate.grid(row=6, column=0, rowspan=1)

lab_total = Label(frame2, text='Total P/L($):')
lab_total.grid(row=6, column=1)

lab_total_pl = Label(frame2, text=0)
lab_total_pl.grid(row=6, column=2)

# define buttons
# buy and sell buttons that will change buy and sell price values in results
b1 = Button(frame1, text="BUY", command=lambda: buy(lab_price1, lab_b1), width=5)
b1.grid(row=1, column=3, rowspan=1)

b1_c = Button(frame1, text="SELL", command=lambda: sell(lab_price1, lab_s1), width=5)
b1_c.grid(row=1, column=4, rowspan=1)

b2 = Button(frame1, text="BUY", command=lambda: buy(lab_price2, lab_b2), width=5)
b2.grid(row=2, column=3, rowspan=1)

b2_c = Button(frame1, text="SELL", command=lambda: sell(lab_price2, lab_s2), width=5)
b2_c.grid(row=2, column=4, rowspan=1)

b3 = Button(frame1, text="BUY", command=lambda: buy(lab_price3, lab_b3), width=5)
b3.grid(row=3, column=3, rowspan=1)

b3_c = Button(frame1, text="SELL", command=lambda: sell(lab_price3, lab_s3), width=5)
b3_c.grid(row=3, column=4, rowspan=1)

b4 = Button(frame1, text="BUY", command=lambda: buy(lab_price4, lab_b4), width=5)
b4.grid(row=4, column=3, rowspan=1)

b4_c = Button(frame1, text="SELL", command=lambda: sell(lab_price4, lab_s4), width=5)
b4_c.grid(row=4, column=4, rowspan=1)

b5 = Button(frame1, text="BUY", command=lambda: buy(lab_price5, lab_b5), width=5)
b5.grid(row=5, column=3, rowspan=1)

b5_c = Button(frame1, text="SELL", command=lambda: sell(lab_price5, lab_s5), width=5)
b5_c.grid(row=5, column=4, rowspan=1)

b5_c = Button(frame1, text="Next Day", command=next, width=10)
b5_c.grid(row=6, column=3, columnspan=2)

# start the GUI
window.mainloop()
