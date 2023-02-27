# Список
lst = []
lst1 = [1, 2, 3, 4]
lst2 = list()
lst3 = [i for i in range(10)]

print (lst)
print (lst1)
print (lst2)
print (lst3)

#lst3.clear()# очистил
print (f"slt3 - {lst3}")
num_one = lst3[1]
print (num_one)

for i in lst3:
    print (i)

word = "Hello" # слово записать в кортеж
lst_chr = []
for i in word:
    lst_chr.append(i)
print (lst_chr)


lst5 = [i for i in range(10)]
lst5.remove(7) # удалило по значению 3
print (lst5)


lst5.insert(1, "D") # вставить символ
print (lst5)

lst5.insert(100, "F") # вставить символ drjytw
print (lst5)

lst5.extend("Wre") # расширение в конец
print (lst5)

lst5 += "World" # прибавление
print (lst5)