class Animal():
    cool = True

    def make_sound(self, sound):
        print(sound)


class Cat(Animal):
    pass


gandalf = Animal()
print(gandalf.cool)
gandalf.make_sound("meow")
