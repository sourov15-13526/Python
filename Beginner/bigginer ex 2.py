print("Printing current and previous number sum in a given")
t = int(input())
x = 0
for i in range(t):
    print("Current Number", i,"previous Number",x,"Sum:",i+x)
    x = i