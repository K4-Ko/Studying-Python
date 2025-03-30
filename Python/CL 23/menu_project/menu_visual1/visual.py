import time

def menu_principal_visual ():
    print('-'*45)
    print()
    print('''
    ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
    ████╗ ████║██╔════╝████╗  ██║██║   ██║
    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝
    ██║ ╚═╝ ██║███████╗██║ ╚████║ ╚████╔╝ 
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  
    ''')
    print('-'*45)
    print(f'\033[1;33m{1}\033[0m - \033[1;34mCheck register\033[0m \n\033[1;33m{2}\033[0m - \033[1;34mRegister a new user\033[0m \n\033[1;33m{3}\033[0m - \033[1;34mExit\033[0m')
    print('-'*45)
    return ''

def print_error_temp():
    """
    Shows a temp error message and delete it's self

    """
    print('\033[1;31mThis option is not valid !\033[0m')
    time.sleep(1)
    print('\033[1A\033[K')
    return ''

def print_option1():
    print('-'*45)
    print(f'\033[1;34m{"Option 1":>24}\033[0m')
    print('-'*45)
    return ''

def print_option2():
    print('-'*45)
    print(f'\033[1;34m{"Option 2":>24}\033[0m')
    print('-'*45)
    return ''

