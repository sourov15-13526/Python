inputstr = "PyNaTive"
words = inputstr.split()
lower = []
upper = []
for char in inputstr:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
precedence = ''.join(lower+upper)
print("arranging characters giving precedence to lowercase letters")
print(precedence)

