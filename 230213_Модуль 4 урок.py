# Модуль 4. Коллекции. Лист
# изменяемые, неизменяемы, 
lst1 = []
lst2 = list ()
print (type(lst1), type(lst2))
lst1 = ["1", 1, lst2]
print (lst1)
print (type(lst1[0])) # обращение по индексу
print ("******")
lst1 = ["1", 10, lst2]
for i in lst1:
    print(type(i))

for i in range (len(lst1)):
    print(lst1[i])

for i in range (len(lst1)):
    print (lst1[i])

#print(lst1[3]) # index error
print (lst1[-2]) # возврат второго с конца элемента из списка


