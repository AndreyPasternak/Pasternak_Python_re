def my_func(ar1, ar2, ar3):
    res = sum([ar1, ar2, ar3]) - min([ar1, ar2, ar3])
    return res
ar1 = float(input('Ввведите первое число:   '))
ar2 = float(input('Ввведите второе число:   '))
ar3 = float(input('Ввведите второе число:   '))
value = my_func(ar1, ar2, ar3)
print(value)