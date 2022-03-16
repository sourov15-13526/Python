def inputstr(char):
    words = char.split()
    digitCount = 0
    symbolCount = 0
    charCount = 0
    for a in char:
        if a.islower() or a.isupper():
            charCount+=1
        elif a.isnumeric():
            digitCount+=1
        else:
            symbolCount+=1
    print("Chars = {} Digits = {} Symbol = {}".format(charCount,digitCount,symbolCount))
print("total counts of chars, digits,and symbols")
inputstr("P@#yn26at^&i5ve")
