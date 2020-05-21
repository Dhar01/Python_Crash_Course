import re

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    # ^ means start with/matches the begining of a line
    if re.search('^From: ', line):
        print(line)