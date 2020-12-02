def my_fin():
    a = int(input("введите ставку за час:  "))
    b = int(input("введите часы:  "))
    pr = int(input("введите размер премии:  "))
    d = (a * b) + pr
    return d
all_fin = my_fin()
print(all_fin)