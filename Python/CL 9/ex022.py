# Create a program that reads a person's full name and displays:
# – The name in all uppercase and lowercase letters.
# – How many letters in total (excluding spaces).
# – How many letters are in the first name.

u = input(str('Enter your full name: ')).strip()
r = u.replace(' ','')

s = u.split()
print('The first name has:', len(s[0]), 'letters,', 'The full name contains:', len(r), 'letters', )
print(u.upper(), 'and', u.lower())
