import json

def write_to_json(data):
    with open('StudentJson.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

def read_from_json():
    with open('StudentJson.json', 'r') as json_file:
        data = json.load(json_file)
        return data

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

# Update the existing data with the new CourseDetails
existing_data["StudentDetails"][0]["CourseDetails"] = course_details

# Write the updated data to the JSON file
write_to_json(existing_data)

# Read the data again to display the final details
final_data = read_from_json()["StudentDetails"][0]

# Display the details
print("\nDetails of the Student are")
print(f"  Name: {final_data['Name']}")
print(f"  ID: {final_data['ID']}")
print(f"  Course: {final_data['course']}")
print(f"  Group: {final_data['CourseDetails']['Group']}")
print(f"  Year: {final_data['CourseDetails']['Year']}")
