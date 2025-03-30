def increase (a, b, cur=True):
    t = a + (a*(b/100))
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t
    

def decrease(a, b, cur=True):
    t = a - (a*(b/100))
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t

def double(num, cur=True):
    t = num *2
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t

def half(num, cur=True):
    t = num/2
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t

def format_currency (num):
    
    ff= f'{num:,.2f}'
    fff=ff.replace('.','x').replace(',','.').replace('x',',')
    return fff

def current_resume (a,b,c):
    """
    a = Price

    b = discount

    c = increase
    """
    p = format_currency(a)
    db = double(a)
    hf = half(a)
    dc = decrease(a, b)
    ic = increase(a, c)
    
    print('---'*12)
    print(f'{'Prices':^36}')  # Centered title
    print('---'*12)
    print(f'Original Price: {'€':>13}{p}')
    print(f'Double Price: {'€':>15}{db}')
    print(f'Half Price: {'€':>17}{hf}')
    print(f'{b}% discount Price:{'€':>10}{dc}')
    print(f'{c}% Increase Price:{'€':>10}{ic}')
    print('---'*12)

