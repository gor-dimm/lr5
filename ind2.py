# Вариант 2. В списке, состоящем из вещественных элементов, вычислить:
# 1) сумму положительных элементов списка;
# 2) произведение элементов списка, расположенных между максимальным по модулю и минимальным по модулю элементами.
# Упорядочить элементы списка по убыванию.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = []
    s = 0
    p = 1
    n = int(input())
    for i in range(n):
        element = float(input())
        a.append(element)
    a.sort(reverse=True)
    for el in a:
        p *= el
        if el > 0:
            s += el
    print("Сумма положительных элементов списка = ", s)
    print("Произведение элементов списка, расположенных между максимальным и минимальным элементами = ", p)
    print("Отсортированный по убыванию список: ", a)