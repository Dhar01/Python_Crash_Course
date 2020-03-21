# main part

def collatz(number):
    if number%2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    return result

def sequence(number):
    result = collatz(number)

    while result != 1:
        result = collatz(result)
        print(result)

# input validation

try:
    userInput = int(input())
    sequence(userInput)
except ValueError:
    print('Input must be an integer.')
