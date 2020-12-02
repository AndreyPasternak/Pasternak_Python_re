class Road:
    _lenth = 20
    _width = 5000
    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width

    def volume(self):
        return self.lenth * self.width * 25 * 5
a = Road(20, 5000)
a.volume()
print(a.volume())