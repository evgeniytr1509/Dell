# https://www.youtube.com/watch?v=HPw8JEWsDOQ
# кортеж
# к. это списки, значения которых можно только читать, менять нельзя 
# к. записывают в круглых скобках(), списки в []
sp1 = ("eggs", "orage", "sugar", "salt", "vinegar")
print (sp1)
print (sp1[2])
print (sp1[2:])

# словари
# например словарь иностранного языка, поиск слова по ключу
s1 = {"ключ" : "значения", "яблоко" : "яблоня", "груша" : "грушевое дерево", "банан" : "пальма"}
print (s1)
print (s1["груша"]) # вывод слова по ключу

s1 ["двигатель"] = "машина" # добавление нового слова в словарь
print (s1)

s1["груша"] = "высокое грушевое дерево" # замена слова в словаре
print (s1)

del s1["груша"]# удаление слова из словаря
print (s1)