from sympy import *
from sympy.abc import *


def lapitale(my_func1, my_func2):
    return limit(my_func1 / my_func2, z=n, z0='oo')


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
            (" 2 ** (3 * n)", 2 ** (3 * n)),
            ("factorial(n)", factorial(n))
            ]

num = 0
for f in func[num:]:
    for i in func:
        if i[0] != f[0]:
            print(f'{f[0]} | {i[0]} - {lapitale(f[1], i[1])}')
        else:
            continue
    num += 1

