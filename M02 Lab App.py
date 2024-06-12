#Emily Elliott
#M02 Lab App.py
#This app will use is else and while loops to determin if the student is on the deans list or the Hounor role.

last_name = ""

while last_name.upper() != 'ZZZ':
    last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
    if last_name.upper() == 'ZZZ':
        break
    
    first_name = input("Enter the student's first name: ")

    gpa_str = input("Enter the student's GPA: ")
    
    if gpa_str.replace('.', '', 1).isdigit():
        gpa = float(gpa_str)

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"{first_name} {last_name} did not qualify for the Dean's List or the Honor Roll.")
    else:
        print("Invalid GPA. Please enter a numeric value.")
