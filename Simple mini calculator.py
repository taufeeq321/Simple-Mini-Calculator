# ~~~ Simple Mini Calculator ~~~

num1 = float(input("Enter your number: "))
op = input("Enter the operator (+, -, *, /): ")
num2 = float(input("Enter your second number: "))

if op == '+':
    print("The sum of the given two numbers is", num1 + num2)

elif op == '-':
    print("The difference of the given two numbers is", num1 - num2)

elif op == '*':
    print("The multiplication of the given two numbers is", num1 * num2)

elif (op == '/') and (num2 != 0):
    print("The division of the given two numbers is", num1 / num2)

elif (op == '/') and (num2 == 0):
    print("A number can't be divided by zero")

else:
    print("Invalid operator. Please choose from +, -, *, /")