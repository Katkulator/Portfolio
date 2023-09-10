#abs() - return the absolute value of a number. Can be int or float

print(abs(-5))
print(abs(-2.5))

#sum()  - takes an iterable and an optional start
#       - returns the sum of start and the items of an iterable from left to right and returns total
#       - start defaults to 0

print(sum([1,2,3]))
print(sum([1,2,3], 10)) #starts at 10 and adds all the other numbers to 10
print(sum([1,2,3], -6)) 

#round() - return number rounded to ndigits precision after the decimal poing
#        -  if ndigits is omitted or is None it returns the nearest int to its input

print(round(2.6589))        
print(round(2.6589, 3))        