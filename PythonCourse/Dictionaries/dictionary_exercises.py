# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")

# ILI
quantity = bakery_stock.get(food)
if quantity:
    print(f"{quantity} left")
else:
    print("we don't make that")

####################################################################################################################################################################

#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = {}.fromkeys(game_properties, 0)
print(initial_game_state)

####################################################################################################################################################################

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD

stock_list = {}
stock_list = inventory.copy()

# add the value 18 to stock_list under the key "cookie"
stock_list["cookie"] = 18 ##dodaje key-value u dict ili overrida postojeći key sa drugom vrijednosti

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop("cake")


######################################################################################################################################################################

#Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"]
# create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.
# Save it to a variable called answer.
#I expect you to do this with a dictionary comprehension, but you can also use a built-in function called zip .
# We cover it later in the course.

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,3)}
answer2 = dict(zip(list1, list2))
print(answer)
print(answer2)

######################################################################################################################################################################
#Given a person variable:
#Create a dictionary called answer , that makes each first item in each list a
#  key and the second item a corresponding value.
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer3 = dict(person)
answer4 = {thing[0]: thing[1] for thing in person}
answer5 = {k:v for k,v in person}
print(answer3)

#Create a dictionary with the key as a vowel in the alphabet and the value as 0.
# Your dictionary should look like this {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}.
#Do this programmatically (using a dict comprehension or dict method) rather than hard coding the answer!

answer6 = {}.fromkeys("aeiou", 0)
answer7 = {char : 0 for char in "aeiou"}
print(answer6,answer7)

######################################################################################################################################################################

#Python has a function called chr() that will return a string if you provide the corresponding integer ASCII code.  For example:
#chr(65)  will return  'A'
#chr(66)  will return  'B'
#All the way up to:
#chr(90)  will return  'Z'
#Your task is to create dictionary that maps ASCII keys to their corresponding letters.
#  Use a dictionary comprehension and chr() . Save the result to the answer variable. You only need to care about capital letters (65-90).

answer8 = {num : chr(num) for num in range(65,91)}
print(answer8)