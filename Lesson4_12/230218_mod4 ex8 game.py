def game(terra, power):
    
    for alone_list in terra:
        for index, element in enumerate(alone_list):
            if power >= element:
                power += element
            elif element > power:
                break
    print (power)
    return power
    

game([[1,2,6], [2,3,8], [3,7,8]], 1)