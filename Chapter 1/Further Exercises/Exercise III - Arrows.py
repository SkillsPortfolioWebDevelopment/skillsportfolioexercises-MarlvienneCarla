#number of rows for arrows
rows = 5

#loop to print the upper part of the arrow
for i in range(1, rows + 1):
    #calculate the number of spaces for the current row
    spaces = " " * (rows  - i)
    #calculate the number of stars for the current row
    stars = "*" * (2 * i - 1)
    #print the spces and stars for tge current row
    print(spaces + stars)

#loop to print the lower part of the arrow
for i in range(1, 4):
    #calculate the number of spces for the curent row
    spaces = " " * (rows - 1)
    #fixed at 3 stars for the current row
    stars = "*" * 3
    #print the spacs and stars fo rthe current row
    print(spaces + stars)