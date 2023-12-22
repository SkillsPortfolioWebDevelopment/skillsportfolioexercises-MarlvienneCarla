#outer loop for each table from 1 to 10
for table in range(1, 11):
    #display the header for the current multiplication table
    print(f"Multiplication table of {table}")

    #inner loop or multiplying the current table by numbers from 1 to 10
    for multiplier in range(1,11):
        #calculate the result of multiplication
        result = table * multiplier
        #display the multiplication expression and result
        print(f"{table} x {multiplier} = {result}")
    print()