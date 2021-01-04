import datetime as dt


# datetime class
now = dt.datetime.now()

year=now.year

print(now)

print(type(now))

if year==2021:
    print('this is 2021')

day_of_week=now.weekday()
print(day_of_week)

'''設定自己的時間(至少需要年月日)
創建新的datetime對象時，需要提供的唯一內容是
年，月和日。
'''

date_of_birth=dt.datetime(year=1975,month=9,day=23)

print(date_of_birth)