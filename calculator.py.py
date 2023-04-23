while True:
    operator = input("Select operator exit[x] :/n +, -, /, //, *, ^: ")
    if operator.lower() == "x":
        print("Thanks for checking in!")
        break
    num1 = input("Enter number: ")
    num2 = int(input("Enter number: "))
    if operator == "+":
            print(int(num1) + num2)
    elif operator == "-":
            if num1 > num2:
                print(int(num1) - num2)
            else:
                print(int(num2) - num1)
    elif operator == "/":
        print(int(num1)/num2)
    elif operator == "//":
        print(int(num1)//num2)
    elif operator == "*":
        print(int(num1)*num2)
    elif operator == "^":
        print(int(num1)**num2)
    else:
        None