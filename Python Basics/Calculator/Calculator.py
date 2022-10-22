#Number Calculator SOTC

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
indication = input("Enter the operation [+, -, *, /]: ")

if indication == "+":
    print("Addition Result of two numbers is: ", num1 + num2)
elif indication == "-":
    print("Subtracton Result of two numbers is: ", num1 - num2)
elif indication == "*":
    print("Multiplication Result of two numbers is: ", num1 * num2)
elif indication == "/":
    print("Division Result of two numbers is: ", num1 / num2)
else:
    print("Choose correct Operator : ")
