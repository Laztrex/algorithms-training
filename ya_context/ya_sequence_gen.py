# D. Генерация скобочных последовательностей

# Дано целое число n. Требуется вывести все правильные скобочные последовательности длины 2 ⋅ n, упорядоченные
# лексикографически (см. https://ru.wikipedia.org/wiki/Лексикографический_порядок).
#
# В задаче используются только круглые скобки.
#
# Желательно получить решение, которое работает за время, пропорциональное общему количеству правильных скобочных
# последовательностей в ответе, и при этом использует объём памяти, пропорциональный n.
#
# Формат ввода
# Единственная строка входного файла содержит целое число n, 0 ≤ n ≤ 11
#
# Формат вывода
# Выходной файл содержит сгенерированные правильные скобочные последовательности, упорядоченные лексикографически.

# Пример 1
# Ввод	Вывод
# 2     (())
#       ()()

# Пример 2
# Ввод	Вывод
# 3     ((()))
#       (()())
#       (())()
#       ()(())
#       ()()()
import sys


def gen(n, counter_open=0, counter_close=0, string=''):

    if counter_open + counter_close == 2 * n:
        print(string)
    if counter_open < n:
        gen(n, counter_open=counter_open + 1, counter_close=counter_close, string=string+'(')
    if counter_open > counter_close:
        gen(n, counter_open=counter_open, counter_close=counter_close + 1, string=string+')')


gen(int(sys.stdin.readline()))
# def next_scoba(string):
#     count_open = 0
#     count_close = 0
#     for i in range(len(string)):
#         if string[i] == '(':
#             count_open += 1
#             if count_close > count_open:
#                 breakpoint()
#         else:
#             count_close += 1
#
#     string = string[0: len(string) - count_open - count_close]
#     if string == '':
#         return "No Solution"
#     else:
#         string = string + ')'
#         for j in range(count_open):
#             string = string + '('
#         for j in range(count_close):
#             string = string + ')'
#         return string
#
#
# def order(n):
#     string = ''
#     for j in range(n):
#         string = string + '('
#     for j in range(n):
#         string = string + ')'
#
#     print(string)
#     while next_scoba(string) != 'No Solution':
#         print(next_scoba(string))
#     return
#
#
# order(5)


