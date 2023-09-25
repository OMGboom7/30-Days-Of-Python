from datetime import datetime, time, date

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second

timestamp = now.timestamp()
print(year, month, day, hour, minute, second)
print('timestamp:', timestamp)
print(f'{day}/{month}/{year},{hour}:{minute}')

t = now.strftime('%H:%M:%S')
print('time:', t)
time_1 = now.strftime('%m/%d/%Y, %H:%M:%S')
print('time1:'), time_1

"""
1.Get the current day, month, year, hour, minute and timestamp from datetime module
2.Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
3.Today is 5 December, 2019. Change this time string to time.
4.Calculate the time difference between now and new year.
5.Calculate the time difference between 1 January 1970 and now.
6.Think, what can you use the datetime module for? Examples:
    Time series analysis
    To get a timestamp of any activities in an application
    Adding posts on a blog
"""
t4 = now.strftime('%m/%d/%Y, %H:%M:%S')
print(t4)

time2 = date(day=5, month=12, year=2019)
print(time2)

new_year = datetime.strptime('2024-01-01 00:00:00','%Y-%m-%d %H:%M:%S')

print(new_year-now)