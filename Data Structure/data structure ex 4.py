sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)
print("Printing count of each item",end=" ")
print({k:sampleList.count(k) for k in sampleList})