# Dictonary Practice
student_grades = {}

off = False

while not off:
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")
    student_grades[name] = grade
    print("Student added successfully \n" + str(student_grades))
    add_another = input("Would you like to add another student? Y or N ").lower()
    if add_another == "y":
        pass
    else:
        off = True
