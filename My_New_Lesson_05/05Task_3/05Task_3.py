my_list = open('My_Units.txt', 'r', encoding='utf-8')
lines = my_list.read()
res = [float(i) for i in lines.split() if i.isdigit()]
print('Среднее арифметическое от дохода:   ', sum(res) / 3)

my_list.close()
with open('My_Units.txt', 'r', encoding='UTF-8') as spisok:
    i = 0
    sum_zp = 0
    for line in spisok:
        name, zp = line.split()
        sum_zp += float(zp)
        i += 1
        if float(zp) < 20000:
            print('С доходом меньше 20 000:   ', name, zp)

