# Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^52 <= m <= 10^5,
# необходимо найти остаток от деления n-го числа Фибоначчи на m.
# Sample Input:
# 10 2
#
# Sample Output:
# 1


def fibonacci(n, m):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, (a + b) % m
        yield a, b


def main():
    n, m = map(int, input().split())
    mode_list = [0, 1]
    for i, j in fibonacci(n, m):
        if i == 0 and j == 1:
            mode_list.pop()
            break
        else:
            mode_list.append(j)
    print(mode_list[n % len(mode_list)])


if __name__ == "__main__":
    main()
