c = 0
summa = True
while summa:
    cicle = input('Введите числа для сложения или S для выхода:   ')
    for number in cicle.split():
        if number == 'S':
            summa = False
            break
        c += float(number)
        print(c)