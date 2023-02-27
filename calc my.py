result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input("ввести данные >>>")
    if wait_for_number == True:
        try:
            number = float(user_input)
            if operator == "+":
                result = number + number
            elif operator == "-":
                result = number - number
            elif operator == "*":
                result = number * number
            elif operator == "/":
                result = number / number
            elif operator == "==":
                print (f"result1 {result}")
            wait_for_number = False
            
        except ValueError:
            print(f"{user_input} not number3")
            continue
    else:
        if user_input in ("+", "-", "*", "/"):
            operator = user_input
            if user_input == "+":
                result = number + number
            elif user_input == "-":
                result = number - number
            elif user_input == "*":
                result = number * number
            else:
                result = number / number
            print (f"result2 {result}")        
            wait_for_number = True
        else:
            print(f"{user_input} not operator")
                
            
                