
from datetime import date, datetime, timedelta
def gen_datestr(today_val):
    y = str(today_val.year)
    m = str(today_val.month)
    d = str(today_val.day)
    if len(m) < 2:
        m = '0' + m
    if len(d) < 2:
        d = '0' + d
    return y + m + d

def todaystr():
    today_val = date.today()
    return gen_datestr(today_val)

def date_sub(day1, day2):
    d1_y, d1_m, d1_d = int(day1[:4]), int(day1[5:7]), int(day1[8:])
    d2_y, d2_m, d2_d = int(day2[:4]), int(day2[5:7]), int(day2[8:])
    d1 = datetime(d1_y, d1_m, d1_d)
    d2 = datetime(d2_y, d2_m, d2_d)
    return (d1-d2).days

def isleapyear(year):
    if year % 4 ==0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def month_days(datestr):
    d1_y, d1_m, d1_d = int(datestr[:4]), int(datestr[5:7]), int(datestr[8:])
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_calc = days[d1_m]

    if isleapyear(d1_y) and d1_m == 2 and d1_d == 29:
        day_calc += 1

    return day_calc

def issameweek(day1, day2):
    d1_y, d1_m, d1_d = int(day1[:4]), int(day1[5:7]), int(day1[8:])
    d2_y, d2_m, d2_d = int(day2[:4]), int(day2[5:7]), int(day2[8:])
    cal1 =  datetime(d1_y, d1_m, d1_d)
    cal2 =  datetime(d2_y, d2_m, d2_d)
    return cal1.isocalendar()[1] == cal2.isocalendar()[1]

def issamemonth(day1, day2):
    d1_m = int(day1[5:7])
    d2_m = int(day2[5:7])
    if d1_m == d2_m:
        return True
    else:
        return False

def next_n_day(datestr, number):
    d1_y, d1_m, d1_d = int(datestr[:4]), int(datestr[4:6]), int(datestr[6:])
    olddate = datetime(d1_y, d1_m, d1_d)
    newdate = olddate + timedelta(number)
    newstr = str(newdate.year) + str(newdate.month) + str(newdate.day)
    return newstr
