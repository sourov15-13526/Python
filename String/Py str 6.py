def twostring(s1,s2):
    s2 = s2[::-1]
    lengthS1 = len(s1)
    lengthS2 = len(s2)
    length = lengthS1 if lengthS1 > lengthS2 else lengthS2
    stringresult = ""
    for a in range(length):
        if (a < lengthS1):
            stringresult = stringresult + s1[a]
        if (a < lengthS2):
            stringresult = stringresult + s2[a]
    print(stringresult)
twostring("Pynative","Website")