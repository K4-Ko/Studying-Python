# Create a program that declares a 3×3 matrix  
# and fills it with values entered by the user via keyboard.  
# At the end, display the matrix on the screen with proper formatting.  

main = []

for c in range (1, 10):
    num = int(input('Type number to ad in the Matrix:  '))
    main.append(num)

print(f'[{main[0]:^5}] [{main[1]:^5}] [{main[2]:^5}]')
print(f'[{main[3]:^5}] [{main[4]:^5}] [{main[5]:^5}]')
print(f'[{main[6]:^5}] [{main[7]:^5}] [{main[8]:^5}]')