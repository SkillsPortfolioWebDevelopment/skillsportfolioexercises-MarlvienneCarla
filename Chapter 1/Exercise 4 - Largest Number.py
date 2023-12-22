#ask the user for 3 numbers
no1 = int(input("Enter what number you want: "))
no2 = int(input("Enter what number you want: "))
no3 = int(input("Enter what number you want: "))

#check which of the three numbers is the largest using these functions
if no1 >= no2 and no1 >= no3:
    largest = no1
elif no2 >= no1 and no2 >= no3:
    largest = no2
else:
    largest = no3

#idsplay the largest number using an f string
print(f"The Highest Number is : {largest}")
