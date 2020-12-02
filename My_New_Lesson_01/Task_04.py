Num = int(input('Введите число: '))
#тут мой мозг сломался - спасибо за помощь!
max = 0
while Num > 0:
    a = Num % 10
    Num = Num // 10
    if a > max: max = a
print (max)



