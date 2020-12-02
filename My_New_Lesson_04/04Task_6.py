from itertools import count
print('Часть 1 задачи')
for a in count(3):
    if a > 10:
        break
    else:
        print(a)
print('Часть 2 задачи')
from itertools import cycle

my_list = (1, 2, 5, 7, 15, 19)
step = cycle(my_list)
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))
print(next(step))