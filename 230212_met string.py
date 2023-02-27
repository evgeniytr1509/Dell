# Методы в строках
# https://www.youtube.com/watch?v=7gGZDNlge-M
str1 = "Hello world! How are you?"
str1.find("!") # поиск положения єлемента
print (str1.find ("!")) # поиск с левой стороны
print (str1.find ("o"))
print (str1.rfind ("y")) # поиск с правой стороны
print (str1.rfind ("o"))
print (str1.index("!")) # поиск положения стороны
print (str1.rindex("!"))# поиск с правой стороны
str2 = str1.replace("world", "frend") # замена слов
print (str2) 
str3 = str1.replace(" ", "") # удалить пробелы
print (str3) 
str4 = str1.split(" ") # разбить  строку на элементы списка
print (str4) 

str5 = "01.jpg#0201.jpg#023401.jpg#2945.jpg#02.jpg#5485.jpg"
str6 = str5.split("#")# разбить строку на элементы списка c разделителем #. результат массив 
print (str6)


img_array = ['01.jpg', '0201.jpg', '023401.jpg', '2945.jpg', '02.jpg', '5485.jpg']
img_str = " ;".join(img_array)
print (img_str)

print(str1.lower()) # все буквы маленькие
print(str1.upper()) # все буквы бульшие
print(str1.count('o')) # подсчет всех букв о
print(str1.count(' ')) # подсчет всех пробелов
print(len(str1)) # подсчет символов в строке

str11 = "dowАreyou"
print (str11.isalpha()) # возвращает true (строковая (только символы)) или fasle (не строковая (пробелы, знаки, цифры))
str12 = "dowareyou!"
print (str12.isalpha())
str13 = "dowa reyou"
print (str13.isalpha())

str14 = "1234" 
print (str14.isdigit()) # проверка на число. используется при проверке ввода от пользователя 

