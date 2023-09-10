#name = ""

#if name == "Arya Stark" :
	#print ("Valar Morghulis")
#elif name == "Jon Snow":
	#print ("You know nothing")
#else:
	#print("Carry on")





#from random import randint
#choice = randint(1,10)

#if choice == 7:
	#print("Lucky!!!")
#else:
	#print("Unlucky :(")





#from random import randint
#num = randint(1, 1000)

#if num % 2 != 0: != znači nije jednako
	#print("odd")
#lse:
	#print("even")




#print("What's your favourite color?")
#color = input()
#if color == "purple":
	#print("woow, mine too!1")
#else:
	#print("too bad lol")





#print("What's your favourite animal?")
#animal = input()

#if animal: ako varijabla postoji printaj ovo dolje
#	print(animal + " is my favourite too!")
#else:
#	print("you didn't say anything :(")
#age = 2
#2-8 2$
#65 5$
#10 dolara svi ostali
#if not ((age >= 2 and age <= 8) or age >= 65):
	#print("You pay 10$ ticket")
#else:
	#print("You're a child or senior")

# from random import randint                           
# x = randint(-100, 100)                             
# while x == 0:  # make sure x isn't zero             
#     x = randint(-100, 100)                                   
# y = randint(-100, 100)                               
# while y == 0:  # make sure y isn't zero             
#     y = randint(-100, 100)

# if x > 0 and y > 0:
# 	print("both positive")

# elif x < 0 and y < 0:
# 	print("both negative")

# elif x > 0 and y < 0:
# 	print("x is positive and y is negative")

# else:
# 	print("y is positive and x is negative")


from random import choice, randint

# randomly assigns values to these four variables
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)
# NO TOUCHING ======================================

calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!
if actually_sick and sick_days > 0:
	calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
	calling_in_sick = True
else:
	calling_in_sick = False




