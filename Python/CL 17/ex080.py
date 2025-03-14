# Create a program where the user can enter five numerical values 
# and store them in a list, inserting each value in the correct position 
# without using the sort() function. 
# In the end, display the sorted list on the screen.

i1 = int(input('Type a number here: '))
i2 = int(input('Type a number here: '))
i3 = int(input('Type a number here: '))
i4 = int(input('Type a number here: '))
i5 = int(input('Type a number here: '))

prelist = [i1, i2, i3, i4, i5]

#find the largest and smalest number
smalest = min (prelist)
smalest2 = 0
middle = 0
largest2= 0
largest = max (prelist)

#remove from pre list the largest and smalest number
prelist.remove (smalest)
prelist.remove (largest)

# find the second smalest 
if prelist[0] < prelist[1] and prelist[1] < prelist[2]:
     smalest2 = prelist[0]
elif prelist[1] < prelist[0] and prelist[1] < prelist[2]:
     smalest2 = prelist[1]
elif prelist[2] < prelist[0] and prelist[2] < prelist[1]:
     smalest2 = prelist[2]

# remove the second smalest from pre list 
prelist.remove (smalest2)

# find the second largest
if prelist[0] > prelist[1]:
    largest2 = prelist [0]
else:
     largest2 = prelist [1]
# remove the second largest from pre list 
prelist.remove (largest2)

# find the middle number 
middle = prelist[0]

# making a new list with the organized number
list = [smalest, smalest2, middle, largest2, largest]

print(list)