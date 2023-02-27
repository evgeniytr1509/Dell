# позиционные аргументы

def sum_int(num1: int, num2: int=10, num3: int|None = None) -> int:
    if num3:
        return num1 + num2 + num3
    result = num1 + num2 + num3
    return result

print (sum_int(1, 20, 300))

# змінна кількість параметрів
a, b, *c, d, e, f = [1, 2, 45, 78, 89] 
print (a,b,c,d,e,f)

a, b, *c = [1, 2, 45, 78, 89] #все что после *с в []
print (a,b,c)

a, b = {"name": "Bill", "phone": "123456"}

print (type (a),(b))

def calc_sum(num1: int=5, *nums, **knums) -> int:
    print(nums)
    result = 0
    for num in nums:
        result += num
    result += num1
    print(knums)

    for _, items in knums.items():
        result += items
    
    return result

nums = [1, 1, 1, 1, 1]

k_nums = {"first":1, "second": 2, "third": 3}
print (calc_sum(5, *nums, **k_nums)) # * распаковка при передачи
