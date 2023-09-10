list1 = [1,2,3]
list2 = [i*5 if i == 3 else i for i in list1]
list3 = [i*5 for i in list1 if i == 3]
list4 = [i*5 if i == 3 else i for i in list1 if i>1]
print(list2)
print(list3)
print(list4)

results = []

for i in list1:
    if i > 1:
        if i == 3:
            i = i*5
        else:
            i
        results.append(i)

print(results) 

sum = sum(list1)
print(sum)

def myFunction():
    print("hello world")

myFunction()