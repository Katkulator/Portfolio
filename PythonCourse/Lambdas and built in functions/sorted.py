nums = [1,46,12,3,10,53,14]
print(sorted(nums))
print(sorted(nums, reverse=True))

#radi i na Tuplu - ali returna listu
print(sorted((1,18,3,15,26)))

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#print(sorted(users, key=lambda user: user["username"]))
#print(sorted(users, key=lambda user: len(user["username"])))
print(sorted(users, key=lambda user: len(user["tweets"]), reverse=True))


songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

print(sorted(songs, key=lambda song: song["playcount"]))
print(sorted(songs, key=lambda song: len(song["title"])))