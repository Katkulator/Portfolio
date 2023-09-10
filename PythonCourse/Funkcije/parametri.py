def square_of_num(num):
    return num**2
print(square_of_num(16))


def sum_of_nums(a,b):
    return a + b
print(sum_of_nums(7,3))

def multiply(first,second):
    return first * second
print(multiply(7,3))

###########################DEFAULT PARAMETERS###########################
def exponent(num,power):
    return num**power
print(exponent(2,3))
#print(exponent(2)) - error jer nema drugog argumenta

def exponent2(num, power=2):
    return num**power
print(exponent2(2,3)) #3 overrida default value parametra power
print(exponent2(2)) # printa 4 jer je default value parametra 2


def add(a,b):
    return a+b
print(add()) #doesn't work

def add2(a=10, b=20):
    return a+b
print(add2()) #radi jer smo mu zadali default parametre
