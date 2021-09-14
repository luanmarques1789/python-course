# BISSEXTUS YEAR
# --------------
# Make a proogram that reads some year and shows
# if it is bissextus

from datetime import date

year = int(input('Enter some year or input 0 for current year: '))

if (year == 0):
    year = date.today().year


# LOGIC:
# 1. The year must be divisible by 4.
# 2. If the year is divisible by 100, it must also be divisible by 400.
# by Leap Year Calculator (OMNI CALCULATOR)

isBissext = False
if (year % 4 == 0):
    isBissext = True
    if(year % 100 == 0 and year % 400 == 0):
        isBissext = True
    elif(year % 100 == 0 and year % 400 != 0):
        isBissext = False


print(
    f'{year} is a leap year... \u001b[1m{"YES" if isBissext else "NO"}\u001b[0m')
