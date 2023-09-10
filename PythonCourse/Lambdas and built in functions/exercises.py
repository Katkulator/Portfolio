#Write a lambda that accepts a single number and cubes it. Save it in a variable called cube .
cube = lambda num: num ** 3
print(cube(2))
print(cube(3))
print(cube(8))

#Write a function called decrement_list  that accepts a single list of numbers as a parameter.
# It should return a copy of the list where each item has been decremented by one.
# Use map to do this!

# numbers = [1,2,3,4]
# decrement = map(lambda num: num - 1, numbers)
# print(list(decrement))
def decrement_list(l):
    return list(map(lambda n: n-1, l))
    
decrement_list([1,2,3])
decrement_list([20,14,11])

#Write a function called remove_negatives that accepts a list of numbers and
# returns a copy of the lists with all negative numbers removed.
# Use filter() in your implementation, not a list comprehension!
def remove_negatives(numbers):
    return list(filter(lambda num : num >= 0, numbers ))

print(remove_negatives([-1,2,3,-45,11,-13,0]))

#Implement a function is_all_strings  that accepts a single iterable
#and returns True if it contains ONLY strings.  Otherwise, it should return false.
def is_all_strings(l):
    return all(type(x) == str for x in l) #ovo je generator, možemo koristiti i list comp, smo dodamo []
print(is_all_strings(["a", "b", 2]))  

#Write a function called extremes  which accepts an iterable.
#It should return a tuple containing the minimum and maximum elements.
def extremes(elements):
    return min(elements), max(elements)

print(extremes([1,2,3,4,5]))
print(extremes((99,25,30,-7)))
print(extremes("alcatraz"))


#Write a function max_magnitude  that accepts a single list full of numbers.
#It should return the magnitude of the number with the largest magnitude (the number that is furthest away from zero).
def max_magnitude(l):
    return max(abs(value) for value in l)
    
print(max_magnitude([300, 20, -900]))  
print(max_magnitude([10, 11, 12]))  
print(max_magnitude([-5, -1, -89]))

#Write a function called sum_even_values. This function should accept a variable
#number of arguments and return the sum of all the arguments that are divisible by 2.
#If there are no numbers divisible by 2, the function should return 0.
#To be clear, it accepts all the numbers as individual arguments!
def sum_even_values(*numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10)) 
print(sum_even_values(1,3,7)) 
        
#DRUGO KRAĆE RJEŠENJE
def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)

print(sum_even_values(1,2,3,4,5,6))
print(sum_even_values(4,2,1,10)) 
print(sum_even_values(1,3,7)) 

#Write a function called sum_floats.
#This function should accept a variable number of arguments.
#The function should return the sum of all the parameters that are floats.
#If there are no floats the function should return 0
def sum_floats(*args):
    return(sum(arg for arg in args if type(arg) is float))

print(sum_floats(1.5, 2.4, 'awesome', [], 1)) # 3.9
print(sum_floats(1,2,3,4,5)) # 0

#Write a function interleave  that accepts two strings.
#It should return a new string containing the 2 strings interwoven or zipped together. For example:
def interleave(str1, str2):
    return ''.join(''.join(x) for x in zip(str1,str2))

print(interleave('hi','ha'))    # 'hhia'
print(interleave('aaa', 'zzz'))  # 'azazaz'
print(interleave('lzr','iad')) #  'lizard'

#Write a function called triple_and_filter. This function should accept a list of numbers,
#filter out every number that is not divisible by 4, and return a new list where every remaining number is tripled.
def triple_and_filter(l):
    return list(map(lambda num: num*3, filter(lambda num: num % 4==0,l)))
print(triple_and_filter([1,2,3,4]))
print(triple_and_filter([6,8,10,12]))

#Write a function called extract_full_name. This function should accept a list of dictionaries
#and return a new list of strings with the first and last name keys in each dictionary concatenated.
def extract_full_name(dict_list):
    return list(map(lambda val: f"{val['first']} {val['last']}", dict_list))
print(extract_full_name([{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]))


