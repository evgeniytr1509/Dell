result = None
operand1 = None
operand2 = None
operator = None
wait_for_number = True
result = float (input ("result: "))
operand1 = float (input ("operand1: "))
operand2 = float (input ("operand2: "))
operator = input ("operator: ")

while True:
    if operator == "+":
        result = float (operand1 + operand2)
        print (result)
        break    
    elif operator == "-":
        result = float (operand1 - operand2)
        print (result)
        break
    elif operator == "*":
        result = float (operand1 * operand2)
        print (result)
        break   
    elif operator == "/":
        result = float (operand1 / operand2)
        print (result)
        break
    else:
        print ("is not '+' or '-' or '/' or '*'. Try again")