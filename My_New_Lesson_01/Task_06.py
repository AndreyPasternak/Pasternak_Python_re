d = int(input("Введите результат первого дня в км"))
s = int(input("Введите общий пробег"))
day = 1
while d <= s:
    d = d + d*1.1
    day = day + 1
    if d >= s:
        print(day)

