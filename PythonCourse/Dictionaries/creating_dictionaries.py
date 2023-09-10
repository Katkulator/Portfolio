#shopping_cart = {"name" : "cat litter", "quantity" : 1, "price" : 4.66}
#cat = {"name" : "Cica", "age" : 3, "isCute" : True}
#print(cat)
#drugi način za napraviti dictionary
#cat2 = dict(name = "Franjo", age = 2)
#print(cat2)

###ACCESSING INDIVIDUAL VALUES###

cat = {"name" : "Cica", "age" : 3, "isCute" : True}
print(cat["name"])
print(cat["age"])

#Declare a variable called full_name  that is equal to artist's first  and last  names with a space between.
# You must reference the values associated with those keys in the artist dictionary.

artist = {
    "first": "Neil",
    "last": "Young",
}

full_name = artist["first"] + " " + artist["last"]
full_name2 = "{} {}".format(artist["first"], artist["last"])
print(full_name)
print(full_name2)