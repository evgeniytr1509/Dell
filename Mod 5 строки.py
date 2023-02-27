this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string  # True
print (the_same_string)
# вывод в несколько строк
text = """dfjklasdjfklsdjfa;kls
asdfklsdfasdklf
asdfkjas;kljdf;klasd"""
print (text)
print ("**************")
# вывод в одну строку, \ в конце первой и второй строк кода, он 
# указывает интерпретатору игнорировать окончание строки и продолжить сразу со следующей.
one_line = str(1234567899)
            
print (one_line)

str1 = ("spam1 " "eggs") 
str2 = ("spam2 eggs")
print (str1)
print (str2)
# перевод строки
str3 = ("spam3 \n eggs") 
print (str3)
print ("***********")
# перевод строки
str4 = ("spam4 \r eggs") 
print (str4)

# print (one_line.rfind("34"))
# print (one_line.index("43"))
# print (one_line.split("4")) # разбить строку по символу

sentences = ["I am learning strings in Python", "Some new methods got now."]
text = ". ".join(sentences)
print (sentences)
print(text)
sen = "sdasdasdasddasda"
print (sen.split("d")) # разделяет строку на несколько строк по заданному символу
print (sen.replace("a", "*")) # замена

# удаление заданной последовательности
print('TestHook'.removeprefix('Test'))   # Hook
print('TestHook'.removeprefix('Hook'))   # TestHook

# замена
map = {ord('з'): 'z', ord('ю'): ('u')}
translated = 'зю'.translate(map)
print(translated) # zu

for i in range(16):
    s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
    print(s)

# форматирование
width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))