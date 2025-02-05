inp = input("Input a string with numbers: ")
i = 0

for char in inp:
    if char.isdigit():
        i += int(char)
        
print("sum of the numbers in the string: {}".format(i))