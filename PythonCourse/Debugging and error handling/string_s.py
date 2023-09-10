from datetime import datetime
start_time = datetime.now()
def solution(test):
    test_up = list(test.upper())
    count_b = test_up.count("B")
    count_a = test_up.count("A")
    count_l = test_up.count("L") // 2
    count_o = test_up.count("O") // 2
    count_n = test_up.count("N")

    return min(count_b,count_a,count_l,count_o,count_n)

print(solution("balloonballoonballll"))

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))



   

    



    





