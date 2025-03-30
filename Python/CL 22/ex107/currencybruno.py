# Create a module called moeda.py that contains the functions increase(), decrease(), double(), and half().

def increase (a, b):
    """
    a = Total amount 
    b = increase amount 
    t = Total amount + increase amount 
    """
    t = a + (a*(b/100))
    return t

def decrease(a, b):
    """
    a = Total amount 
    b =  amount 
    t = Total amount - b = Discount amount
    """
    t = a - (a*(b/100))
    return t

def double(num):
    """
    num = The amount inputed
    t = The amount inputed x 2
    
    """
    t = num *2
    return t

def half(num):
    """
    num = The amount inputed
    t = The amount inputed / 2
    
    """
    t = num/2
    return t