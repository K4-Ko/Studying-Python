import menu_visual1.visual as visual

def option_menu (msg):
    
    while True:
        n = input(msg)  
        try:
            n = int(n)
            if n >= 1 and n <= 3:
                return n 
            else:
                raise ValueError
        except:
            print(visual.print_error_temp())