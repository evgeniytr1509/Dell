
def format_string(string, length):
    string_lenght = 0
    
    # определение длины исходной строки тест1 18симв, тест2 4симв
    for i in string:
        string_lenght = string_lenght+1
    
    if string_lenght >= length: #1 18>12 
        string = string # новая строка возвращается в исходную
    

    elif string_lenght < length:  #2 4<15
        quantity_spase = (length - string_lenght) // 2 #(15-4)/2=5
        #new_string = string
        #text = (" ")
        #quantity_spase=quantity_spase
        print (f'{" " * quantity_spase}{string}')
        #print (text * quantity_spase,string)
    
    #print (string)
    #print (string_lenght)
    #if  string_lenght < length: print (text * quantity_spase, string)
    #if  string_lenght < length: print (quantity_spase)

format_string('abaa', 15)
