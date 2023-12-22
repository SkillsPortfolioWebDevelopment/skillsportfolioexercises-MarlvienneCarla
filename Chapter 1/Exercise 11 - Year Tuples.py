#create a tuple as years
years = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

#access the element at the -3 position in the tuple
valuesminus_3 = years[-3]
print("Value in list -3: ", valuesminus_3, "\n")

#create a reversed version of the original tuple
reverseyear = years[::-1]
print("\nOriginal Tuple: ", years, "\n")
print("\nReversed Tuple: ", reverseyear, "\n")

#count the number of times 2009 appears in the tuple
count2009 = years.count(2009)
print("\nNumber od times 2009 appears in the tuple: ", count2009, "\n")

#find the index of the first occurence of 2018
index2018 = years.index(2018)
print("\nIndex of 2018: ", index2018, "\n")

#calculate the length of the tuple
tuplelength = len(years)
print("\nLength of the tuple: ", tuplelength, "\n")