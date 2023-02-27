# Модуль 4. Коллекции. Срезы

lst1 = [str (i) for i in range(10)]

print(lst1[0:9:2]) # вывод с шагом 2, списком
print(lst1[0:9])# вывод всех, списком

print (lst1[::-1])# вывод реверсом
lst2 = lst1
print (lst2)