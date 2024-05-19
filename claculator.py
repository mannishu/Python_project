def calculaor(num1,num2,operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif num2 == "0":
        print("Error: Devision by Zero is not allowed.")
        return None
    else:
        print("Error: Invalid Operator. Use +,-,*,/.")
        return None
    

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))
operator = input("Choose an operator (+,-,*,/): ")

print("Result is: ",calculaor(num1, num2, operator))

    
