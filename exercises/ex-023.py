"""
 SPLITTING NUMBER DIGITS
 ------------------------
 Make a program that reads a number of 0 to 9999 and shows
 on screen each splited digits
"""

num = int(input('Type some number: '))


ones = num // 1 % 10
tens = num // 10 % 10
hundreds = num // 100 % 10
thousends = num // 1000 % 10

bold_ = '\u001b[1m'
_bold = '\u001b[0m'
print(f"Ones:{bold_}{ones}{_bold}", end='  ')
print(f"Tens:{bold_}{tens}{_bold}", end='  ')
print(f"Hudreds:{bold_}{hundreds}{_bold}", end='  ')
print(f"Thousends:{bold_}{thousends}{_bold}")
