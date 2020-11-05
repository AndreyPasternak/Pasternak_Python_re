plus = float(input("Введите сумму выручки:  "))
minus = float(input("Введите сумму расходов:  "))
a = float(plus)
b = float(minus)
u = a - b
if a > b :
    print('Вы в плюсе:  ' , u)
elif a < b :
    print('Вы в минусе:  ', u)

units = float(input("Сколько у вас сотрудников:  "))
n = float(units)
d = u / n
if a > b:
    print("Прибыль на сотрудника составляет: ", d)