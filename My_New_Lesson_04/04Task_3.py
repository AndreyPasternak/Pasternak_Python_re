#первый вариант решения
a = [x for x in range(0 , 240, 21)]
print(a)
b = [x for x in range(20, 240 + 1, 20)]
print(b)

# второй вариант решения
print('второй вариант решения')

a = [x for x in range(20, 240 + 1) if x % 20 == 0 or x % 21 == 0 ]
print(a)