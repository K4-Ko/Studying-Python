# Create a program that reads a sentence from the keyboard and shows:
# - How many times the letter "A" appears
# - The position where it first appears
# - The position where it last appears

f = input('Enter a sentence: ').upper()
l1 = f.count('A')
l2 = f.find('A')
l3 = f.rfind('A')

print('The sentence contains:', l1, '"A"', '\nThe first "A" appears at position:', l2, '\nThe last "A" appears at position:', l3)
