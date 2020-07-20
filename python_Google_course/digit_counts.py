def digits(n):
    count = 0
    if n == 0:
        count = 1
    while (n >= 9):
        count += 1
        n = n / 10
        if n < 9:
            count += 1
            break

    return count

print(digits(35))
print(digits(144))
print(digits(1000))
