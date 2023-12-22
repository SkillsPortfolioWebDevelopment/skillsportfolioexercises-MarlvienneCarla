#define a list of numbers
ownList = [6, 3, 9, 13, 2, 9, 4, 7, 6, 4]

#display a message to undicate the list of elements
print("\nList of elements: \n")
#iterate through the elements n the list and print each element with a space in between
for items in ownList:
    print(items, end=" ")
print()

#find and display the highest and lowest values in the list
highest = max(ownList)
lowest = min(ownList)
print(f"\nHighest value: {highest}\n")
print(f"\nLowest value: {lowest}\n")

#sort the list in ascending order
ownList.sort()
print("\nSorted list in ascending order: ", ownList, "\n")

#sort the list in descending order
ownList.sort(reverse=True)
print("\nSorted list in descending order: ", ownList, "\n")

#append two elements to the list
ownList.append(11)
ownList.append(0)
print("\nList after appending two elements: ", ownList, "\n")