import datetime

my_date = datetime.date(2015, 10, 21)

my_time = datetime.time(7, 28, 1)

my_datetime = datetime.datetime(2015, 10, 21, 7, 28, 1)

print(my_date)
print(my_time)
print(my_datetime)
print(my_date.year, my_date.month, my_date.day)
print(my_time.hour, my_time.minute, my_time.second)

now = datetime.datetime.today()
print(now)

output = '{: %A, %B, %d, %Y}'
print(output.format(my_date))
