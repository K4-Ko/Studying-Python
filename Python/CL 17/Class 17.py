numbers = []
v = 0

while True:
    n = (input('Type a number here (to stop type any letter: ) '))
    if not n.isdigit(): #Identify if the user's input is a number or letter
        break
    numbers.append(n)


for c, b in enumerate(numbers):
    print(f'The number {b} is in the position {c}')