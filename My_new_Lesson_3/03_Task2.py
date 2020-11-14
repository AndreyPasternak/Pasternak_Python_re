def str_func(name, surname, year, city, email, phone):
    return name, surname, year, city, email, phone
params = ("Борис", "Моисеев", 1907, "Кижи", "bm07@list.ru", 2128506)
print(str_func(*params))