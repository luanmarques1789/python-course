"""
 LOOKING FOR A STRING WITHIN ANOTHER
 ------------------------------------
 Create an algorithm that reads a person's name and
 tells if he has "SILVA" in his name
"""

name = str(input("What's your name? ")).lower().split()
print(f"Your name has 'Silva'? {'silva' in name}")
