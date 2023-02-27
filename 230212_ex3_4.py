
def format_ingredients(items):
    print (items)
    array_prod = items.split(",")
    print (array_prod)
    #del array_prod [1]
    #array_prod.pop(1)
    str = " ".join(array_prod)
    str1 = str.replace(",", " ")
    str2 = str1.replace(" and", " ")
    print (str2)

    #print (str)
    # img_array = ['01.jpg', '0201.jpg', '023401.jpg', '2945.jpg', '02.jpg', '5485.jpg']
    # img_str = " ;".join(img_array)
    # print (img_str)

format_ingredients("2 eggs, 1 liter sugar, 1 tsp salt and vinegar")
