# my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}


my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open('One_Four.txt', 'r', encoding='UTF-8') as f_obj1, open('Rus_One_Four.txt', 'a', encoding='UTF-8') as f_obj2:
    for line in f_obj1:
        new_dict1 = line.split(' – ')
        new_dict1[0] = my_dict.get(new_dict1[0])
        print(f'{new_dict1[0]} — {new_dict1[1]}')
        f_obj2.write(f'{new_dict1[0]} — {new_dict1[1]}')



    # new_obj1 = f_obj1.read()
    # print(new_obj1












