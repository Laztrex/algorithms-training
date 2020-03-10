# A. A+B 1
# Даны два числа A и B
# Вам нужно вычислить их сумму A + B.
# В этой задаче для работы с входными и выходными данными вы можете использовать и файлы и потоки на ваше усмотрение.

import sys
#
# n = sys.stdin.readline().split()
#
#
# def gen_sum(a, b):
#     return int(a) + int(b)
#
#
# print(gen_sum(n[0], n[1]))

# B. A+B 2


# def open_file(file):
#     with open(file, 'r') as fl:
#         data = fl.readline().split()
#         return data[0], data[1]
#
#
# def write_file(data):
#     with open('output.txt', 'w') as fl:
#         fl.write(data)
#
#
# def gen_sum(a, b):
#     summ = int(a) + int(b)
#     return str(summ)
#
#
# write_file(gen_sum(*open_file('input.txt')))

# C. A+B 3


# Задача лотерейные билеты

from functools import reduce

print(reduce(lambda x, y: x * y, range(32, 37)) / reduce(lambda x, y: x * y, range(1, 6)))
