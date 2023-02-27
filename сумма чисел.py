

def find_average(*numbers):
    result = 0
    count = 0
    if not numbers:
        return result

    for i in numbers:
        if isinstance (i, list):
            for k in i:
                result +=k
                count +=1
        else:
            result += i
            count += 1
    return result/count
print(find_average([3, 3, 3], 3)) 