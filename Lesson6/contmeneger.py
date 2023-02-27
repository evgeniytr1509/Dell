# файловый дискриптор
fh = open('d://test3.txt')

# with open('d://test3.txt') as fd:
#     print (fd.readlines())

# with open('d://test3.txt', 'w') as fd:
#     print (fd.writelines())

# режим байт
with open('d://1-1.png', 'rb') as fd:
    data = fd.read()
print(f"размер в байтах {len(data)}")

with open('d://ABBA - Happy New Year.mp3', 'rb') as fd:
    data = fd.read()
print (f"данные мр3 {data}")

with open('d://ABBA - Happy New Year.mp3', 'rb') as fd:
    data = fd.read()
bytearray = data[:10]
print (bytearray.decode('utf-8'))