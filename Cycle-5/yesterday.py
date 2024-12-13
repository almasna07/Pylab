import datetime as m
today=m.date.today()
yesterday=today-m.timedelta(days=1)
tomorrow=today+m.timedelta(days=1)
print("Yesterday:",yesterday)
print("Today:",today)
print("Tomorrow:",tomorrow)

