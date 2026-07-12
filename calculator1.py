print("Quick Text Calculator ")
print("Type your math problem (e.g., 5 + 3 * 2). Type 'exit' to quit.\n")

while True:
    user_input = input("Enter expression: ")
    
    if user_input.lower() == 'exit':
        print("Thankyou for using !")
        break
        
    try:
        # Evaluates the mathematical string instantly
        result = eval(user_input)
        print(f"Result: {result}\n")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.\n")
    except Exception:
        print("Error: Invalid mathematical expression.\n")