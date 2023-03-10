#Ключ - tuple из двух номеров точек (первый номер всегда меньше)
#Значение - расстояние между точками, указанными в ключе
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    #Общая дистанция. Если в списке координат одна точка или он пустой, то дистанция нулевая.
    #Цикл. Начиная со второй точки маршрута.
    #Если точка одна, или их нет то в цикл не выполняется и функция прекращает работу
    #ends - tuple, в котором хранятся номера двух точек - точки, в которой находится дрон (i-1) и следующую точку маршрута.
    #временно создается tuple так, чтобы первый номер всегда был меньше, чем второй.К дистанции добавляется значение из points с этим ключем.
    distance = 0.0
    for i in range(1, len(coordinates)):
        ends = (coordinates[i-1], coordinates[i])
        
        distance += points[(min(ends), max(ends))]
    print (distance)
calculate_distance ([0, 1, 3, 2, 0])


