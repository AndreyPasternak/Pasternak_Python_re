from functools import reduce
my_list = ()
a2 = [a for a in range(100, 1000 + 1) if a % 2 == 0]
print(a2)
a3 = reduce(lambda x, y: x * y, a2, 1)
print(a3)

# проверка этого дикого массива

from functools import reduce
my_list = ()
a2 = [a for a in range(8, 24 + 1) if a % 2 == 0]
print(a2)
a3 = reduce(lambda x, y: x * y, a2, 1)
print(a3)