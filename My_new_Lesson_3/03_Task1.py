def func(arg_1, arg_2):
    if arg_2 == 0:
        return('на ноль делить нельзя')
    s_div = arg_1 / arg_2
    return s_div
num_1 = float(input('Ввведите первое число:   '))
num_2 = float(input('Ввведите второе число:   '))
final = func(num_1, num_2)
print('Результат:  ', final)