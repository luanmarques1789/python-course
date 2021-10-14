""""
 CHECK THE FIRST CHARACTERES IN A TEXT
 --------------------------------------
 Create a program that reads a city's name and tells
 if it `starts` or `doesn't start` with "SANTO"
"""

city = str(input('Where do you live? ')).lower().split()
isSanto = (False, True)[city[0] == 'santo']

print(isSanto)

# TESTING INPUTS (no single quotes):
# 'santo inácio' -> True
# 'santo inácio' -> False
# '      santo amorim' -> True
# 'amorim santo' -> False
# 'SaNtO inácio' -> True
# 'santo-amorim' -> False
