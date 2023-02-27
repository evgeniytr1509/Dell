def cost_delivery(quantity, *args, discount=0) -> float:
    
    sum = 5 #доставка товара 1
    for i in range(quantity-1): #доставка товара 2, 3 .... 
        sum = sum + 2
    #result = sum
    #return result

    if discount == 0:
        result = sum

    else:
        result = sum * discount

    
    return result
    
    return (cost_delivery( discount)) 
cost_delivery 