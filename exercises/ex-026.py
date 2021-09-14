# FIRST AND LAST OCCURRENCE WITHIN A STRING
# -----------------------------------------
# Make a program that reads a sentence by keyboard and shows:
# 1.1 How many times letter "A" looks
# 1.2 In what position it looks by first time
# 1.3 In what position it looks by last time

sentence = str(input("Enter something... ")).strip().lower()

print(f'How many times does letter "A" look? {sentence.count("a")}')
print(f'In what position does it look by first time? {sentence.find("a") + 1}')
print(f'In what position does it look by last time? {sentence.rfind("a") + 1}')
