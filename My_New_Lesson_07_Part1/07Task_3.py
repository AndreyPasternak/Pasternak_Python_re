class Cell:
    def __init__(self, total_c):
        self.total_c = int(total_c)

    def __str__(self):
        return f'Итог:   {self.total_c * "*"}'

    def __truediv__(self, other):
        return Cell(round(self.total_c // other.total_c))

    def __add__(self, other):
        return Cell(self.total_c + other.total_c)


    def __mul__(self, other):
        return Cell(int(self.total_c * other.total_c))


    def make_order(self, cells_in_line):
        line = ''
        for i in range(int(self.total_c / cells_in_line)):
            line += f'{"*" * cells_in_line} \\n'
        line += f'{"*" * (self.total_c % cells_in_line)}'
        return line

cells_1 = Cell(28)
cells_2 = Cell(14)
print(cells_1)
print(cells_1 + cells_2)
print(cells_2.make_order(7))
print(cells_1.make_order(11))
print(cells_1 / cells_2)