# функция суммы чисел 
from random import randint
def all_sum(*args):
    result = 0
    for i in args:
        result += i
    return result

#print (all_sum(*[radint(10, 100) for _ in range (100)]))
print (all_sum(100, 200, 300, 5000, 5))

