# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the mathematical operation (+, -, *, /): ")

# Perform the operation
result = 0.0
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")

# Print the result
print(f"{num1} {operation} {num2} = {result}")
