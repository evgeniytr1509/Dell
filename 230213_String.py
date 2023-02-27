#Строки

my_str = "Hello"
print(my_str[1])
#my_str[1] = "b"
print(my_str[1:3])

new_str = " "

for i in my_str:
    if i == "e":
        new_str = new_str + "b"
    else:
        new_str += i
print (new_str)