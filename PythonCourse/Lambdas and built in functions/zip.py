first_zip = zip([1,2,3,4], [5,6,7,8])
print(dict(first_zip))
print(list(first_zip)) # ne printa ovaj zato što se first zip ispraznio

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
words = ["hi", "lol", "lmao", "roflmao", "rofl"]
#nums3 = zip(nums1, nums2)
combined = zip(nums1, nums2, words)
print(list(combined))

##UNPACKING##
five_by_two = [(0,1), (1,2), (2,3), (3,4), (4,5)]
print(list(zip(*five_by_two)))


##MORE COMPLEX ZIP##
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["dan", "ang", "kate"]
#final_grades = [pair for pair in zip(midterms, finals)] # [(80, 98), (91, 89), (78, 53)]
#final_grades = [max(pair) for pair in zip(midterms, finals)] #[98, 91, 78]
#final_grades = {pair[0] : max(pair[1], pair[2]) for pair in zip(students, midterms, finals)} #{'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
    zip(
        students, 
        map(lambda pair: max(pair),
            zip(midterms, finals)
            )
        )
    )
print(final_grades)