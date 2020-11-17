a1 = [1, 1, 3, 5, 5, 5, 4]
print(a1)
a2 = [a for a in a1 if a1.count(a) == 1]
print(a2)