#Kody Fatch
#Module_2_Case_Study
#This app will take student's names and GPA as inputs and will test if the student qualifies for either the Dean's List or Honor Roll.
#https://github.com/kfatch/Module-1-Collaboration/blob/master/Module_2_Case_Study.py
counter = 0
while counter == 0:
    last_name = input("Enter student's last name:\n")
    if last_name == "ZZZ":
        counter += 1
        break
    first_name = input("Enter student's first name:\n")
    student_gpa = float(input("Enter student's GPA:\n"))
    if student_gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif student_gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} didn't make either the Dean's List or Honor Roll.")