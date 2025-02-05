i = 0
while i < 8:
    if i == 2 or i == 4:
        i += 1
        continue
    n = 0
    while n < i:
        print(i, end='')
        n += 1
    print()
    i += 1