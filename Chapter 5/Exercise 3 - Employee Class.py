import tkinter as tk

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0

    def setData(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Employee Information App")

        # Create a list to store employee instances
        self.employee_list = []

        # Button to add employees
        self.add_button = tk.Button(master, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=0, column=0, pady=10)

        # Button to display employee details
        self.display_button = tk.Button(master, text="Display Employee Details", command=self.display_employee)
        self.display_button.grid(row=1, column=0, pady=10)

    def add_employee(self):
        # Create an instance of the Employee class
        employee = Employee()

        # Ask user to input employee details
        name = input("Enter employee name: ")
        position = input("Enter employee position: ")
        salary = float(input("Enter employee salary: "))
        emp_id = len(self.employee_list) + 1

        # Set data for the employee
        employee.setData(name, position, salary, emp_id)

        # Add the employee to the list
        self.employee_list.append(employee)

        print(f"\nEmployee {emp_id} added successfully!\n")

    def display_employee(self):
        print("\nName\tPosition\tSalary\tID")
        for employee in self.employee_list:
            print(employee.getData())

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()
