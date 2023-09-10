# {__:__ for __ in __}
numbers = dict(first = 1, second = 2, third = 3)
squared_numbers = {key : value **2 for key,value in numbers.items()}
print(squared_numbers)

numbers_sq = {num: num **2 for num in [1,2,3,4,5]} # num: je key, a value je (num) taj isti broj na kvadrat
print(numbers_sq)

str1 = "ABC"
str2 = "123"
combo = {str1[i]:str2[i] for i in range(0,len(str1))} # i je broj koji počinje od nule i ide do broja koji je dužina stringa znači 3..NE KONTAM JEBENO
print(combo)
print(len(str1))

instructor = {"name" : "colt", "city" : "san francisco", "color" : "yellow"}
yelling_instructor = {k.upper() : v.upper() for k,v in instructor.items()}
yelling_instructor2 = {k.upper() if k is "color" else k : v for k,v in instructor.items()}
print(yelling_instructor2)

######CONDITIONAL LOGIC#########

num_list = [1,2,3,4]
num_dict = {num:("even" if num %2 == 0 else "odd") for num in num_list}
print(num_dict)