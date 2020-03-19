while True:
    print('Who are you?')
    name = input()

    if name.lower() != 'joe':  # using lower() func to match the name
        continue
    print('Hello Joe, what is the password? (It is a fish)')
    password = input()

    if password == 'swordfish':
        break

print('Access granted')