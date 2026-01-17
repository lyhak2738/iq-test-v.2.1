num1 = int(input("enter the first numer: "))
operation = input("enter the operation (+, -, *,or /): ")
num2 = int(input("enter the second numer: "))
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "error: invalid operation"
print("the result is:", result)
