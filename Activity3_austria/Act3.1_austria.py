first_name = input("Enter your firstname: ")
last_name = input("Enter your lastname: ")
age = input("Enter your age: ")

full_name = first_name + last_name
sliced_name = first_name[:3]
greeting_message = f"Hello, {first_name}!, Welcome. You are {age} years old."

print("Fullname: ", full_name)
print("Sliced Name: ", sliced_name)
print("Greeting Message:", greeting_message)