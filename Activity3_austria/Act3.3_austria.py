first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")
age = input("Enter your age: ")
contact_number = input("Enter your Contact No.: ")
course = input("Enter course: ")

student_details = f"Name: {first_name} {last_name} \n Age: {age} \n Contact No.: {contact_number} \n Course: {course}"

with open("students.txt", "a") as file:
    file.write(student_details)
file.close()

print("Student information has been saved to 'students.txt'.")