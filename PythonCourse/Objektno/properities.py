class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:
    #         self._age = 0

    @property  # getter - age je sada properity
    def age(self):
        return self._age

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @age.setter  # setter properity
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age can't be negative number!")


jane = Human("jane", "goodal", 34)
# print(jane.get_age())
# jane.set_age(51)
# print(jane._age)
print(jane.age)  # printamo age kao da je atribut, a nemožemo printati _age zato što je privatni atribut. Iako je metoda, ne trebamo zareze kad ju zovemo
jane.age = 20  # možemo vrijednost spremiti u varijablu
print(jane.age)
print(jane.full_name)
