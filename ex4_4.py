# def lookup_key(data, value):
        
#     dct = {str(i): i for i in range(5)}
#     for value in dct.values():
#         print(f"data{data}", f"val{value}")
        
# lookup_key([3, 2], [7, 5])


# def lookup_key(data, value):
        
#     dct1 = {str(i) : i for i in range(10)}
    
#     print(dct1)   

#     print(f"data{data}", f"val{value}")

# lookup_key([3, 2], [7, 5])



def lookup_key(data, value):
    result = []
    for k, v in data.items():
        if value == v:
            result.append(k)
    return result
lookup_key("'key1': 1", "'key2': 2", "'key3': 3", 'key4': 4")