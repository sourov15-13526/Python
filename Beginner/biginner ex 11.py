def reversenum(num):
    print("Reverse order is:",end=" ")
    while (num>0):
        digit = num%10
        num = num//10
        print(digit,end=" ")

number = 7536
reversenum(number)