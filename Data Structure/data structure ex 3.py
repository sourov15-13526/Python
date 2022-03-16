list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list:",list)
a = list[0:3]
print("Chunk 1:",a)
a = a[::-1]
print("After reversing it:",a)
b = list[3:6]
print("Chunk 2:",b)
b = b[::-1]
print("After reversing it:",b)
c = list[6:len(list)+1]
print("Chunk 3:",c)
c = c[::-1]
print("After reversing it: ",c)