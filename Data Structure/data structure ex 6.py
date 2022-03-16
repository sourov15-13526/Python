FirstSet = {65, 42, 78, 83, 23, 57, 29}
SecondSet = {67, 73, 43, 48, 83, 57, 29}
ThirdSet = FirstSet.intersection(SecondSet)
print("Intersection is: ",ThirdSet)
FirstSet.difference_update(ThirdSet)
print("After removing intersection:",FirstSet)