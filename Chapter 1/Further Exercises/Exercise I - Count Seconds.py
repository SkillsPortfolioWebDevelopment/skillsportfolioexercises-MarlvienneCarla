try:
    #get user input for the number of days as a float
    days = float(input("\nEnter number of days: "))

#convert days to hours, minutes, and seconds
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

#display the conversation result
    print(f"{days} days is equal to {seconds} seconds")

except ValueError:
    #handle the case where tghe user enters an invalid input
    print("Invalid please try again.")