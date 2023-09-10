instructor = {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses" : 4,
    "favourite_language" : "Python",
    "is_hilarious" : False,
    44 : "his_favourite_number",

}

"""for value in instructor.values():
    print(value)

for key in instructor.keys():
    print(key)

for item in instructor.items():
    print(item)

for k,v in instructor.items():
    print (f"key is:{k}, and value is:{v}") """

#Given the provided dictionary of donations:
#Use a loop to calculate the total value of the donations.
# Save the result to a variable called total_donations 

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

#1. rješenje
#total_donations = 0
 
#for donation in donations.values():
 #total_donations += donation

#2.rješenje
#total_donations = sum(donation for donation in donations.values())

#3.rješenje - NAJBOLJE
#total_donations = sum(donations.values())
#print(total_donations)

if "name" in instructor:
    print("there is name in instructor")

if 4 in instructor.values():
    print("yes, there is 4 in the dictionary")