import json

# Function to write data to JSON file
def write_to_json(data):
    with open('StudentJson.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Function to read data from JSON file
def read_from_json():
    with open('StudentJson.json', 'r') as json_file:
        data = json.load(json_file)
        return data

# Function to display student details
def display_student_details(student_data):
    print("\nDetails of the Student are")
    print(f"  Name: {student_data['Name']}")
    print(f"  ID: {student_data['ID']}")
    print(f"  Course: {student_data['course']}")
    if 'CourseDetails' in student_data:
        print(f"  Group: {student_data['CourseDetails']['Group']}")
        print(f"  Year: {student_data['CourseDetails']['Year']}")

# Ask the user to enter student details
name = input("Enter the student name: ")
student_id = int(input("Enter the student ID: "))
course = input("Enter the course: ")

# Create the initial student details dictionary
student_details = {
    "Name": name,
    "ID": student_id,
    "course": course
}

# Write the initial student details to the JSON file
write_to_json({"StudentDetails": [student_details]})

# Ask the user to enter additional CourseDetails
group = input("Enter the group: ")
year = int(input("Enter the year: "))

# Append CourseDetails to the existing student dictionary
course_details = {
    "Group": group,
    "Year": year
}

# Read the existing data from the JSON file
existing_data = read_from_json()

# Update the existing data with the new CourseDetails for the first student
existing_data["StudentDetails"][0]["CourseDetails"] = course_details

# Write the updated data to the JSON file
write_to_json(existing_data)

# Read the data again to display the final details for the first student
final_data = read_from_json()["StudentDetails"][0]
display_student_details(final_data)

# Ask the user to enter details for another student
name2 = input("Enter the name of another student: ")
id2 = int(input("Enter the ID of another student: "))
course2 = input("Enter the course of another student: ")

# Create a dictionary for the second student
student_details2 = {
    "Name": name2,
    "ID": id2,
    "course": course2
}

# Append the details of the second student to the existing data
existing_data["StudentDetails"].append(student_details2)

# Write the updated data to the JSON file
write_to_json(existing_data)

# Read the data again to display the final details for both students
final_data1 = read_from_json()["StudentDetails"][0]
final_data2 = read_from_json()["StudentDetails"][1]

# Display details for both students
print("\nDetails for the first student:")
display_student_details(final_data1)

print("\nDetails for the second student:")
display_student_details(final_data2)
