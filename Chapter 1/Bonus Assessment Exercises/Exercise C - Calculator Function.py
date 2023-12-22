#define a functions to perform addition, subratraction, multiplication, division, and remainder
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return
    return x / y

def remainder(x, y):
    if y == 0:
        return
    return x % y

#main loop for calculator functionality
while True:
    print("\nHello, Welcome! Im your Calculator")
    print("\nPlease Choose: ")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Remainder")

    #get user input for the chose operation
    choice = input("\nEnter the number of your choice: ")

    #validate the user's choice
    if choice not in ('1', '2', '3', '4', '5'):
        print("Invalid please try again.")
        continue
    
    #get user input for thw two numbers
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("\nEnter the second number: "))
    
    #perform the chose operation based on use input
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = remainder(num1, num2)
    
    #display the result of the calculation
    print(f"\nResult: {result}")
    
    #ask the user if they want to perform another calculation
    another_calculation = input("Do you want to perform another calculation?: ")
    #if the user enters anything other than yes, exit the loop
    if another_calculation.lower() != 'Yes':
        break

