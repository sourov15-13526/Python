FirstSet = {27, 43, 34}
SecondSet = {34, 93, 22, 27, 43, 53, 48}
print("First set is subset of second set:",FirstSet.issubset(SecondSet))
print("Second set is subset of first set:",SecondSet.issubset(FirstSet))
print("First set is Super set of second set:", FirstSet.issuperset(SecondSet))
print("Second set is Super set of First set:", SecondSet.issuperset(FirstSet))
if(FirstSet.issubset(SecondSet)):
    FirstSet.clear()
if(SecondSet.issubset(FirstSet)):
    SecondSet.clear()
print("First set is : ",FirstSet)
print("Second set is :",SecondSet)

