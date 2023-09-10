def count_squares(tiles):
    grid = [[y for y in x]for x in tiles]
    row_length = len(grid[0]) -1
    column_length = len(grid) -1
    row = 0
    column = 0
    next_row = 0
    next_column = 0
    path = set()
    clean = set()
    direction = 1
    
    
 
        
        
       

        
       
        
        print(path)
        return len(path)

print(count_squares(["...X..", "....XX", "..X..."]))  # Output should be 6

    




