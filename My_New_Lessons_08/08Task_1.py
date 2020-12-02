class Date:
    def __init__(self, day_mon_year):
        # self.day = day
        # self.mon = mon
        # self.year = year
        self.day_mon_year = str(day_mon_year)

    @classmethod
    def extract(cls, day_mon_year):
        my_date = []

        for i in day_mon_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, mon, year):

        if day == 1 or day <= 31:
            if mon == 1 or mon <= 12:
                if year == 0 or year <= 2020:
                    return f'Correct date'
                else:
                    return f'Uncorrect year'
            else:
                return f'Uncorrect month'
        else:
            return f'Uncorrect day'

    def __str__(self):
        return f'Your date {Date.extract(self.day_mon_year)}'


today = Date('11 - 1 - 2012')
print(today)
print(Date.valid(11, 11, 2022))
print(Date.valid(33, 11, 2018))
print(Date.valid(11, 14, 2018))
print(Date.extract('03 - 08 - 1998'))
print(today.extract('06 - 30 - 1996'))