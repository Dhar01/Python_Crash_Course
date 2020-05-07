# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
result = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    number = line.find('.')
    number = int(number)
    number = number - 1
    addition = line[number:]
    addition = float(addition)
    result = result + addition
    
result1 = result / count
print("Average spam confidence:", result1)
