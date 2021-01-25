import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
    print('b=', born+2)
    return (calendar.day_name[born])


# Driver program
date = '2021-01-01'
print(findDay(date))
print(findDay('2020-08-12'))
print(findDay('2021-01-03'))


s = '4'
a = [i for i in s]
print(a)
