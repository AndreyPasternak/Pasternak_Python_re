
txt_obj = open("My_Lines_02.txt", "r", encoding="UTF-8")
lines = txt_obj.readline()
for x in lines:
    x = lines.split()
    lines_num = len(x)
print('количество слов', lines_num)
print(lines)
lines = txt_obj.readline()
for x in lines:
    x = lines.split()
    lines_num = len(x)
print('количество слов', lines_num)
print(lines)
lines = txt_obj.readline()
for x in lines:
    x = lines.split()
    lines_num = len(x)
print('количество слов', lines_num)
print(lines)
txt_obj.close()
total_lines = sum(1 for l in open('My_Lines_02.txt', 'r'))
print('количество строк в документе:  ', total_lines)
#выводит количество строк: 4 А должно быть 3. Подозреваю, что он считает еще пустую строку
#но как от нее избавиться уже не соображу





