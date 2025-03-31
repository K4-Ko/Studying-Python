# Create a registration menu in Python
# a) The menu should ask for name and age
# b) The menu should save these data
# c) The menu should display the saved data

from time import sleep
from menu_functional1 import functional
from menu_visual1 import visual
import os

def main():
    
        print(visual.menu_principal_visual())  

        while True:

            p = functional.option_menu('Choose an option: ')
            
            if p == 1:
                print(visual.print_option1())
                try:
                    # with open abre e fecha o arquivo de forma segura 
                    with open('Python\CL 23\menu_project\ register.txt', 'r') as file:
                        for line in file:
                            print(line.strip())
                except FileNotFoundError:
                    print('No records found.')
            
            elif p == 2:
                
                print(visual.print_option2())
                while True:
                    
                    while True:
                        name_person = str(input('Enter the name: '))
                        
                        if name_person.replace(' ','').isalpha():
                            break
                        else:
                            print(visual.print_error_temp())

                    while True:    
                        age_person = input('Enter the age: ')
                        
                        try:
                            age_person = int(age_person)
                            break
                            
                        except ValueError:
                            print(visual.print_error_temp())

                    with open('Python\\CL 23\\menu_project\\ register.txt', 'a') as file:
                        file.write(f'{name_person:<20}{"Age:":<5}{age_person:>3}\n')
                    
                    question = input('Do you want to register another user? (Y/N): ').upper()
                    
                    if question == 'Y':
                        continue
                    elif question == 'N':
                        break
                    else:
                        print('Invalid option. Please try again.')
                
                print('Registration completed.')
                sleep(2)

                os.system('cls' if os.name == 'nt' else 'clear')
                print(visual.menu_principal_visual())
        
            elif p == 3:
                print('\033[1;34mExiting...\033[0m')
                sleep(1)
                break
if __name__ == "__main__":
    main()