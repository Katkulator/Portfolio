alphabet = ("a", "b", "c", "d")
print(type(alphabet))

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
print(months[9]) #accesamo isto kao i dictovima

locations = {
    (30.2451,45.8761) : "Tokio office",
    (41.5436,56.7658) : "New York office",
    (43.9486,15.5878) : "San Francisco office"
}


for item in locations.items():
    print(item)

cat = {"name":"biscuit", "age":0.5, "color":"black"}
print(cat.items())

