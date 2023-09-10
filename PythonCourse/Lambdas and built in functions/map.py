people = ["Matjaž", "Smajo", "Robs", "Micara"]
upper = list(map(lambda item: item.upper(),people))
print(upper)

nums = [1,2,3,4,5,6]
doubles = map(lambda num: num * 2, nums)
print(list(doubles))

names = [
    {"first":"Colt", "last":"Steele"},
    {"first":"Rusty", "last":"Steele"},
    {"first":"Blue", "last":"Steele"}
]
first_names= list(map(lambda name: name["first"], names))
print(first_names)