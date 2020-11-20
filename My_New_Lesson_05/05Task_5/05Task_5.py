with open('My_Summ.txt', 'r', encoding='UTF-8') as sam_b:
    print_b = sam_b.read()
    print(print_b)
    print_u = print_b.split()
    print(sum(int(perem) for perem in print_u))


    # c = 0
    # # for number in print_b.split():
    # #     c += float(number)
    # #     print(c)


