def spamList(items):
    count = 0
    maxCount = len(items) - 1 # cause item no and length are not same

    for i in range(len(items)):
        if count < maxCount:
            print(str(items[count]) + ', ', end='')
            count += 1
        else:
            print('and ' + items[maxCount])

spam = ['apples', 'bananas', 'tofu', 'cats']

spamList(spam)
