# Словари
dct1 = {}
dct2 = dict()

print(type(dct1), type(dct2))

dct1["key1"] = "Value1"

print(dct1)

dct1["key1"] = "Value2"
print(dct1)

# dct3 = {[1, 2]: "list1"}# ошибка т.к. объект изменяемый
# print(dct3)

dct3 = {(1, 2): "list1"}# ошибки нет объект неизменяемый
print(dct3)

dct4 = {str(i): i for i in range(10)} # словарь циклом
print (dct4)

# ключ должен быть стринг
print ("************")

dct5 = {f"key - {i}": i for i in range(10)}
for i in dct5:
        print(f"{i} : {dct5[i]}")

for k, v in dct5.items():
    print (f"{k} : {v}")  

for v in dct5.items():
    print (f"{v}")      