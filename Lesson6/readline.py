fd = open('d:\\test2.txt')
data = fd.readlines()
fd.close()
print (data)

fd = open('d:\\test3.txt')
line = fd.readline()
while line:
    print (line)
    line = fd.readline()
#data = fd.readline()
fd.close()

print("*********")
fd = open('d:\\test3.txt')
line = fd.readline()

print (line)
print (fd.tell()) #tell - позиция 
line = fd.readline()
print (line)
print (fd.tell())
#data = fd.readline()
fd.close()
