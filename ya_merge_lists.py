# Даны k отсортированных в порядке неубывания массивов неотрицательных целых чисел, каждое из которых не превосходит
# 100. Требуется построить результат их слияния: отсортированный в порядке неубывания массив, содержащий все элементы
# исходных k массивов.
#
# Длина каждого массива не превосходит 10 ⋅ k.
#
# Постарайтесь, чтобы решение работало за время k ⋅ log(k) ⋅ n, если считать, что входные массивы имеют длину n.
#
# Формат ввода
# Первая строка входного файла содержит единственное число k, k ≤ 1024.
#
# Каждая из следующих k строк описывает по одному массиву. Первое число каждой строки равняется длине
# соответствующего массива, оставшиеся числа этой строки описывают значения элементов этого же массива. Элементы
# массивов являются неотрицательными целыми числами и не превосходят 100.
#
# Формат вывода
# Выходной файл должен содержать отсортированный в порядке неубывания массив, содержащий все элементы исходных массивов.

# Пример
# Ввод	                                      Вывод
# 4                        1 2 4 8 16 20 26 42 58 61 64 65 69 84 86 88 96 96
# 6 2 26 64 88 96 96
# 4 8 20 65 86
# 7 1 4 16 42 58 61 69
# 1 84
import sys


def sorted_return(my_list):
    new_list = list(my_list)
    merge(new_list, my_list, 0, len(my_list))


def merge(massive, result, start, end):
    if end - start < 2:
        return
    if end - start == 2:
        if result[start] > result[start + 1]:
            result[start], result[start + 1] = result[start + 1], result[start]
        return

    middle = (start + end) // 2
    merge(result, massive, start, middle)
    merge(result, massive, middle, end)

    i = start
    j = middle
    idx = start
    while idx < end:
        if j >= end or (i < middle and massive[i] < massive[j]):
            result[idx] = massive[i]
            i += 1
        else:
            result[idx] = massive[j]
            j += 1
        idx += 1


n = sys.stdin.readline().strip()
a = []
for _ in range(int(n)):
    a += [int(i) for i in sys.stdin.readline().split()][1:]
sorted_return(a)
for i in a:
    print(i, end=' ')

# int_list = []
# t = [0] * 101
# n = int(sys.stdin.readline().strip())
# for i in range(int(n)):
#     s = sys.stdin.readline().strip()
#     try:
#         num = int(s[:s.find(' ')])
#     except ValueError:
#         continue
#     for index, value in enumerate(s.split(' ')):
#         if index == 0:
#             continue
#         elif index == num + 1:
#             break
#         try:
#             t[int(value)] += 1
#         except ValueError:
#             pass
#     del s
#
# for i in range(101):
#     if t[i]:
#         print(' '.join([str(i)] * t[i]), end=' ')