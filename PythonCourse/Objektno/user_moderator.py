from typing import Any


class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are curently {cls.active_users} active users!"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        User.active_users += 1
        self.first = first
        self.last = last
        self.age = age

    def logout(self):
        active_users -= 1
        return f"{self.first} {self.last} has logged out!"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}"


class Moderator(User):
    active_mods = 0

    @classmethod
    def display_active_mods(cls):
        return f"There are curently {cls.active_mods} active mods!"

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.active_mods += 1

    def remove_post(self):
        return f"{self.full_name()} has removed post from the {self.community} community"


jasmine = Moderator("Jasmine", "Clit", 25, "/blenderhelp")
kristina = Moderator("Kristina", "Clit", 22, "/superstonk")
user1 = User("Tom", "Garcia", 28)
user2 = User("Mark", "Twain", 18)
user3 = User("Good", "Soup", 21)
print(User.display_active_users())
print(Moderator.display_active_mods())
