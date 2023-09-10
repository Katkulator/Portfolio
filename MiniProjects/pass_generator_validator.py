import string
from string import punctuation
import secrets
import random


class Password:
    def __init__(self):
        self.letters_lower = list(string.ascii_lowercase)
        self.letters_upper = list(string.ascii_uppercase)
        self.chars = list(punctuation)
        self.numbers = list(string.digits)
        self.password = []

    def validate_entries(self, validate=False):
        if (not validate and sum([self.upper, self.special, self.nums]) > self.pass_len) or (
            validate and sum([self.upper, self.special, self.nums, self.lower]) != self.pass_len):
            print("The sum of special characters, uppercase letters, and numbers exceeds the password length.")
            return False
        return True

    def start(self): #STARTS PASSWORD CREATION OR VALIDATION BASED ON USER INPUT
        is_finished = False
        while not is_finished:
            question = input('Press "c" if you would like to create a password or\npress "v" if you would like to validate password:')
            if question == "c":
                Password.create_password(self)
                is_finished = True
            elif question == "v":
                Password.validate_password(self)
                is_finished = True
            else:
                print('Please type "c" or "v"!')

    def questions(self, validate): #ASKS USER FOR INPUT ABOUT AMOUNT OF CHARACTERS IN PASSWORD
        self.pass_len = int(input(f"How many characters do you{' want to' if not validate else ''} have in your password?: "))
        self.upper = int(input(f"How many uppercase letters do you{' want to' if not validate else ''} have in your password?: "))
        self.special = int(input(f"How many special chars do you{' want to' if not validate else ''} have in your password?: "))
        self.nums = int(input(f"How many numbers do you{' want to' if not validate else ''} have in your password?: "))
        if validate:
            self.lower = int(input("How many lowercase letters do you have in your password?:"))

    def create_password(self): #CREATES THE PASSWORD, BUT CHECKS IF THE SUM OF CHARACTERS IS OKAY
        pass_created = False
        while not pass_created:
            try:
                self.questions(validate=False)
                self.validate_entries(validate=False)
                self.fill_password()
                print("Here is your password", "".join(self.password))
                pass_created = True
            except ValueError:
                print("Invalid input. Please enter only integers.")
            
    def fill_password(self): #FILLS THE PASSWORD WITH CHARACTERS BASED ON USER INPUT
        for i in range(self.pass_len - self.upper - self.special - self.nums):
            self.password.append(secrets.choice(self.letters_lower))
        for i in range(self.upper):
            self.password.append(secrets.choice(self.letters_upper))
        for i in range(self.special):
            self.password.append(secrets.choice(self.chars))
        for i in range(self.nums):
            self.password.append(secrets.choice(self.numbers))
        random.shuffle(self.password)

    def validate_password(self): #METHOD FOR VALIDATING PASSWORD
        pass_validated = False
        print("Lets validate your password")
        while not pass_validated:
            self.questions(validate=True)
            if not self.validate_entries(validate=True):
                continue
            pass_eval = input("Type your password here: ")
            self.valid_length = len(pass_eval) == self.pass_len
            self.valid_upper = len(
                [char for char in pass_eval if char in self.letters_upper]) == self.upper
            self.valid_lower = len(
                [char for char in pass_eval if char in self.letters_lower]) == self.lower
            self.valid_special = len(
                [char for char in pass_eval if char in self.chars]) == self.special
            self.valid_nums = len(
                [char for char in pass_eval if char in self.numbers]) == self.nums
            
            if all([self.valid_length, self.valid_upper, self.valid_special, self.valid_nums]):
                print("Pass is valid.")
                pass_validated = True
            else:
                print("Pass is not valid.")
            
if __name__ == "__main__":
    Password().start()
