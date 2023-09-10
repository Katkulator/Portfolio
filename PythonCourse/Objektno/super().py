class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def sound(self, sound):
        return f"this animal says {sound}"


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        return f"{self.name} plays whith {self.toy}"


cica = Cat("Cica", "Calico", "Gumica za kosu")
print(cica.play())
print(cica.species)
