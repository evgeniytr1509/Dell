"""List"""
lst = []
lst1 = [1, 2, 3, 4]
lst2 = list()
lst3 = [str(i) for i in range(1, 10, 2)]

print(lst)
print(lst1)
print(lst2)
print(lst3)

# lst3.clear()

number_one = lst3[1]

print(f'element_1 - {number_one}')

for i in lst3:
    print(i)

word = "Hello World"

lst_chr = []

for i in word:
    lst_chr.append(i)

print(lst_chr)

lst3.remove('3')

print(lst3)

lst3.insert(1, 'D')

print(lst3)

lst3.insert(100, 'F')

print(lst3)

lst3.extend("Hello")

print(lst3)

lst3 += "World"

print(lst3)