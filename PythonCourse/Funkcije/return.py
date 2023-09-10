from random import random

# def square_of_7():
#    return 7**2

# print(square_of_7())

# def say_hi():
#    return "Hi!"

# greeting = say_hi()
# print(greeting)

def flip_coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"

print(flip_coin())


#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    return [num for num in range(1,50) if num % 2 == 0]

def generate_evens2():
    evens = []
    for num in range(1,50):
        if num % 2 == 0:
            evens.append(num)
    return(evens)

def sum_odd_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1,2,3,4,5,6,7]))


#unnecessary else

def is_odd_number(num):
    if num % 2 != 0:
        return True
    else:
        return False
#bolje
def is_odd_number(num):
    if num % 2 != 0:
        return True
    return False





   
