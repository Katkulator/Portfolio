#MIN - return the largest item in iterable or the largest of two or more arguments
max([1,3,4,5])
max("awesome")
max({1:"a", 2:"b", 3:"c"})

names = ["Arya", "Samson", "Dora", "Tim", "Ollivander"]
print(max(len(name) for name in names)) #ispiše koliko slova ima najduži string - 10
print(max(names, key = lambda name: len(name)))
print(min(names, key = lambda name: len(name)))

songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

print(min(songs, key=lambda song: song["playcount"])["title"]) #daje nam samo ime najmanje puštane pjesme
print(max(songs, key=lambda song: song["playcount"]))