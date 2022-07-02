# Домашнее задание урок №1
# Воронов Андрей
def range_a_to_b(a,b):
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


def all_range(post, point_1, point_2, point_3, point_4):
    step_1 = range_a_to_b(post, point_1)
    step_2 = range_a_to_b(point_1, point_2)
    two_step = step_1 + step_2
    step_3 = range_a_to_b(point_2, point_3)
    three_step = two_step + step_3
    step_4 = range_a_to_b(point_3, point_4)
    four_step = three_step + step_4
    step_5 = range_a_to_b(point_4, post)
    five_step = four_step + step_5
    text = f'{str(post)} -> {str(point_1)}[{step_1}] \
-> {str(point_2)}[{two_step}] -> {str(point_3)}[{three_step}] -> {str(point_4)}[{four_step}] \
-> {str(post)}[{five_step}] = {five_step}'
    return  five_step, text

min = 10000
options = []
index = 0
a = (0, 2)
b = (2, 5)
c = (5, 2)
d = (6, 6)
e = (8, 3)
roads = [(a, b, c, d, e),
        (a, b, c, e, d),
        (a, b, d, c, e),
        (a, b, d, e, c),
        (a, b, e, c, d),
        (a, b, e, d, c),
        (a, c, b, e, d),
        (a, c, b, d, e),
        (a, c, d, e, b),
        (a, c, d, b, e),
        (a, c, e, b, d),
        (a, c, e, d, b),
        (a, e, b, c, d),
        (a, e, b, d, c),
        (a, e, c, b, d),
        (a, e, c, d, b),
        (a, e, d, b, c),
        (a, e, d, c, b),
        (a, d, e, b, c),
        (a, d, e, c, b),
        (a, d, b, e, c),
        (a, d, b, c, e),
        (a, d, c, e, b),
        (a, d, c, b, e),]
for a, b, c, d, e in roads: # Первый раз вызываю функцию необходимо найти наименьшую длину пути
    ansver = all_range(a, b, c, d, e)
    if ansver[0] <= min:
        min = ansver[0]
for a, b, c, d, e in roads: # Второй раз вызываю функцию ищим совподаюшие длины путей
    ansver = all_range(a, b, c, d, e)
    if ansver[0] == min:
        index += 1
        print('Вариант: ' + str(index))
        print(ansver[1])
