fd = open('d://test2.txt')
data = fd.read().split('\n')
print (data)
fd.close()

fd = open('d://test2.txt')
data = fd.read().split('\n')
print (type(data))
print (data)
fd.close()
for ch in data:
    print (ch)

print (type(data))

