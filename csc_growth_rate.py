from sympy import limit, factorial, log, sqrt
from sympy.core.numbers import Infinity
from sympy.abc import *
import csv
from collections import defaultdict


def lapitale(my_func1, my_func2):
    return 1 if isinstance(limit(my_func1 / my_func2, z=n, z0='oo'), Infinity) else 0


# def csv_gen(i, j, data):
#     with open('total.py', 'a', newline='') as out_csv:
#         writer = csv.DictWriter(out_csv, delimeter=' ', fieldnames=j)
#         writer.writerow(data)
#         writer.w
dict_total = defaultdict(lambda: 0)

func = [("log(log(n, 2))", log(log(n, 2))),
            ("sqrt(log(n, 4))", sqrt(log(n, 4))),
            ("log(n, 3)", log(n, 3)),
            ("log(n, 2) ** 2", log(n, 2) ** 2),
            ("sqrt(n)", sqrt(n)),
            ("n / log(n, 5)", n / log(n, 5)),
            ("log(factorial(n), 2)", log(factorial(n), 2)),
            ("3 ** log(n, 2)", 3 ** log(n, 2)),
            ("n ** 2", n ** 2),
            ("7 ** (log(n, 2))", 7 ** (log(n, 2))),
            ("log(n, 2) ** log(n, 2)", log(n, 2) ** log(n, 2)),
            ("n ** log(n, 2)", n ** log(n, 2)),
            ("n ** sqrt(n)", n ** sqrt(n)),
            ("2 ** n", 2 ** n),
            ("4 ** n", 4 ** n),
            ("2 ** (3 * n)", 2 ** (3 * n)),
            ("factorial(n)", factorial(n))
            ]

num = 0
for f in func[num:]:
    for i in func:
        if i[0] != f[0]:
            a = lapitale(f[1], i[1])
            dict_total[f[0]] += a
            print(f'{f[0]} | {i[0]} - {a}')
        else:
            continue
    num += 1

print(dict_total)
