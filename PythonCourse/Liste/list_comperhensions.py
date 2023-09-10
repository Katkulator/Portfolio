""" nums = [1,2,3]
[x*10 for x in nums]
print(nums) """

""" numbers = [1, 2, 3, 4, 5]
doubled_numbers = [num*2 for num in numbers]

print(doubled_numbers) """

#colors = ["red", "blue", "green", "yellow", "black", "white"]
#colors_upper = [color[0].upper() + color[1:] for color in colors ]
#colors_upper = [color.capitalize() for color in colors]
#print(colors_upper)

#numbers = [1,2,3,4,5]
#string_list = [str(num) for num in numbers]
#print(string_list)

######STRINGS WITH CONDITIONALS######

#numbers = [1, 2, 3, 4, 5]
#odd = [num for num in numbers if num %2 != 0]
#even = [num for num in numbers if num %2 == 0]
#calc = [num*2 if num %2 == 0 else num/2 for num in numbers ]

#print(odd)
#print(even)
#print(calc)

# with_vowels = "That is cool dude!"
# without_vowels = "".join (char for char in with_vowels if char not in "a,e,i,o,u")
# print(without_vowels)

#strings = ["intro", "to", "list", "comps"]

# results =[]
# for i in strings:
#     i = i.upper()
#     results.append(i)
# print(results)

# results2 = [i.upper() for i in strings]
# print(results2)

# nums = [1,2,3,4,5,6]
# results = []
# def timesFive(num):
#     return num*5

# for i in nums:
#     i = timesFive(i)
#     results.append(i)

# results2 = [timesFive(i) for i in nums]
# print(results2)


# dicts = [{"name": "John"}, {"name" : "Matt"}]
# results3 = []

# for i in dicts:
#     results3.append(i["name"])

# print(results3 )

# def disemvowel(string_):
#     return "".join (char for char in string_ if char not in "a,e,i,o,u,A,E,I,O,U")
# print(disemvowel("This website is for losers LOL!"))

# def find_it(seq):
#     for i in range(len(seq)):
#         if seq.count(seq[i]) % 2 != 0:
#             return seq[i]
        
# print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))

# def sum_two_smallest_numers(numbers):
#     return sum(sorted(numbers)[:2])
    

# print(sum_two_smallest_numers([3,5,9,6,10]))

# def validate_pin(pin):
#     return pin.isalpha() and len(pin) in (4,6)

# def solution(number):
#     total = 0
#     for i in range(0,number):
#         if i % 3 == 0 or i % 5 == 0:
#             total += i
#     return total
# print(solution(16))

# ilii

# def solution(number):
#     return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# def descending_order(num):
#     return int("".join(sorted(str(num), reverse = True)))

# print(descending_order(815973804))

def square_digits(num):
    return int("".join(str(int(i)**2) for i in str(num)))
    
print(square_digits(9119))
