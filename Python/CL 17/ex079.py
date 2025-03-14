# Create a program where the user can enter multiple numerical values 
# and store them in a list. If the number already exists in the list, 
# it should not be added again. 
# In the end, display all unique values entered, in ascending order.

list = []


while True:
    n = int(input('Type a number to add in the list: (To stop add 999): '))
    if n == 999:
        break
    if n not in list:
        list.append(n)
list.sort()

print(list)
