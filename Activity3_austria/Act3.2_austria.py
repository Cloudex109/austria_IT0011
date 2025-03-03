first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")


full_name = first_name + last_name
upper_case_name = full_name.upper()
lower_case_name = full_name.lower()
name_length = len(full_name)

print("Fullname: ", full_name)
print("Fullname (Upper Case): ", upper_case_name)
print("Fullname (Lower Case): ", lower_case_name)
print("Length of Full Name: ", name_length)