# Даны две строки, состоящие из строчных латинских букв. Требуется определить, являются ли эти строки анаграммами,
# т. е. отличаются ли они только порядком следования символов.
#
# Формат ввода Входной файл содержит две строки строчных латинских символов, каждая не длиннее 100 000 символов.
# Строки разделяются символом перевода строки.
#
# Формат вывода
# Выходной файл должен содержать единицу, если строки являются анаграммами, и ноль в противном случае.
#
# Пример 1
# Ввод	Вывод
# qiu     1
# iuq
#
# Пример 2
# Ввод	Вывод
# zprl    0
# zprc
import ya_alphabet_settings

import sys


# def anagram(word_1, word_2):
#     for letter in word_1:
#         if letter in word_2:
#             word_2.remove(letter)
#             continue
#         else:
#             return 0
#     else:
#         return 1 if len(word_2) == 0 else 0
#
#
# print(anagram(sys.stdin.readline().strip(), list(sys.stdin.readline().strip())))


# s1 = sys.stdin.readline().strip()
# s2 = sys.stdin.readline().strip()
#
# l1 = list(s1)
# l1.sort()
# print(l1.sort())
# l2 = list(s2)
# l2.sort()
# print(l2.sort())
#
# print(1 if l1 == l2 else 0)

class AnagramSolution:

    def __init__(self, list_1, list_2, alphabet='ru'):
        self.sequence_one = list_1
        self.sequence_two = list_2
        self.alphabet = alphabet
        self.count_one = None
        self.count_two = None

    def run(self):
        if self.alphabet == 'ru':
            self.alphabet = ya_alphabet_settings.ru
        else:
            self.alphabet = ya_alphabet_settings.eng
        self.count_one = [0] * len(self.alphabet)
        self.count_two = [0] * len(self.alphabet)

        return self._computation_unicode()

    def _computation_unicode(self):
        for i in range(len(self.sequence_one)):
            position = ord(self.sequence_one[i]) - ord('a')  # возвращает позицию юникод-символа. известно, что у нас
                                                             # en alphabet
            self.count_one[position] = self.count_one[position] + 1

        for i in range(len(self.sequence_two)):
            position = ord(self.sequence_two[i]) - ord('a')  # ord('a')  # 97
            self.count_two[position] = self.count_two[position] + 1

        return self._comparison_positions()

    def _comparison_positions(self):
        start = 0
        flag = 1
        while start < 26 and flag:
            if self.count_one[start] == self.count_two[start]:
                start = start + 1
            else:
                flag = 0
        return flag


if __name__ == '__main__':
    anagram = AnagramSolution(sys.stdin.readline().strip(), sys.stdin.readline().strip())
    print(anagram.run())
