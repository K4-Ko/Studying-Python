# Create a program where the user can enter seven numeric values  
# and store them in a single list that keeps even and odd values separated.  
# At the end, display the even and odd values in ascending order.  

x = 0 
main_list = [[],[]]

for c in range(1,8):
    x+=1
    n = int(input(f'Type the {x} number here: '))
    if n % 2 == 0:
        main_list[0].append(n)
    elif n % 2 != 0:
        main_list[1].append(n)

main_list[0].sort()
main_list[1].sort()

print(f'The even numbers entered are: {main_list[0]} \nand the odd numbers are: {main_list[1]}')