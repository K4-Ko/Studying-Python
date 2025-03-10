# Write a program that reads a person's gender but only accepts the values 'M' or 'F'.  
# If an incorrect value is entered, prompt the user to enter it again until a valid value is provided.



g =''
while g != 'M' and g != 'F':
    g = str(input('Typer your gender: [M] Male or [F] Female: ')).upper()
    if g != 'M' and g!= 'F':
        print('Try Again !')
print('Thanks for updating your information !')
    


        

