while True:
    num1 = float(input("What is your first number?: "))
    oper = input("What is your operation? (+, -, *, /, **[exponent], %[remainder]): ")
    num2 = float(input("What is your second number?: "))
    x = 0
    if  oper != "+" and oper != "-" and oper != "/" and oper !="*" and oper != "**" and oper != "%":
        print("Please enter a valid operator")
    elif oper == "/" and num2 == 0 or oper == "%" and num2==0:
        print("You cannot divide by zero.")
    elif oper == "+":
        x = num1 + num2
        print(num1, oper, num2, "=", x)
    elif oper == "-":
        x = num1 - num2
        print(num1, oper, num2, "=", x)
    elif oper == "*":
        x = num1 * num2
        print(num1, oper, num2, "=", x)
    elif oper == "/":
        x = num1 / num2
        print(num1, oper, num2, "=", x)
    elif oper == "**":
        x = num1 ** num2
        print(num1, oper, num2, "=", x)
    elif oper == "%":
        x = num1 % num2
        print(num1, oper, num2, "=", x)
