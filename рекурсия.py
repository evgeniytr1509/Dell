

def fnc(n):
    if n == 3: # первая условие не сработало, второе сработало
        return 3 # возврат 3 
    return fnc(n-1) + n # самомвызов функции
print (fnc(5))