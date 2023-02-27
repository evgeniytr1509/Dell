while True:
    num = int(input("Введите число: "))
    if num < 18:
        result = "Вам нужно учиться. "
    elif num >= 18 and num < 50:
        result = "Вам нужно работать. "
    elif num >= 51 and num < 59:
        result = "Вы скоро станете пенсионером. "
    elif num >= 60 and num < 110:
        result = "Вы пенсионер. "
    else:
        result = "Вы долгожитель!"
    print(result)