def twostr(s1,s2):
    midle1 = int(len(s1)/2)
    midle2 = int(len(s2)/2)
    print(s1[:1]+s2[:1]+s1[midle1:midle1+1]+s2[midle2:midle2+1]+s1[len(s1)-1]+s2[len(s2)-1])
twostr("America","Japan")

