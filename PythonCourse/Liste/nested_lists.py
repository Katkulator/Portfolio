#nested_list = [[1,2,3], [4,5,6], [7,8,9]]
#print(len(nested_list)) - len = 3

#nested_list = [[1,2,3], [4,5,6], [7,8,9]]
#print(nested_list[0][1])
#print(nested_list[2][1])
#print(nested_list[1][-1])

###PRINTING VALUES IN NESTED LISTS####
#for l in nested_list:
    #for val in l:
        #print(val)
#
#coords = [[10.423, 9.132], [37.212, -14.092], [21.367, 32.572]]
#for loc in coords:
    #for coord in loc:
        #print(coord)
        

#[[print(val) for val in l] for l in nested_list]

board = [[num for num in range(1,4)] for val in range(1,5)]
print(board)

matrix = [["X" if num %2 !=0 else "O" for num in range(1,4)] for val in range(1,4)]
print(matrix)

asterix = [["*" for char in range(1,4)] for x in range(1,4)]
#ili
asterix2 = [["*" for char in [1,2,3]] for x in range(1,5)]

print(asterix)
print(asterix2)
