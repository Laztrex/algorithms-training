# Сборник задач по курсу Математическая статистика от CSC на Stepik.org.
# =============
# 1.4. Задача:
# =============
# По предложенной выборке найдите значения первой, третьей и седьмой порядковых статистик.
# Формат ответа: значения через запятую с пробелом (2 знака после запятой)
# Sample Input:
# 2.36, 3.11, 7.1, 4.32, -0.77, -0.29, 0.03, 2.89
#
# Sample Output:
# -0.77, 0.03, 4.32
import os
import sys

with open(os.path.normpath(f'{sys.path[1]}/files/dataset_26210_4.txt'), mode='r', encoding='utf-8') as sample_file:
    sample_list = [float(string) for string in sample_file.readline().strip().split(',')]
    for i, j in enumerate(sorted(sample_list)):
        if i == 0 or i == 2 or i == 6:
            print(f'{i + 1}-ая порядковая статистика - {j}')
