# take the input operation form user
# take 2 numbers from user
# perform the operations as per the user input (addition, subtraction, multiplication, division) through if else statements
# print the result of the operation


print("Welcome to the Calculator!")
op = input("Please select an operation: (+, -, *, /)")
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

if op == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")

elif op == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")

elif op == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")

elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")