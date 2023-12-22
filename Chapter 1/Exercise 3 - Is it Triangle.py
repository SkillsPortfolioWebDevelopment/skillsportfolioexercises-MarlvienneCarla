#propmt the user to put each extent
a = int(input("Enter extent for side A :"))
b = int(input("Enter extent for side B :"))
c = int(input("Enter extent for side C :"))

#define a funtion to determine the type of triangle based on side lengths
def type_triangle(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"

#to check if the side lengths can form a valid triangle
def valid(a, b, c):
    return a + b > c and a + c > b and b + c > a

#check if the provided side lengths is valid
if valid(a, b, c):
    #if valid, determine the type of tringle
    triangle_type = type_triangle(a, b, c)
    print(f"This is a {triangle_type} triangle.")
else:
    #if not valid, display an error message
    print("These extent is not valid to form a triangle.")
    