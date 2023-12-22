#import the math module for using math.pi
import math

#function to calculte the area of a square
def squarearea():
    #get user input for the side length of the square
    sidelength = float(input("\nEnter side length of square: "))
    #calculate the area of the square
    area = sidelength ** 2
    #print the calculated area
    print(f"\nThe are of the square is: {area}")

#fucntion to calculate the are of a circle
def circlearea():
    #get user input for the radius of the circles
    radius = float(input("\nEnter the radius of circle: "))
    #calculate the area of the circle using math.pi
    area = math.pi * radius ** 2
    #print it
    print(f"\nThe area of the cirle is: {area}")

#fucntion to calculate the area of a triangle
def trianglearea():
    #get auser input for the base length an height of the triangle
    point = float(input("\nEnter length of triangle: "))
    height = float(input("\nEnter the height of the triangle: "))
    #calculate the area of the triangle
    area = 0.5 * point * height
    #print it
    print(f"\nThe area of the traingle is: {area}")

#main loop for the shape calculator
while True:
    print("\nHello I'm Shape Calculator!\n")
    print("\nPlease Choose:")
    print("1: Calculate the are of a square\n")
    print("2: Calculate the area of a circle\n")
    print("3: Calculate the area of a triangle\n")
    print("4: Quit")

#get user input for the choice
    choice = input("\nEnter the number of your choice: \n")

#perform the chosen operation based on user input
    if choice == '1':
        squarearea()
    elif choice == '2':
        circlearea()
    elif choice == '3':
        trianglearea()
    elif choice == '4':
        #exit the loop if the user chooses to quit
        break
    else:
        #display an error message for invalid choices
        print("Invalid Please Try Again.")