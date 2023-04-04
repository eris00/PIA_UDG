import datetime

# data = datetime.date(1995,3,5)
# print(data)

# print(data.day)
# print(data.month)
# print(data.year)

# dt = datetime.timedelta(-100)
# print("nakon 100 dana: ", data + dt)

# print(data.strftime(data))

# danas = datetime.date.today()

# print(danas.strftime('%B %A-%D, %Y'))    
                                   
# danas = datetime.datetime.now()
danasnji_dan = datetime.datetime.now()
# print(danasnji_dan)

date = datetime.datetime(19,9,2019)

print(danasnji_dan - date)