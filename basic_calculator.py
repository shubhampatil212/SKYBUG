def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Not Defined!"

print("Select operation:")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

user_choice = input("Enter choice (1/2/3/4): ")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

if user_choice == '1':
    print(number1, "+", number2, "=", addition(number1, number2))
elif user_choice == '2':
    print(number1, "-", number2, "=", subtraction(number1, number2))
elif user_choice == '3':
    print(number1, "*", number2, "=", multiplication(number1, number2))
elif user_choice == '4':
    print(number1, "/", number2, "=", division(number1, number2))
else:
    print("Invalid input")
