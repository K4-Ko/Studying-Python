#Create a program with a function called grade(), which can receive multiple student grades 
# and return a dictionary containing the following information:

def grade(*num,**kwargs):
    """
    
    dc['Highest grade'] = high = max(l) : Shows the Highest grade
    dc['Lowest grade'] = low = min(l): Shows the Lowest grade
    dc['Number of grades'] = Shows the amout of grades
    dc['Class average'] = Shows the average


    """
    l = list(num)
    dc = {}
    print(l)
    # – Highest grade
    dc['Highest grade'] = high = max(l)
    # – Lowest grade
    dc['Lowest grade'] = low = min(l)
    # – Number of grades
    dc['Number of grades'] = grade_amount = len(l)
    # The sum of the grades
    g = 0
    for x in l:
        if g == 0:
            g = x
        else:
            g = g + x
    print(g)
    # – Class average
    dc['Class average'] = clas = g/len(l)

    # – Situation (optional)
    
    if kwargs.get('st') == True:
        sit = ''
        
        if clas > 6:
            dc['Class average'] = 'Approved'
        
        elif clas <6 and clas >5:
            dc['Class average'] = 'Pending'
        
        else:
            dc['Class average'] = 'Not Approved'
    else:
        del dc['Class average']

    print(dc)


x = grade(5,4,3,2,1,st=True)

