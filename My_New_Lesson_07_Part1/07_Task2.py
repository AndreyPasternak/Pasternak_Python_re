class Textil:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_pp(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'S ткани:  \n' f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Costum(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return (f'S для костюма:   {self.square_c}')


class Palto(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_pp = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'S для пальто:   {self.square_pp}'

costum_in = Costum(2, 4)
palto_in = Palto(1, 2)
print(costum_in)
print(palto_in)

print(costum_in.get_sq_full)
print(palto_in.get_sq_full)

