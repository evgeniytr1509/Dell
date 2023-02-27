#словари
#четные / нечетные
lst = [i for i in range(10)]

def odd_even(lst):
    result = {"odd": [], "even":[]}
    for i in lst:
        if i % 2 ==0:
            result ["even"].append(i)
        else:
            result["odd"].append(i)
    return result

if __name__ == "__main__":
    print (odd_even(lst))


dct = {"Bill":"123456", "Jill": "45645646"}

def find_contact(dct, number):
    result = []

    for name, phone in dct.items():
        if str(number) in phone:
            result.append((name, phone))
    return result

if __name__ == "__name__":
    print (find_contact(dct, "5"))


