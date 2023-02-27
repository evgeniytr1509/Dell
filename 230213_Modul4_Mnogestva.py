# Множества. Коллекция, в которой хранятся только уникальные значения несортированные.
# используется для определиния наличия повторов
my_set = set("hello")
print (my_set)

set1 = set("hello")
set2 = set("aloha")
print(set1 and set2)

print(set1 & set2)
print(set1 | set2) # вывод того что есть и в 1м и в 2м

if len("hello") != len(set("hello")):
    print ("double")

print (set1 ^ set2) # уникальные