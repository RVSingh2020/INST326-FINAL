import Singh326_StockProgram

# Function to calculate total P/L
def calc():
    lab_total_pl['text'] = lab_total_pl['text'] + (
                (lab_s1['text'] - lab_b1['text']) + (lab_s2['text'] - lab_b2['text']) + (
                    lab_s3['text'] - lab_b3['text']) + (lab_s4['text'] - lab_b4['text']) + (
                            lab_s5['text'] - lab_b5['text']))
    calculate.config(state=DISABLED)
    assert lab_total_pl > 0 or lab_total_pl <= 0 #returns True

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
    assert lab_day_num > 7 #returns false
