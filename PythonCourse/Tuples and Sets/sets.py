s = set({1,2,3,4,5,5,5}) #sets can't have duplicate values
print(s)

s2 = {1,2,3,4,5}

4 in s #True

8 in s #False

numbers = {1,2,3,4}

for num in numbers:
    print(num)

cities = ["Našice", "Zagreb", "Osijek", "Našice", "Zagreb", "Zadar", "Split", "Split"]
print(list(set(cities)))