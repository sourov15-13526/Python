rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
print("Roll Number:",rollNumber)
print("Dictionary:",sampleDict)
list = []
for item in rollNumber:
    if item in sampleDict.values():
        list.append(item)
print("After removing unwanted items from rollNumber:",list)
