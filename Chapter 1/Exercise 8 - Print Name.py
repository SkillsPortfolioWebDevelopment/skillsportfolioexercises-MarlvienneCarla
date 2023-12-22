#define the number of rows in the pattern
rows = 5

#use a nested for loop to create a pattern with 'rows' number of rows
for i in range(1, rows + 1):
    #inner loop to print the numbers in each row
    for j in range(1, i +1):
        #print the current value of 'j' followed by a space and without a newline
        print(j, end=" ")
    #move to the next line to start a new row
    print()
