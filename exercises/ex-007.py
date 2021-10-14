"""
 STUDENT'S AVERAGE
 ------------------
 Develop a program that reads two student's grade,
 calcs and shows his average
"""

grade1 = float(input('Type the firts grade: '))
grade2 = float(input('Type the second grade: '))

# Python rounds numbers to up or down automatically
# when user especify decimal place quantity
average = (grade1 + grade2) / 2
print('the average is... {:.1f}'.format(average))
