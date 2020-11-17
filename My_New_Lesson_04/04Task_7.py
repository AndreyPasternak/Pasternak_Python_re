from math import factorial

def fact(n):
    res = 1

    for i in range(1, n + 1):
        res = factorial(i)
        yield res


n = int(input('введите число:   '))
for el in fact(n):
    print(el)






