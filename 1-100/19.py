# Problem link: http://projecteuler.net/index.php?section=problems&id=19

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def isValidDay(year, month, day):
    if month == 2:
        if isLeapYear(year):
            if day >= 1 and day <= 29:
                return True
            else:
                return False
        else:
            if day >= 1 and day <= 28:
                return True
            else:
                return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day >= 1 and day <= 30:
            return True
        else:
            return False
    elif month < 1 or month > 12:
        return False
    else:
        if day >= 1 and day <= 31:
            return True
        else:
            return False

res = 0
weekday = 1
for year in range(1900, 2001):
    for month in range(1, 13):
        for day in range(1, 32):
            if isValidDay(year, month, day):
                if weekday == 0 and day == 1 and year > 1900:
                    res += 1
                weekday += 1
                if weekday == 7:
                    weekday = 0
print res

