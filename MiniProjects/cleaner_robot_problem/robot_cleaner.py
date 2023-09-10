def count_tiles(grid):
    x = 0
    y = 0
    x_len = len(grid[0]) - 1
    y_len = len(grid) - 1
    path = []
    direction = 1

    def start():
        nonlocal x, y, direction
        while (0 <= x <= x_len and 0 <= y <= y_len):
            tile = (x, y, direction)
            if tile in path:
                break

            path.append(tile)
            check_direction_change()

            match direction:
                case 1:
                    x += 1
                case 2:
                    y += 1
                case 3:
                    x -= 1
                case 4:
                    y -= 1

    def check_direction_change():
        nonlocal x, y, direction
        flag = "X"

        match direction:
            case 1:
                if x + 1 <= x_len:
                    flag = grid[y][x+1]
            case 2:
                if y + 1 <= y_len:
                    flag = grid[y+1][x]
            case 3:
                if x - 1 >= 0:
                    flag = grid[y][x-1]
            case 4:
                if y - 1 >= 0:
                    flag = grid[y-1][x]

        if flag != ".":
            change_direction()
            check_direction_change()

    def change_direction():
        nonlocal direction
        match direction:
            case 4:
                direction = 1
            case _:
                direction += 1

    start()
    clean = set([(char[0], char[1]) for char in path])
    print(clean)
    return len(clean)


print(count_tiles(["...X..", "....XX", "..X..."])) #6
print(count_tiles(["....X..", "X......", ".....X.", "......."])) #15
print(count_tiles(["...X.", ".X..X", "X...X", "..X.."])) #9
