# ask for age
# 18-21 wristband
# 21 + drink, normal entry
# too young, sorry


# age = input("What is your age: ")
# if age != "": # može ići i if age: (ako ima išta u age)
	
# 	age = int(age)
	
# 	if age >= 18 and age < 21:
# 		print ("You can enter but get a wristband")
# 	elif age >= 21:
# 		print ("You can enter and drink booze!")
# 	else:
# 		print("FUCK OFF!!")
# else: 
# 	print("please state your age!")


age = input("What is your age: ")
if age != "": # može ići i if age: (ako ima išta u age)
	age = int(age)
	if age >= 21:
		print ("You can enter and drink booze!")
	elif age >= 18:
		print ("You can enter but get a wristband")
	else:
		print("FUCK OFF!!")
else: 
	print("please state your age!")