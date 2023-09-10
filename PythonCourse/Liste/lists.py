########Creating Lists#########

	#demo_lists = ["a", 1.45, True, 7]
	#len (demo_lists) #printa koliko ima elemenata u listi

	#r = range(1, 10)
	#list(r) #ispiše range u listi, svaki broj je jedan element

	#tasks = list(range(1, 4)) možemo storati range u listu
	#print(tasks)

########Accesing data in Lists#########
	# friends = ["Ashley", "Matt", "Michael"] - prvi item je broj 0, 
	#  drugi je broj 1. redni broj u listu se zove INDEX
	#print(friends[0]) - printa Ashley
	#print(friends[1]) - printa Matt
	#print(friends[2]) - printa Michael

#PRINTANJE ITEMA UNAZAD
	#print(friends[-3]) - printa Ashley 
	#print(friends[-2]) - printa Matt
	#print(friends[-1]) - printa Michael

#PROVJERA DA LI JE ITEM U LISTI
	#"Ashley" in friends - vrijednost je True
	#"Colt" in friends - vrijednost je False

	#if "Ashley" in friends:
		#print("You have good friends")

#MJENJANJE ELEMENATA U LISTI
	#people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
	#people[0] = "Hannah"
	#people[4] = "Jeffrey"
	#people[5] = "Aparna"

#PRINTANJE FOR PETLJA
	#numbers = [1, 2, 3, 4]
	#for number in numbers:
		#print(number)

#PRINTANJE WHILE PETLJA
# colors = ["purple", "emerald", "teal", "black",]
# index = 0  #i
# while index < len(colors): dok je index manji od dužine lista (3)
# 	print(colors[index])
# 	index += 1
# while index < len(colors):
# 	print(f"{index}: {colors[index]}")
# 	index += 1
# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# # Define your code below:
# result = ''
# for s in sounds:
#     result += s
# result = result.upper()
# print(result)

# sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# result = ""

# for s in sounds:
# 	result += s.upper()
# print(result)

#####List methods####
#metode su slične kao funkcije

####APPEND####
	#.append dodaje item u listu - dodaje samo 1 item
	# first_list = [1, 2, 3, 4]
	# first_list.append(5)
	# print(first_list) - [1, 2, 3, 4, 5]

####EXTEND####
	#.extend dodaje više itema u listu
	# first_list = [1, 2, 3, 4]
	# first_list.extend = ([5, 6, 7, 8)

####INSERT####
   	#.insert dodaje item na određeno mjesto u listu
   	# first_list = [1, 2, 3, 4]
	# first_list.insert = (2, "hello") - [1, 2, hello, 3, 4]
    #                      ^dodaje na 2. mjesto u listu 


# Initially create an empty list called instructors
#instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
#instructors.extend(["Colt", "Blue", "Lisa"])
# Run the tests to make sure you've done this correctly!
#print(instructors)

####CLEAR####
	#.clear - briše sve iteme iz liste
	# lista = ["ručnici", "wc papir", "omekšivač"]
	# lista.clear()
	# print(lista) - []

####POP####
	#.pop - briše indexirani item iz liste, ako ne stavimo index, odbirše zadnji item
	# lista = ["ručnici", "wc papir", "omekšivač"]
	# lista.pop(1) - index itema u listi
	# print(lista) - ["ručnici", "omekšivač"]

	# lista = ["ručnici", "wc papir", "omekšivač"]
	# lista.pop() - ako nema indexa briše zadnji item
	# print(lista) - ["ručnici", "wc papir"]
	# last_item = lista.pop() - možemo spremiti .pop u varijablu i prinati
	# print(last_item)

####REMOVE####
	#.remove - briše prvi item sa vrijednosti x
	# lista = [1, 2, 3, 4, 5, 5, 5,]
	# lista.remove(2)
	# print(lista) - [1, 3, 4, 5, 5]
	
	# lista = [1, 2, 3, 4, 5, 5, 5,]
	# lista.remove(5)
	# print(lista) - [1, 2, 3, 4, 5, 5]


####INDEX####
	#.index - returns the index of the specified item
	# 	numbers= [5, 6, 7, 8, 9, 10]
	# 	numbers.index(6) - 1
	# 	numbers.index(9) - 4
	# can specify start and end
	# 	numbers= [5, 5, 6, 7, 5, 8, 8, 9, 10]
	# 	numbers.indes(5) - 0
	# 	numbers.index(5, 1) - 1 -> find index of 5 after index of 1
	# 	numbers.index(5, 2) - 4
	# 	numbers.index(8, 6, 8) - 6 -> find index of 8 between index of 6 and 8
	# 	names = ["Colt", "Blue", "Arya", "Lena", "Colt", "Selena", "Pablo"]
	# 	names.index("Colt", 1) - 4 


####COUNT####
	#.count - returns the number of times x appears in the list
	 	# numbers = [1, 2, 3, 4, 3, 2, 1, 4, 10, 2]
	 	# numbers.count(2) - 3
	 	# numbers.count(21) - 0
	 	# numbers.count(3) - 2


####REVERSE####
	#.reverse - reverses the elements of the list(in-place)
	 # 	numbers = [1, 2, 3, 4, 5, 6]
		# numbers.reverse()
		# print(numbers) - [6, 5, 4, 3, 2, 1]


####SORT####
	#.sort - sort the elements of the list(in-place)
	 # 	numbers = [6, 2, 1, 3, 4, 5]
		# numbers.sort()
		# print(numbers) - [1, 2, 3, 4, 5, 6]


####JOIN####
	#.join - joins the strings in the list
	 # words = ["Coding", "is", "fun"]
	 # " ".join(words) - Coding is fun
	  # names = ["Colt", "Blue", "Arya", "Lena", "Colt", "Selena", "Pablo"]
	  # friends = ", ".join(names) - Colt, Blue, Arya, Lena...


#####################SLICING#####################

#make new lists using slices of the old lsit!

#some_list[start:end:step]

#start	
	# first_list = [1, 2, 3, 4]
	# first_list[1:] - [2,3,4]
	# first_list[3:] - [4]

	# first_list[-1] - [4] - slajsanje odozada
	# first_list[-4] - [2, 3, 4]

#end - exclusive, ne ubraja zadnji index
	# first_list = [1, 2, 3, 4]
	# first_list[:2] - [1, 2]
	# first_list[:4] - [1, 2, 3, 4] - nema indexa 4
	# first_list[1:3] - [2, 3] 

	#colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
	#print(colors[:5])
	#print(colors[2:4]) - yellow, green

#step - number to count at a time, same as step with range
	#  - step of 2 (1,3,5...)
	# first_list = [1, 2, 3, 4, 5, 6]
	# first_list[1::2] - 2,4,6
	# first_list[::2] - 1,3,5

#negativne vrijednosti
	# first_list[1::-1] - 2,1
	# first_list[:1:-1] - 6,5,4,3
	# first_list[2::-1] - 3,2,1

	# string = "This is fun!"
	# print(string[::-1])

	# numbers = [1,2,3,4,5]
	# numbers[1:3] = ["a", "b", "c"]
	# print(numbers)

	# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
	# colors[5][::-1] - ogidni

	# "helllllo"[0] - h
	# "helllllo"[:4] - hell
	# "helllllo"[::3] - hllo

#swapping values

""" names = ["James", "Michelle"]
names[0], names[1] = names [1], names [0]
print(names) - Michelle, James """

answer=[[num for num in range(0,3)]for val in range(1,4)]
print(answer)