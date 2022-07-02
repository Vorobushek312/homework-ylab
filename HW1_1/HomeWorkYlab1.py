# Домашнее задание урок №1
# Воронов Андрей
from cmath import inf
import itertools


def range_a_to_b(a,b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def all_range_updata(*args):
    index_value = 0
    a = str()
    text = str()
    answer = 0
    len_args = len(args)
    for arg in args:
        if index_value == 0:
            a = arg
            a_last = arg
            text += str(a)
        else:
            step = range_a_to_b(a, arg)
            answer += step
            text += f'{arg}[{answer}]'
            a = arg
        text += ' -> '
        index_value += 1
        if index_value == len_args:
            step = range_a_to_b(a, a_last)
            answer += step
            text += f'{arg}[{answer}] = {answer}'
            return answer, text


min_value = float(inf)
options = []
index = 0
a = (0, 2)
b = (2, 5)
c = (5, 2)
d = (6, 6)
e = (8, 3)
roads = []
roads_gener = itertools.permutations([b,c,d,e], 4)
for road in roads_gener:
    road_list = []
    road_list.append(a) 
    for point in road:
        road_list.append(point) 
    roads.append(road_list)
for road in roads:
    answer = all_range_updata(road[0], road[1], road[2], road[3], road[4])
    if answer[0] <= min_value:
        min_value = answer[0]
for road in roads:
    answer = all_range_updata(road[0], road[1], road[2], road[3], road[4])
    if answer[0] == min_value:
        index += 1
        print('Вариант: ' + str(index))
        print(answer[1])
