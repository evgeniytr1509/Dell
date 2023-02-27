f = int(input("Ввести число: "))
def fact(num):
    if num == 0:
        print (1)
        return 1
    else:
        print (num)
        return num * fact(num-1)
print (f"factorial {f}: %s" % fact(f))