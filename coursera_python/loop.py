largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == 'done':
        break

    try:
        num = int(num)
        if largest is None and smallest is None:
            largest = num
            smallest = num
        elif largest < num:
            largest = num
        elif smallest > num:
            smallest = num
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
