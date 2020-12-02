class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return self.title


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}. Запуск отрисовки'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}. Запуск отрисовки'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}. Запуск отрисовки'


Pen_in = Pen('Ручка')
Pencil_in = Pencil('Карандаш')
Handle_in = Handle('Маркер')
print(Pen_in.draw())
print(Pencil_in.draw())
print(Handle_in.draw())