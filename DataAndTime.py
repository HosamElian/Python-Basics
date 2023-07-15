import datetime

# print current dataTime and  time
print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)

print("=" * 50)

# print min and max of dateTime
print(datetime.datetime.min)
print(datetime.datetime.max)

print("=" * 50)

# print current time
print(datetime.datetime.now().time())
print(datetime.datetime.now().time().hour)
print(datetime.datetime.now().time().minute)
print(datetime.datetime.now().time().second)

print("=" * 50)

# print min and max of time
print(datetime.time.min)
print(datetime.time.max)

print("=" * 50)

# print specific datatime
print(datetime.datetime(1998, 9, 1, 12, 00, 00, 198))

# subtract dates
mybirthday = datetime.datetime(1998, 9, 1, 12, 00, 00, 198)
dateNow = datetime.datetime.now()
print(f"May Age is {((dateNow - mybirthday).days)/365}")


# day formating
print(mybirthday.strftime("%d, %B, %Y"))