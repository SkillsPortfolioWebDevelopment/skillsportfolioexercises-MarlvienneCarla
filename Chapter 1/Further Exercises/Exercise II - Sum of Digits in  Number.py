try:
    #get user input for a number as an integer
    number = int(input("\nPlease enter a number: "))
    #initialize a varidale to store the sum of digits
    digitS = 0

    #process each digit in the number using a while loop
    while number> 0:
        #extract the last digit of the number
        digit = number % 10
        #add the digit to the sum
        digitS += digit
        #remove the last digit from the number
        number //= 10
    #print the toal sum of digits
    print(f"The total is: {digitS}")
except ValueError:
    #print when the user enters an invalid input
    print("Invalid please try again.")