names = ("Colt", "Rusty", "Lassie", "Blue")

for name in names:
    print(name)

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

i = len(months) -1
while i >= 0:
    print(months[i])
    i -= 1


#####Methods####

x = (1,2,3,3,3)
print(x.count(3))

print(x.index(1))
print(x.index(3))


nums = (1,2,3,(4,5),6,7)
print(nums[3][0])
print(nums[0:4])