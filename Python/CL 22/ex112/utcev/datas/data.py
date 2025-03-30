
def valid(msg):
    
    while True:
        a = str(input(msg)).replace(',','.').strip()
        
        if a.isalpha() or a == '':
            print(f'\033[1;31mERROR {a} is invalid number\033[m')
        else:
            return float(a)
       


        # ALSO WORKS:
        # try:
        #     a = float(a)
        #     return a
        
        # except ValueError:
        #     print(f'\033[1;31mERROR {a} is invalid number\033[m')
