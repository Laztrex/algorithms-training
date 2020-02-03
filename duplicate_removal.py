# Дан упорядоченный по неубыванию массив целых 32-разрядных чисел. Требуется удалить из него все повторения.
#
# Желательно получить решение, которое не считывает входной файл целиком в память, т.е., использует лишь константный
# объем памяти в процессе работы.
#
# Формат ввода
# Первая строка входного файла содержит единственное число n, n ≤ 1000000.
#
# На следующих n строк расположены числа — элементы массива, по одному на строку. Числа отсортированы по неубыванию.
#
# Формат вывода
# Выходной файл должен содержать следующие в порядке возрастания уникальные элементы входного массива.
#
# Пример 1
# Ввод	Вывод
# 5       2
# 2       4
# 4       8
# 8
# 8
# 8

# Пример 2
# Ввод	Вывод
# 5       2
# 2       8
# 2
# 2
# 8
# 8
import sys

my_iter = sys.stdin.readline().strip()

foo = 0
result = []
for _ in range(int(my_iter)):
    elem = sys.stdin.readline().strip()
    if elem != foo:
        result.append(elem)
    foo = elem

for num in result:
    print(num)


# def del_dub(data):
#     foo = []
#     for num in data:
#         start = data.count(num)
#         if start == 1:
#             yield num
#         elif num not in foo:
#             yield num
#             foo.append(num)
#         else:
#             continue
#
#
# with open('duplicate.txt', mode='r', encoding='utf8') as file:
#     my_list = file.read().split()
#     with open('out.txt', mode='a', encoding='utf8') as out:
#         for i in del_dub(my_list[1:]):
#             out.write(i + '\n')
