from random import randint
#111111111111111111111111111111111111111111111111111111111111111111111
def get_random_password(a, b):
    password = []
    for i in range (8):
        simb = randint(a, b)
        simb1 = chr (simb)
        password.append(simb1)
    
    print (''.join([ str (i) for i in password]))
    
get_random_password(40, 126)

#22222222222222222222222222222222222222222222222222222222222222222222222
def is_valid_password(password):
# условие 1 Количество цимволов
    l = len(password)
    password = list (password) 
# условие 2 Большие буквы
    count_big = 0
    for symb in password:
        #print (symb)
        b = ord (symb)
        #print (w)
        
        if b >= 65 and b <= 90: 
            count_big = count_big + 1 
    print (f"big- {count_big}")

# условие 3 Маленькие буквы
    count_small = 0
    for symb in password:
        #print (symb)
        s = ord (symb)
        #print (d)
        
        if s >= 97 and s <= 122: 
            count_small = count_small + 1
    print (f"small- {count_small}")    

# условие 4 Цифры   
    count_dig = 0
    for symb in password:
        #print (symb)
        d = ord (symb)
        #print (d)
            
        if d >= 48 and d <= 57: 
            count_dig = count_dig + 1
    print (f"digit- {count_dig}")      
    
    if l == 8 and count_big >=1 and count_small >=1 and count_dig >=1:
        print (True)
        return True
        
    else:
        print (False)
        return False
is_valid_password("b8g^ro4^")


