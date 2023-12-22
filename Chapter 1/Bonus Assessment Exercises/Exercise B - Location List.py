#given list of locations
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

#display the original list and its length
print("\nOriginal list: ", locations, "\n")
print("\nLength of the list", len(locations), "\n")

#create a sorted copy of the list and print it
sortedlist = sorted(locations)
print("\nSorted list in alphabetical order: ", sortedlist, "\n")
#display the original list to show it remains unchanged
print("\nOriginal list and original order: ", locations, "\n")

#created a sorted copy of the list in reverse order and print it
reversesortedList = sorted(locations, reverse=True)
print("\nSorted list in reverse alphabetical order: ", reversesortedList, "\n")
#display the original list to show it remains unchanged
print("\nOriginal list and original order: ", locations, "\n")

#reverse the original list in place and print it
locations.reverse()
print("\nReversed List: ", locations, "\n")

#sort the original list in alphabetical order in place and print it
locations.sort()
print("\nSorted list alphabetical order: ", locations, "\n")

#sort the original list in reverse alphabetical order and print it
locations.sort(reverse=True)
print("Sorted List in reversed alphabetical order: ", locations, "\n")