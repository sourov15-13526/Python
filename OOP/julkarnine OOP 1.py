class Person:
    def __init__(self,name,date_of_birth,ht):
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = ht
    def get_name(self):
        return self.name

    def get_summary(self):
        return f"name: {self.name} \nDOB: {self.date_of_birth} \nHeight: {self.height}"

    def set_name(self,new_name):
        self.name = new_name

a_person = Person("Sourov",1999,"5.5 feet")
b_person = Person("Zulkarnine",1990,"6 feet")
a_person.set_name("Md Sourov")
b_person.set_name("Zulkarnine Mahbub")
print(a_person.get_summary())
print(b_person.get_summary())