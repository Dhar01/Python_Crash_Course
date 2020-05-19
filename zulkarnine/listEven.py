def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

starting = 0
even_numbers =[]
user_input = int(input("Limit:"))

"""while starting < user_input:
    if is_even(starting):
        even_numbers.append(starting)
    
    starting = starting + 1 """

for value in range(0, user_input + 1):
    if is_even(value):
        even_numbers.append(value)

print(f"Even Numbers: {even_numbers}")
print("Finished")