#given list of staffs 
staff = ["Arshiya", "Usman", "Iftikhar", "Usman","Rafia", "Mary", "Anmol","Zainab","Iftikhar", "Arshiya","Rafia","Jake"]

#dictionary to store the count of each staff member
itemC = {}

#loop through each item in the staff list
for item in staff:
    #check if the item is already in the dictionary
    if item in itemC:
        #if yes, increment the count
        itemC[item] += 1
    else:
        #if not, add the iteam to the dictionary with a count of 1
        itemC[item] = 1

#print the current state of the item counts dictionary
    for item, count in itemC.items():
        print(f"{item}: {count} times")