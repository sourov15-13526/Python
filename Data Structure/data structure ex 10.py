sampleList = [87, 52, 44, 53, 54, 87, 52, 53]

sampleList = list(set(sampleList))
print("unique list", sampleList)

tuple = tuple(sampleList)
print("tuple ", tuple)

print("Minimum number is: ", min(tuple))
print("Maximum number is: ", max(tuple))