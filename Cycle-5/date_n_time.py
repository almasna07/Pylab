import datetime
now=datetime.datetime.now()
current_year=now.year
month_year=now.strftime("%B")
week_number=now.strftime("%U")
weekday_name=now.strftime("%A")
day_of_year=now.strftime("%j")
days=now.day
day_of_week=now.strftime("%A")
print("Current date and time:",now)
print("Current Year:",current_year)
print("Month of the year:",month_year)
print("Week Number of Year:",week_number)
print("Week Day Name:",weekday_name)
print("Day of Year:",day_of_year)
print("Day of Month:",days)
print("Day of the Week:",day_of_week)

