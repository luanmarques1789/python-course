# FIRST AND LAST PERSON'S NAME
# ============================
# Make a program that reads person's full name showing after the
# first and last name apart

name = str(input('Type your full name: ')).strip()

splited = name.split()
print(f'First name: {splited[0]}')
print(f'Last name: {splited[len(splited) - 1]}')
