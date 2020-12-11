import base64

my_file = open("encodedflag.txt", "r")
context = my_flag.readline()

flag = ' '

for i in range(0, 5):
    flag = base64.b16decode(context)
    context = flag

for i in range(0, 5):
    flag = base64.b32decode(context)
    context = flag
    
for i in range(0, 5):
    flag = base64.b64decode(context)
    context = flag

print(context)

my_file.close()
