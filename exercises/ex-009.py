# TIMES TABLES
# Make a program that reads some integer number
# and shows on screen its times tables

num = int(input('Type some number for its times tables: '))

print('-' * 12)
for i in range(0, 10):
    i = i + 1
    print(f'{num} * {i} = {num * i}')
print('-' * 12)
