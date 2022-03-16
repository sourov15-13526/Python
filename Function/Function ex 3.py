def calculation(a, b):
    return a+b, a-b

res = calculation(40, 10)
print(res)

#or

def calculation(a, b):
    return a+b, a-b

add, sub = calculation(40, 10)
print(add)
print(sub)