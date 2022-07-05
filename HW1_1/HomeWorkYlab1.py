# Домашнее задание урок №1
# Воронов Андрей
from cmath import inf
import itertools


def range_a_to_b(a,b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def all_range_updata(list_place):
    index_value = 0
    a = str()
    text = str()
    answer = 0
    for arg in list_place:
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
        if index_value == len(list_place):
            step = range_a_to_b(a, a_last)
            answer += step
            text += f'{a_last}[{answer}] = {answer}'
            return answer, text


min_value = float(inf)
options = []
index = 0
list_place = [(0, 2), (2, 5), (5, 2), (6, 6), (8, 3)]
roads = []
roads_gener = itertools.permutations(list_place[1:], len(list_place) - 1)
for road in roads_gener:
    road_list = []
    road_list.append(list_place[0]) 
    for point in road:
        road_list.append(point) 
    roads.append(road_list)
for road in roads:
    answer = all_range_updata(road)
    if answer[0] <= min_value:
        min_value = answer[0]
for road in roads:
    answer = all_range_updata(road)
    if answer[0] == min_value:
        index += 1
        print('Вариант: ' + str(index))
        print(answer[1])

