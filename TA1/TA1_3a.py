i = 5
for x in range(1, i+1, 1):
    print(" " * (i - x) + "".join(str(num) for num in range(1, x + 1, 1)))