#use a for loop to unterate through numbers from 1 to 100
for num in range (1, 101):
    #check if the number is divisable by both 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    #check if the number is divisible by 3
    elif num % 3 == 0:
        print("Fizz")
    #check if the number is divisible by 5
    elif num % 5 == 0:
        print("Buzz")
    else:
        #if none of the above conditions are met, dipslay num 
        print(num)