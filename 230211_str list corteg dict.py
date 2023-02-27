












def prepare_data(data):
    datas = data
    print (f"{datas} data")
    sort_data = sorted(datas)
    print (f"{sort_data} sort")
    del sort_data [0] # удаление первого элемента
    print (f"{sort_data} data del first")
    sort_data.pop() # удаление последнего элемента
    print (f"{sort_data} data del first last")
    return (sort_data)
    print (sort_data)
prepare_data([4, 1, 2, 3, 7, 6, -10, 0, -10, -10, 7]) 
