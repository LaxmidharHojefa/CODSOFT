# Simple Calculator with Continuous Operations

def add(x, y):
    """This function adds two numbers."""
    return x + y

def subtract(x, y):
    """This function subtracts two numbers."""
    return x - y

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def divide(x, y):
    """This function divides two numbers."""
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero is not allowed."

def calculator():
    """Main calculator function to handle user input and perform operations continuously."""
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # User can input multiple numbers for a global calculation
        while True:
            try:
                next_num = float(input("Enter another number (or type 'done' to stop): "))
                operator = input("Choose operation (+, -, *, /): ")

                if operator == '+':
                    num1 = add(num1, next_num)
                elif operator == '-':
                    num1 = subtract(num1, next_num)
                elif operator == '*':
                    num1 = multiply(num1, next_num)
                elif operator == '/':
                    num1 = divide(num1, next_num)
                else:
                    print("Invalid operator. Please choose +, -, *, or /.")
                    continue

                print(f"Result: {num1}")
            except ValueError:
                break

        choice = input("\nDo you want to continue with a new calculation? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
