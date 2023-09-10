def stars(num):
    for a in range(num):
        for b in range(num):
            if a == b or a + b == num - 1:
                print("+", end = " ")
            else:
                print(" ", end = " ")
        print(" ")
stars(9)