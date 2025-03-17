# Improve the previous challenge by displaying at the end:  

main = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

s = 0
s1 = 0
s2 = 0

for l in range (0, 3):
    for c in range(0,3):
        main[l][c] = int(input(f'Type the number here [{l},{c}]: '))
        # A) The sum of all even values entered.
        if main[l][c] % 2 == 0:
            s = main[l][c] + s

print('=-='*10)

# B) The sum of the values in the third column.
for l in range (0,3):
    s1 += main [l][2]

# C) The largest value in the second row
for l in range (0,3):
    if main [l][1] > s2:
        s2 = main [l][1]

for l in range (0, 3):
    for c in range(0,3):
        print(f'[{main[l][c]:^5}]', end='')
    print()

print('=-='*10)

print(f'The sum of all even values entered: {s}')
print(f'The sum of the values in the third column is: {s1}')
print(f'The largest value in the second row is: {s2}')