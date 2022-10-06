#Calculator SOTC

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
sign = input("Enter the operation [+, -, *, /]: ")

if sign == "+":
    print("Addition is = ", num1 + num2)
elif sign == "-":
    print("Subtracton is = ", num1 - num2)
elif sign == "*":
    print("Multiplication is = ", num1 * num2)
elif sign == "/":
    print("Division is = ", num1 / num2)
else:
    print("Choose correct Operator")
