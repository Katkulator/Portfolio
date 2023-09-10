def sum_all_nums(num1,num2,num3):
    return num1+num2+num3

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num
    return total
print(sum_all_nums(4,6,8,9,15,10))

def ensure_correct_info(*info):
    if "Colt" in info and "Steele" in info:
        return "Welcome back Colt!"
    return "I don't know who you are"
    
ensure_correct_info("Colt", "Steele")

#Define a function contains_purple  that accepts any number of arguments.
# It should return True  if any of the arguments are "purple" (all lowercase).
# Otherwise, it should return False

def contains_purple(*value):
    if "purple" in value:
        return True
    return False

contains_purple(25, "purple")
contains_purple("green", False, 37, "blue", "hello world")
contains_purple("a", 99, "blah blah blah", 1, True, False, "purple")