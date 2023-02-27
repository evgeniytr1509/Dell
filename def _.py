def f (*args): # чиса упаковываются в переменную args в виде кортежа неизменного (1,2,3,4,5,6) * для упаковки чисел
    sum=0
    for i in args: #цикл обходит элементы кортежа по значениям
        sum = i + sum
    return sum
print (f(1, 2, 3, 4, 5, 6))

# передача в функцию именованых объектов в неограниченном количестве, упаковывается в словарь
def f(**kwards):
    for k,v in kwards.items():
        print(k,v)
f (a=1, b=5, c=6, name=67)

# комбинация. первые значения в виде кортежа, потом именованые параметры, которые упаковываються в словарь
def f(*args, **kwargs):
    print(args,kwargs)
f (5, 4, 9, 1, a=1, b=5, c=6, name=67)

# 333333333333
def outPrint(*args, sep="#", end="@"):
    print(args,sep,end)
outPrint (5, 4, 9, 1, sep="67")
outPrint (1, 2) # 

a = [1, 2, 6, 6]
print (a) # вывод кортежа
print (*a) #* распаковака