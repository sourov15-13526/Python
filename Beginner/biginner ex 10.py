def newlist(listone, listtwo):
    print("First list",listone)
    print("Second list", listtwo)
    thirdlist = []
    for num in listone:
        if (num%2 != 0):
            thirdlist.append(num)
    for num in listtwo:
        if (num%2 == 0):
            thirdlist.append(num)
    print("result is",thirdlist)
listone = [10, 20, 23, 11, 17]
listtwo = [13, 43, 24, 36, 12]
newlist(listone,listtwo)
