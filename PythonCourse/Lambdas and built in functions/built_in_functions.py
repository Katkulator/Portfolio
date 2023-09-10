#ALL - return True all elements in an iterable are truthy or if the iterable is empty
people = ["Christie","Chris","Calum","Colt","Christian"]
print(all(name[0] == "C" for name in people)) #True

nums = [2,40,60,26,19]
print(all(num % 2 == 0 for num in nums)) #False

#ANY - return True if ANY element of the iterable is truthy, return False if the iterable is empty
print(any([num % 2 == 1 for num in nums])) #True
print(any([num % 2 == 3 for num in nums])) #False