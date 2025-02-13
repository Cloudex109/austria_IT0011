def is_palindrome(n):
    return str(n) == str(n)[::-1]

def process_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    for index, line in enumerate(lines[:10], start=1):
        numbers = [int(num) for num in line.strip().split(',') if num.strip().isdigit()]
        total = sum(numbers)
        result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
        print(f"Line {index}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
        
process_file('numbers.txt')