############VJEŽBA 1###############

#Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list. 
##MOJE RJEŠENJE##
#names = ["Ellie", "Tim", "Matt"]
#answer = [name[0] for name in names]
#print(answer)
###cOURSE RJEŠENJE###
#answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
#ILI#
#answer = []
#for person in ["Elie", "Tim", "Matt"]:
#    answer.append(person[0])


#Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values. 
##MOJE RJEŠENJE##
#numbers = [1,2,3,4,5,6]
#answer2 = [num for num in numbers if num %2 == 0]
#print(answer2)
###cOURSE RJEŠENJE###
#answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]
#ILI#
#answer2 = []
#for num in [1,2,3,4,5,6]:
#    if num % 2 == 0:
#        answer2.append(num)





############VJEŽBA 2###############
#For all the numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
#answer = [num for num in range(1,101) if num %12 == 0]

############VJEŽBA 3###############
#Given the string "amazing", create a variable called answer, which is a list containing all the letters
#from "amazing" but not the vowels (a, e, i, o, and u).  The answer should look like: ['m', 'z', 'n', 'g'].

#answer = [char for char in "amazing" if char not in "a,e,i,o,u"]
#print(answer)