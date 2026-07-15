def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def calculator():
    print("=" * 40)
    print("      Oasis Infobyte - Python Task 1     ")
    print("         Simple CLI Calculator           ")
    print("=" * 40)
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        choice = input("Enter choice (1/2/3/4): ").strip()
        if choice in ['1', '2', '3', '4']:
            break
            
        print("Invalid choice! Please select 1, 2, 3, or 4.")

    print("\n" + "-" * 40)
    if choice == '1':
        print(f"Result: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    print("-" * 40)

if __name__ == "__main__":
    calculator()