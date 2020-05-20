words_all = []
unique_words = set()

with open("shaks.txt", mode="r") as s_file:
    for line in s_file.readlines():
        words = line.strip().split(" ")
        words_all += words

    unique_words = set(words_all)
    print(unique_words)

    with open("unique_words.txt", mode="w") as write_file:
        for item in unique_words:
            write_file.write(item)
            write_file.write(" ")

print("finished")