################# TUPLE UNPACKING #################
def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = (1,2,3,4,5,6,7)

print(sum_all_values(*nums))


################# DICTIONARY UNPACKING #################
def display_names(first,second):
    return f"{first} says hi to {second}"

names = {"first":"Colt","second":"Rusty"}

print(display_names(**names))


