def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("=== Simple Calculator ===")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit")

    while True:
        choice = input("\nEnter operation (+ - * /) or exit: ").strip()

        if choice.lower() == "exit":
            print("Exiting Calculator. Goodbye!")
            break

        if choice not in ["+", "-", "*", "/"]:
            print("Invalid operation. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "+":
            print("Result:", add(num1, num2))
        elif choice == "-":
            print("Result:", subtract(num1, num2))
        elif choice == "*":
            print("Result:", multiply(num1, num2))
        elif choice == "/":
            print("Result:", divide(num1, num2))

if __name__ == "__main__":
    main()
