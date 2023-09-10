#add - adds an element to a set...if element is already in the set, the set doesn't change
s = {1,2,3,4}
s.add(5)
print(s)
s.add(5) #duplicate element..set doesn't change
print(s)

#remove - removes a value from a set...returns a KeyError if value isn't found
#discard - it's same as remove but doesn't return a KeyError if the value isn't found

set = {1,2,3,4,5,6,7}
set.remove(5)
print(set)
print(set.discard(5))


#copy - makes a copy of the set

set2 = {1,2,3,4,5,6}
another_set2 = set2.copy()
print(set2 is another_set2) #False

#clear - removes all the contents from the set

set2.clear()
print(set2)

#Set Math
math_students = {"Mathew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane","Mathew", "Charlotte", "Mesut", "Oliver", "James"}

#set union - | - combines two sets with no duplicates
print(math_students | biology_students)

#set intersection - & -  set of elements who are in both of the sets
print(math_students & biology_students)

#set difference - - - computes differences between two or more sets
print(math_students - biology_students)