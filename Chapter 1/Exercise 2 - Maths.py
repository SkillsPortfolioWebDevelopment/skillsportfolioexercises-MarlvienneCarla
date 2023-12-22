#propmt the user to enter numbers
a = float(input("\nPut Number you want: \n"))
b = float(input("\nAny Number you want: "))

#the formula for each calculations
showsum = a + b
difference = a - b
product = a * b
quotient = a / b
remainder = a % b

#display the calculated results
print(f"Sum : {a} + {b} = {showsum}")
print(f"Difference: {a} - {b} = {difference}")
print(f"Product: {a} * {b} = {product}")
print(f"Quotient: {a} + {b} = {quotient}")
print(f"Remainder: {a} % {b} = {remainder}")
