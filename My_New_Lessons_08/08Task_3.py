class Exclusion:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                numbers = int(input('Введите число и нажмите Enter - '))
                self.my_list.append(numbers)
                print(f'{self.my_list}')
                # я вот тут два часа с синтаксисом провозился, это можно только зазубрить
            except:
                print(f'Можно вводить только числа')
                correct = input(f'Попробовать еще раз? Y/N ')
                if correct == 'Y':
                    print(trytry.my_input())
                elif correct == 'N':
                    return f'Конец цикла'

trytry = Exclusion()
print(trytry.my_input())