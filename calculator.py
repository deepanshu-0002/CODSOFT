print("===== SIMPLE CALCULATOR =====")

while True:
    num1 = float(input("Enter First Number: "))
    operator = input("Enter Operator (+, -, *, /): ")
    num2 = float(input("Enter Second Number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error! Division by zero is not allowed.")
            continue
    else:
        print("Invalid Operator!")
        continue

    print("Result =", result)

    choice = input("Do you want to calculate again? (y/n): ")
    if choice.lower() != "y":
        print("Calculator Closed.")
        break