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

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    while True:
        print("\n====== Simple Calculator Menu ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Modulus")
        print("7. Exit")

        choice = input("Choose an operation (1-7): ")

        if choice == '7':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input. Please enter numbers.")
                continue

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))
            elif choice == '6':
                print("Result:", modulus(num1, num2))
        else:
            print("❌ Invalid choice. Please select a number between 1 and 7.")

calculator()