# match_case_calculator.py

# Prompt the user for the first and second numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation the user wants to perform
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()
        result = num1 / num2
    case _:
        print("Invalid operation.")
        exit()

# Output the result
print(f"The result is {result}.")
