# # читает существующий файл
# fd = open('d:\\test.txt')
# print (fd.read())
# fd.close()

# открывает файл для записи, если его нет ошибка
# fd = open('d:\\test1.txt', 'x')
# print (fd.read())
# fd.close()

# создает новый файл. если с w перезаписывает существующий
fd = open('d:\\test2.txt', 'w')
fd.write('Hello from python1')
fd.close()

# читает указанный файл. если с r 
fd = open('d:\\test2.txt', 'r')
print (fd.read())
fd.close

# читает указанный файл. и добавляет в конец (append)
fd = open('d:\\test2.txt', 'a')
fd.write('Hello world')
fd.close

# стирает 
fd = open('d:\\test2.txt', 'w+')
fd.write('adsad')
fd.seek(5) # 0 - положение курсора. 0 позиция курсора
print(fd.seek(5))
print (fd.read())
fd.close









