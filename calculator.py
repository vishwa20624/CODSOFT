def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("Select operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Enter choice (a/b/c/d): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 'a':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == 'b':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == 'c':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == 'd':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")
