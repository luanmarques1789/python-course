# TEXT ANALYZER
# -------------
# Create a program that reads a person's full name and shows:
# 1.1 The name with all letters in upper and lower case
# 1.2 How many letters does it have? (no space)
# 1.3 How many letters does first name have?

name = str(input("What's your full name? ")).strip()

# bold text
bold_ = '\u001b[1m'  # open "tag"
_bold = '\u001b[0m'  # close "tag"

print(f'Your name in {bold_}upper{_bold} case: {name.upper()}')
print(f'Your name in {bold_}lower{_bold} case: {name.lower()}')

splited = name.split()
print(f"Your name has {bold_}{len(''.join(splited))} letters{_bold}")

print(f"Your first name is {bold_}{splited[0]}{_bold} and", end=' ')
print(f"it has {bold_}{len(splited[0])} letters{_bold}")
