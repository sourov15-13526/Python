def outerFun(a, b):
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(15, 10)
print(result)