#clear - clears all keys and values in a dictionary
#d = dict(a=1,b=2,c=3)
#d.clear()
#print(d)

#copy - makes a copy of a dictionary
#c = d.copy()
#print(c)

#fromkeys - creates a key-value pairs from values separated by a comma

fromkeys_dict = {}.fromkeys("abcdefg", [1,2,3,4])
print(fromkeys_dict)

new_user = {}.fromkeys(["name", "score", "email", "profile bio"], "unknown")
print(new_user)

test = {}.fromkeys("phone", "unknown") #za svako slovo u phone će dodati value unknown
print(test)

#get - retrieves a key in an object and return None instead of a Key Error if the key doesnt exist
d = dict(a=1,b=2,c=3)
print(d.get("l"))
print(d.get("b"))

#pop - takes a single argument coresponding to a key and removes the key-value pair from the dictionary

d.pop("a")
print(d)

#popitem - removes a random key in dictionary - doesnt take a value

d.popitem()
print(d)

#update - updates keys and values in dictionary with another set of key-value pairs

first = dict(a=1, b=2, c=3, d=4, e=5)
second = {}

second.update(first)
second["a"] = "Amazing"
second.update(first)
print(second)

instructor = {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses" : 4,
    "favourite_language" : "Python",
    "is_hilarious" : False,
    44 : "his_favourite_number",

}

person = {"city" : "Našice"}
person.update(instructor)
person["name"] = "matko"
print(person)
person.update(instructor)
print(person)