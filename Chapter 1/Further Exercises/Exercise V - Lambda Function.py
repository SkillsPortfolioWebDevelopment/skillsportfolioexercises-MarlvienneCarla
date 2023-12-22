#given list of tuples container course names and makrs
marks = [("CodeLab I",67),("web Development", 75),("CodeLabII",74),("Smartphone Apps",68),("Games Development",70),("Responsive web",65)]

#sort the list of tuples by marks in ascending order
lowtohigh = sorted(marks, key=lambda x: x[1])
#by in descending order
hightolow = sorted(marks, key=lambda x: x[1], reverse=True)

#print the original list
print(marks)
#the list of the marks sorted in ascending order
print("\nSorted by marks low to high: ", lowtohigh)
#the list sorted in descending order
print("\nSorted by marks high to low: ", hightolow)