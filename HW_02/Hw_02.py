import random
import math

def make_random_queens_configuration():
    conf = []
    while len(conf) < 8:
        temp = [random.randint(1,8), random.randint(1,8)]
        if temp not in conf:
            conf.append(temp)
    return conf

def is_queens_check_ok(i, j, set):
    result = True
    for num in range(0,len(set)):
        temp = set[num]
        if temp[0] == i and temp[1] == j:
            result = False
            break
        if (math.fabs(temp[0]-i)) == (math.fabs(temp[1]-j)):
            result = False
            break
    return result

def check(list_01):
    for i in range(9):
        for j in range(9):
            if not is_queens_check_ok(i, j, list_01):
                return 0
    return 1

def print_configuration(list_01):
    t = [ ['0']*8 for i in range(8)]
    for i in range(len(list_01)):
        temp = list_01[i]
        t[temp[0]-1][temp[1]-1] = '*'
    print(*t, sep='\n')

#
#
# list_01 = make_random_queens_configuration()
# check(list_01)
# print(*list_01)
# print_configuration(list_01)


