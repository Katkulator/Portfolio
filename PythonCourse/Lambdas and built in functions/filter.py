nums = [1,2,3,4,5,6,7]
evens = list(filter(lambda num: num % 2 == 0, nums))
print(evens)

names = ["matko", "matija", "šimun", "marija", "stjepan", "anthony"]
a_names = list(filter(lambda name: name[0] == "a", names))
print(a_names)


users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": []},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#extract inactive users using filter:
inactive_users = list(filter(lambda u: not u['tweets'], users))

#extract inactive users using list comprehension:
inactive_users2= [user for user in users if not user["tweets"]]

# extract usernames of inactive users with map and filter:
usernames = list(map(lambda user: user["username"].upper(), 
	filter(lambda u: not u['tweets'], users)))

# extract usernames of inactive users with list comprehension
usernames2 = [user["username"].upper() for user in users if not user["tweets"]]