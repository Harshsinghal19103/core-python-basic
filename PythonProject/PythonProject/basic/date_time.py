import datetime

dob = datetime.date(2003, 5, 12)
print(dob)

now = datetime.datetime.now()
print(now)

future = now + datetime.timedelta(days=750)
print("future is", future)

past = now - datetime.timedelta(days=500)
print("past is", past)

format = "%d-%m-%y %H:%M:%S"
print(now.strftime(format))

time = datetime.time(11,8,54)
print(time.minute)

# age = now.year - dob.year
# print(age)
#
# d = datetime.datetime.now()
# print(d)
# print(d.year)
# print(d.month)
# print(d.day)
# print(d.hour)
# print(d.minute)
# print(d.second)
