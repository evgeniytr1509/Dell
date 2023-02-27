# Модуль 4. Коллекции. Методы

lst1 = [i for i in range (10)]
lst1.append(1) #добавление в список
print (len(lst1))

lst2 = [[], []]
for i in range(10):
    lst2[0].append(i) #добавление в вложенный список
print (lst2)

print (lst2[0][3])
print ("*******")
lst2d = [[2, 3, 4],
        [6, 7, 8],
        [8, 9, 0]]

print (lst2d [0][0])
print (lst2d [1][1])

print ("*****")
lst3 = [i for i in range(10)]
print (lst3)
lst3.clear()
print (lst3)

print (lst3.clear()) #очистка, вывод None
print (lst3) # вывод пустого списка

print("*********")

lst4 = [i for i in range(10)]
lst4.remove(4) # удаление значения
print (lst4)

lst5 = [i for i in range(100, 110)]
print (lst5.pop(5)) # удаляет 5й элемент
print (lst5)

for i in range(10):
    print(lst4.pop(2)) #удаление первых двух элементов

lst6 = [10, 20, 30]
lst2.extend(lst3) # расширение списка
print (lst2)

lst7 = ["a", "b", "c", "a"]
print(lst1.count("a")) # подсчет букв в списке


print (lst3 + lst3)

print(lst2.append(lst6.pop()))
print (lst2)

lst6.insert(1, 40)
print (lst6) # вставка по индексу

lst6.insert(-1, 40)
print (lst6) # вставка по индексу первый с конца

lst1.reverse() # реверс списка