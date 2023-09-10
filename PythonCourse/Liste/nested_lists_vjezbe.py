#Using a nested list comprehension and range(), create a variable called answer  with the following value - [[0, 1, 2], [0, 1, 2], [0, 1, 2]] .
#To break it down...start by using range and a list comp to generate the list [0,1,2].
#And then repeat that whole thing 3 times in a nested list comp.
answer=[[num for num in range(0,3)] for val in range(1,4)]
print(answer)

#Using list comprehension, create a variable called answer with the following value :it's a 10x10 nested list. 
# 10 rows, each row contains the numbers 0-9. Your answer will be all on one giant line.
# #Use nested list comprehension and range() to accomplish this.
answer2 = [[num for num in range(0,10)] for val in range(0,10)]
print(answer2)

#Reverse a list
list1 = [100, 200, 300, 400, 500]
#list1 = list1[::-1]
list1.reverse()
print(list1)

#Concatenate two lists index-wise.Write a program to add two lists index-wise.
# Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element.
# any leftover items will get added at the end of the new list.

list2 = ["M", "na", "i", "Ke"]
list3 = ["y", "me", "s", "lly"]
list4 = [i + j for i, j in zip(list2, list3)]
print(list4)

#Given a list of numbers. write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
print([num**2 for num in numbers])