# Даны две строки строчных латинских символов: строка J и строка S. Символы, входящие в строку J, — «драгоценности»,
# входящие в строку S — «камни». Нужно определить, какое количество символов из S одновременно являются
# «драгоценностями». Проще говоря, нужно проверить, какое количество символов из S входит в J. Это разминочная
# задача, к которой мы размещаем готовые решения. Она очень простая и нужна для того, чтобы вы могли познакомиться с
# нашей автоматической системой проверки решений. Ввод и вывод осуществляется через файлы, либо через стандартные
# потоки ввода-вывода, как вам удобнее.

# Формат ввода:
# На двух первых строках входного файла содержатся две строки строчных латинских символов: строка J и
# строка S. Длина каждой не превосходит 100 символов.
# Формат вывода:
# Выходной файл должен содержать единственное число
# — количество камней, являющихся драгоценностями.

import sys

jewelry_list = sys.stdin.readline().strip()
stone_list = sys.stdin.readline().strip()

total_result = 0
for stone in stone_list:
    if stone in jewelry_list:
        total_result += 1

print(total_result)
