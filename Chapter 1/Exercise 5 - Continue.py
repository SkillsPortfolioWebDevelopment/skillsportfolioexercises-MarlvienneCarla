#initialize a counter for the number of times the loop lasts
count = 0

#create an infinite loop
while True:
    #ask the user if they will continue by typing Y for yes and N for No
    user = input("Do you want to continue? Y or N \n").strip().upper()

    #check if the user put 'Y'
    if user == 'Y':
        count += 1
    #check if the user put 'N'
    elif user == 'N':
        #if 'N' is entered, its break out of the loop
        break
    else:
        print("Please choose Yes or No")

#display the number of times the loop ran
print(f"The loop last {count} times.")