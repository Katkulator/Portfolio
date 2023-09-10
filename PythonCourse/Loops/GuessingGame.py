#user guesses, if they guess correct, tell them they won
#otherwise tell them if they are too gihg or too low
#while they are wrong
#BONUS - let player play again if they want

import random

random_number = random.randint(1,10)
guess = None

# while guess != random_number:
# 	guess = int(input("Guess a number between 1 and 10: "))
# 	if guess < random_number:
# 		print("Too low!")
# 	elif guess > random_number:
# 		print("Too high!")
# 	else:
# 		print("YOU WON!")

while True:
	guess = int(input("Pick a random number from 1 to 10: "))
	if guess < random_number:
		print("Too low, try again!")
	elif guess > random_number:
		print("Too high, try again!")
	else:
		print("YOU WON!!")
		play_again = input("Do you want to play again? (y/n): ")
		if play_again == "y":
			random_number = random.randint(1,10)
			guess = None
		else:
			print("Thank you for playing!")
			break
