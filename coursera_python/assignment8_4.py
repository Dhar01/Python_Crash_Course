fname = input('Enter file name: ')
fh = open(fname)

lst = list()
listFull = list()

for line in fh:
    # line.rstrip()
    lst = line.split()
    listFull = listFull.append(lst)

listFull.sort()
print(listFull)
