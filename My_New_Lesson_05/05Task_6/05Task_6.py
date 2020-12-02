
with open('Ditch.txt', 'a+', encoding='utf-8') as line_s:
    line_s.seek(0)
    for line in line_s:
        print(sum([int(x) for x in "".join([x for x in line if x in ' 1234567890 ']).split(" ") if x.isdigit()]))