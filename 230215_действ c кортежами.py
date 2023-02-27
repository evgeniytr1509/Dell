a = 1, 3, 4, 4, 4, [1, 3, 4], "hello", "hello", "hi", 
c = 5, 8, 9
b = tuple(a)
print (b, type(b))
print (a)
print (len(a))
print (2 in a)
print (a + c)
print (a*2)
#print (min (a))
#print (sum(a))
d = a.count(4) #подсчет єлементов в кортеже
e = a.count("hello")
print (d)
print (e)
g=float(d+e)
print (g)
print (a[5])
a[5].append (100) # добавление в список, которій в кортеже
print (a)
