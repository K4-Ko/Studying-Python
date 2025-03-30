def increase (a, b, cur=True):
    """
    a = Total amount 
    b = increase amount 
    t = Total amount + increase amount 
    """
    t = a + (a*(b/100))
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t
    

def decrease(a, b, cur=True):
    """
    a = Total amount 
    b =  amount 
    t = Total amount - b = Discount amount
    """
    t = a - (a*(b/100))
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t

def double(num, cur=True):
    """
    num = The amount inputed
    t = The amount inputed x 2
    
    """
    t = num *2
    if cur: 
        tt =f'{t:,.2f}'
        format_t = tt.replace('.','x').replace(',','.').replace('x',',')
        return format_t
    else:
        return t

def half(num, cur=True):
    """
    num = The amount inputed
    t = The amount inputed / 2
    
    """
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