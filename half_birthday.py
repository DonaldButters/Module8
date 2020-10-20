from datetime import timedelta
import datetime

def half_birthday(date):
        hbday = date + (timedelta(days=365/2))
        return hbday.strftime(('%B' + ' ' + '%d' + ', ' + '%Y'))

def test_half_birthday():
    bday = datetime.datetime(2019, 11, 28)
    if half_birthday(bday) == 'May 28, 2020':
        return True
    else:
        return False

bday = datetime.datetime(2019, 11, 28)
print('Your most recent birthday was: ')
print(bday.strftime(('%B' + ' ' + '%d' + ', ' + '%Y')))


print('Your half birthday is: ')
a = half_birthday(bday)
print(a)

print(test_half_birthday())

