inp = input("Enter a string: ")
vowels = 0
consonants = 0
space = 0
i = 0
special = 0
for char in inp:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isspace():
        space += 1
    elif char.isalnum():
        i += 1
    else:
        special += 1
        
print("""vowels = {}
1consonants = {}
space = {}
numbers = {}
special = {}""".format(vowels, consonants, space, i, special))