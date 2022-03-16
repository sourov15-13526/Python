floatnumbers = []
n = int(input("Enter the list size: "))
for i in range(0,n):
    print("Enter number at location",i,":")
    item = float(input())
    floatnumbers.append(item)
print("User list is", floatnumbers)
