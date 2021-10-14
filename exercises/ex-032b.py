"""
 BISSEXTUS YEAR
 ---------------
 Second resolution
 Source: https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=43
"""

from datetime import date

year = int(input('Enter some year or input 0 for current year: '))

if (year == 0):
    year = date.today().year

# LOGIC:
# 1. The year must be divisible by 4.
# 2. If the year is divisible by 100, it must also be divisible by 400.

isBissext = False
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    isBissext = True

print(
    f'{year} is a leap year... \u001b[1m{"YES" if isBissext else "NO"}\u001b[0m')
