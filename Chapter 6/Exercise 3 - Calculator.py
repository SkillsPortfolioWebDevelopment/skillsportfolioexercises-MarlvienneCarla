import operator

def calculator_menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-6) or Q to quit: "))
            if 1 <= choice <= 6:
                return choice
            elif choice == 'Q' or choice == 'q':
                return 'Q'
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6 or Q to quit.")

def get_user_values():
    try:
        value1 = float(input("Enter the first value: "))
        value2 = float(input("Enter the second value: "))
        return value1, value2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None

def perform_operation(choice, value1, value2):
    operations = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul,
        4: operator.truediv,
        5: operator.mod,
        6: max
    }

    operation_function = operations.get(choice)
    if operation_function:
        return operation_function(value1, value2)
    else:
        return None

if __name__ == "__main__":
    while True:
        calculator_menu()
        user_choice = get_user_choice()

        if user_choice == 'Q':
            print("Exiting the calculator. Goodbye!")
            break

        value1, value2 = get_user_values()

        if value1 is not None and value2 is not None:
            result = perform_operation(user_choice, value1, value2)
            if result is not None:
                print(f"Result: {result}")
            else:
                print("Invalid operation. Please choose a valid operation from the menu.")
