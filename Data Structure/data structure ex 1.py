listone = [3,6,9,12,15,18,21]
listtwo = [4,8,12,16,20,24,28]
listTree = []
oddElements = listone[1::2]
print("Element at odd-index positions from list one")
print(oddElements)
evenELement = listtwo[0::2]
print("Element at even-index positions from list two")
print(evenELement)
listTree.extend(oddElements)
listTree.extend(evenELement)
print("Printing Final third list")
print(listTree)