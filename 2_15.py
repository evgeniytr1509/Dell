operator = None
operand = None
result = None
wait_for_number = True

while True:
    user_input = input(f"{"take a operand" if wait_for_number else "take a operator"} >>>")
    if user_input == "=":
        print(result)
        break
        
    if wait_for_number:
        try:
            operand = int(user_input)
            wait_for_number = False
        except ValueError:
            print(f"{user_input} not a nomber")
            continue
        if not result:
            result = operand
            operant = None

    else:
        if user_input in ("+", "-", "*", "/"):
            operand=user_input
            wait_for_number = True
        else:
            print (f"{user_input} not operator")
            continue
    
    if operand:
        if operator == "+":
            result += operand