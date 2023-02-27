result = None
operand = None
operator = None
wait_for_number = True

while True:
    
    if wait_for_number == True:
        operand = input("ввести число >>>")
        try:
            number = int(operand)
            wait_for_number = False

        except ValueError:
            print(f"{operand} не число")
            continue
        if result == None:        
            result = operand

        else:
            result = eval(result + operand)
            result = str(result)

    else:
        operator = input ("ввести оператор")
        
        if operator in ("+", "-", "*", "/"):
            
            result += operator   
            wait_for_number = True
        elif operator == "=":
            result = int(float(result))
            break
            
            
        else:

            print(f"{operator} не оператор")

