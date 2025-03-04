# Create a program that reads the name of a city and checks whether it starts with the name "SANTO" or not.
c = input(str('Enter the name of the city: ')).strip()
l = c.split()
f = l[0].upper()
print('SANTO' in f)
