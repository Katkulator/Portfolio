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


#Implement a function yell  which accepts a single string argument.
# It should return(not print) an uppercased version of the string with an exclamation point aded at the end
def yell(string):
    return string.upper() + "!"

print(yell("go away"))
print(yell("leave me alone"))

#Using the string format() method:
def yell(word):
    return "{}!".format(word.upper())

#Using an f-string, my personal favorite (works in Python 3.6 or later):
def yell(word):
    return f"{word.upper()}!"

#Write a function called return_day. this function takes in one parameter (a number from 1-7)
# and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.).
# If the number is less than 1 or greater than 7, the function should return None
def return_day(day_num):
    weekdays = {1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday"}
    if day_num in range(1,8):
        return weekdays.get(day_num)
    else:
        return None

print(return_day(9))



#Write a function called last_element. This function takes in one parameter (a list)
# and returns the last value in the list. It should return None if the list is empty.
def last_element(list):
    if list:
        return list[-1]
    else:
        return None
print(last_element([]))
    

#Write a function called is_palindrome.This function should take in one parameter and returns True or False
# depending on whether it is a palindrome. As a bonus, allow your function to ignore whitespace and capitalization so that
# is_palindrome('a man a plan a canal Panama') returns True.

def is_palindrome(word):
    backwards = [element for element in word[::-1].lower().replace(" ","")]
    forward = [element for element in word[::1].lower().replace(" ","")]
    if backwards == forward:
        return True
    else:
        return False
    
# def is_palindrome(string): KRAĆE RJEŠENJE
#     stripped = string.replace(" ", "").lower()
#     return stripped == stripped[::-1]

print(is_palindrome("tacocat"))
print(is_palindrome("testing"))
print(is_palindrome("a man a plan a canal Panama"))


#Write a function called frequency. This function accepts a list
# and a search_term (this will always be a primitive value) and returns
# the number of times the search_term appears in the list.
def frequency(data,search_term):
    return data.count(search_term)
print(frequency([False, False, False, False, True, True],False))

#Write a function called multiply_even_numbers.
# This function accepts a list of numbers and returns the product of all even numbers in the list.
def multiply_even_numbers(numbers):
    collection = 1
    for num in numbers:
        if num % 2 == 0:
            collection *= num
    return collection
print(multiply_even_numbers([1,2,3,4,5,6,7]))

#Write a function called capitalize.
#This function accepts a string and returns the same string with the first letter capitalized. 
# You may want to use slices to help you out.
def capitalize(x):
    return x.capitalize()
print(capitalize("jamaica"))
print(capitalize("france"))

#Write a function called compact.
# This function accepts a list and returns a list of values that are truthy values,
# without any of the falsey values.
def compact(items):
    collection = []
    for item in items:
        if item:
            collection.append(item)
    return collection
print(compact([0,1,2,"",[], False, {}, None, "All done"]))

def compact(l):
    return [val for val in l if val]


#Write a function called intersection. This function should accept two lists
# and return a list with the values that are in both input lists.
def intersection(l1,l2):
    return list(set(l1) & set(l2))
print(intersection([1,2,3,4],[4,5,6,7]))


#Write a function called partition. This function accepts a list and a callback function (which you can assume returns True  or False  ). 
#The function should iterate over each element in the list and invoke the callback function at each iteration. 
# If the result of the callback function is True , the element should go into the first list (i.e. the "truthy" list).
# If the result of the callback function is False , the element should go into the second list (i.e. the "falsy" list).
# When it's finished, partition should return both lists inside of one larger list, like so:

def isOdd(num):
    return num % 2 != 0


def partition(data, fn=isOdd):
    return [[num for num in data if fn(num)],[num for num in data if not fn(num)]]

print(partition([1,2,3,4,5,6,7,8]))