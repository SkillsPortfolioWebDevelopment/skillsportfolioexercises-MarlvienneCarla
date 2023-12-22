#display a greeting message
print("Hello, I would like to know you")

#ask the user for their full name and age
fullName = input("\nEnter your full name:\n")
realAge = input("\nHow old are you?\n")

#display a welcome message using the user's info
print("\nIt is good to meet you, " + fullName.title())
print("\nThe length of your name is " + len(fullName))
print("\nYou will be " + (realAge + 1))