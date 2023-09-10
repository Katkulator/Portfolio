def sum_pairs(ints, s):
    mylist = set()
    for num in ints:
        mylist.add(num)
        first_num = s - num
        if first_num in mylist:
            return [first_num, num]


print(sum_pairs([11, 3, 7, 5], 10))
