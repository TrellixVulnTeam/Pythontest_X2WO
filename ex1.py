import datetime

days = lambda year, month, day: (datetime.date.today()-datetime.date(year,month,day)).days

print(days(1990,8,16))