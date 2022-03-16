"""class Mobile:
    def __init__(self):
        self.model = 'RealMe X'
    def show_model(self):
        price = 15000
        print("Model:", self.model, "Price:",price)
realme = Mobile()
realme.show_model()  # or print(realme.model)
print(id(realme))
print()

redmi = Mobile('Redmi 8s')
redmi.show_model(12000)
print(id(redmi))
"""

# or

class Mobile:
    def __init__(self,m):
        self.model = m
    def show_model(self,p):
        price = p
        print("Model:", self.model, "Price:",price)
realme = Mobile('RealMe X')
realme.show_model(15000)
print(id(realme))
print()

redmi = Mobile('Redmi 8s')
redmi.show_model(12000)
print(id(redmi))
