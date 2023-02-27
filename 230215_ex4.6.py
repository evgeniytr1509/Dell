def split_list(grade):
    average = sum(grade)/len(grade)
    print (f"{average} - среднее значение" )
    grade1 = []
    grade2 = []

    for i in range (len(grade)):
        if float (grade [i]) <= average:
            grade1.append(grade[i])
        elif float (grade [i]) > average:
            grade2.append(grade[i])
    
    print (grade)
    print (grade1)
    print (grade2)
    return (grade)
    return (grade1)
    return (grade2)

    
split_list([5,10,8,7,5])
