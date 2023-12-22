#use a for loop to iterate through numbers from 1 to 99
for num in range(1,100):
    #check if the nmber us not divisible by 2
    if num % 2 != 0:
        #if its odd, continue to the next iteration of the loop
        continue
    #if the number is even, print it
    print(num)