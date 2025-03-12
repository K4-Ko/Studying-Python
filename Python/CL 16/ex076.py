# Create a program that has a single tuple with product names and their respective prices, in sequence.  
# At the end, display a price list, organizing the data in a tabular format.

l = ('Rice',8.30,'Milk',3.10,'Bread',4.5,'sugar',2.55,'Eggs',3.69)

print('=-='*15)
print('  '*7,'Products')
print('=-='*15)

print(l[0],'...'*10,'USD',l[1])
print(l[2],'...'*10,'USD',l[3])
print(l[4],'..'*14,' USD',l[5])
print(l[6],'..'*14,' USD',l[7])
print(l[8],'...'*10,'USD',l[9])
print('=-='*15)
