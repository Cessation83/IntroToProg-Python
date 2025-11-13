# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Mike Luke,11/10/2025,Modified Script
# ------------------------------------------------------------------------------------------ #
import _io
import json #import json module

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list[dict[str, str, str]] = []  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as file_error:
    print('Error: File not found!')
    print(f'Details: {file_error}')

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError ('First name must be alphanumeric')
            student_last_name = input("Enter the student's last name: ")
            if not student_first_name.isalpha():
                raise ValueError ('Last name must be alphanumeric')
            course_menu = """
            --- Choose your Course ---
            1. Python 100
            2. C++ 100›
            3. Java 100
            4. PHP 100
            5. React 100
            --------------------------
            """

            print(course_menu)
            course_choice = input('Enter your choice 1-5: ')

            # Map course choice to course name
            course_options = {
                '1': 'Python 100',
                '2': 'C++ 100',
                '3': 'Java 100',
                '4': 'PHP 100',
                '5': 'React 100'
            }
            if course_choice in course_options:
                course_name = course_options[course_choice]
            if not course_choice.isdigit:
                raise ValueError ('Course Option must be Numeric Value 1-5')

        # Add Dictionary New Row
            student_data = {
                'FirstName' : student_first_name,
                'LastName' : student_last_name,
                'CourseName' : course_name,
            }
            students.append(student_data)
        finally:
            print(f'You have registered {student_first_name}'
                  f' {student_last_name} for {course_name}.')
            print('Please Use Option 3 to Save Your Data.')
        continue

    # Present the current data
    elif menu_choice == "2":
        print('The Following Students are Currently Registered')
        print('-' * 50)
        for student_data in students:
            student_first_name = student_data['FirstName']
            student_last_name = student_data['LastName']
            course_name = student_data['CourseName']
            print(f'{student_first_name}, {student_last_name}, {course_name}')
        print('-' * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=4)  # Adding the indent option to format the JSON file.
            file.close()
            print('You have saved all your data to file.')
        except FileNotFoundError as file_error:
            print('Error: File not found!')
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
