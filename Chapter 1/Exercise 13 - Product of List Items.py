#define a fucntuon to calcultae the product of values in a list
def productcalc(first):
    #initialize the product to 1
    product = 1
    #iterate through each value in the list
    for value in first:
        #multiply the curren value with the acculmelated product
        product *= value
    return product

#given lusr of values
list = [5, 7, 3, 9]

#call the fucntion to calculate the product of values in the list
result = productcalc(list)
#print the result
print(f"The product of values in the list is: {result}")