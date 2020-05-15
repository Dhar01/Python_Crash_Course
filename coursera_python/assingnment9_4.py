# courseara assignment 9.4
# answer needed cwen@iupui.edu 5
name = input("Enter file:")

if len(name) < 1: 
   name = "mbox-short.txt"

handle = open(name)

counts = dict()

for line in handle:
    line = line.strip()
    # here 'From ' with space is very important
    if line.startswith('From '):
        words = line.split()
        word = words[1]
        counts[word] = counts.get(word, 0) + 1
    else:
        continue


bigCount = None
bigWord = None

for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
    
print(bigWord, bigCount)