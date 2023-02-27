name = "avril lavigne"
print(name.title())  # Avril Lavigne - первая буква большая

name = "avril lavigne"
print(name.upper())  # AVRIL LAVIGNE - все буквы большие

name = "Avril Lavigne"
print(name.lower())  # avril lavigne - все буквы маленькие

name = "Avril Lavigne"
print(name.startswith('Avr'))  # True - строка начинается с указанного Av

pic = "hello.jpg"
print(pic.endswith("o.jpg"))  # True -  строка заканчиквается  указанного jpg

name = "Avril Lavigne       " "Hello"
print(name.rstrip())  # Avril Lavigne - удалить пропуски у правого края строки

name = "1" "         Avril Lavigne"
print(name.lstrip())  # Avril Lavigne - - удалить пропуски у левого края строки

#https://www.youtube.com/watch?v=TEF-0UXRybg&t=365s
s1="abrakadabranramra"
res = s1.count("ra") # считает количество заданных букв 
print (res)

s2="abrakadabranramra"
res = s2.count("ra", 4) # считает количество заданных букв? поиск начинается с заранного символа
print (res)

s2="abrakadabranramra"
res = s2.count("ra", 4, 11) # считает количество заданных букв? поиск начинается с заранного символа 4 до заданного 11
print (f"from 4 to 11 find' {res} 'times")