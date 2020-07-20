class Person:
    def __init__(self, name, date_of_birth, ht):
        self.name = name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_name(self):
        return self.name

    def get_summary(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: (self.height}"


a_person = Person("Zulkarnine", "1990", "6 feet")
b_person = Person("Robot")

print(a_person.get_name())
print(b_person.get_name())
