text = "X-DSPAM-Confidence:    0.8475";

cut = text.find('.')
cut = int(cut)
cut = cut -1
num = text[cut:]
number = float(num)

print(number)
