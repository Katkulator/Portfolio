from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, another_human):
        if isinstance(another_human, Human):
            return Human(first="Newborn", last=self.last, age=0)
        return "you can't add that"

    def __mul__(self, another_human):
        if isinstance(another_human, int):
            # return [self for i in range(another_human)]
            return [copy(self) for i in range(another_human)]
        return "CAN'T MULTIPLY"


j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 49)
print(j)
print(len(j))
print(j+k)
print(j*2)
triplets = j * 3
# triplets[1].first = "Jessica" #svima promjeni ime jer su sve kopije!
triplets[1].first = "Jessica" #promjeni jednoj jer sada svaka ima drugo mjesto u memoriji zbog copy 
print(triplets)
