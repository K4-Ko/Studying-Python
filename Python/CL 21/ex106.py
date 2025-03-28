# Create a mini-system that uses Python's Interactive Help. 
# The user will type a command, and the manual will appear. 
# When the user types the word 'FIM', the program will terminate. 
# Important: use colors.
import pydoc

def lines (txt):
    print('\033[1;30;47m#######'*6)
    print(txt)
    print(('#######'*6) + '\033[m')

def execute ():
    while  True:
        
        n = str(input('\033[1;40;44mType here: [To stop type: stop_now]:      \033[m')).lower()

        
        if 'stop_now' in n:
            break
        
        try:
            help_text = pydoc.render_doc(n)
            print('\033[1;30;47m' + help_text + '\033[m')
        except:
            print('Document not availble')

lines(f'{'-'*16}{'PyHelper'}{'-'*18}')

execute()