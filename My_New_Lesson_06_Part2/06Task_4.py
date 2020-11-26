class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return (self.name, 'Here we go')
    def stop(self):
        return (self.name, 'We are stopped')
    def turn_toleft(self):
        return (self.name, 'To left')
    def turn_toright(self):
        return (self.name, 'To right')

    def show_speed(self):
        return f'Speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):

        if self.speed >= 60:
            return (self.name, "Stop!!!")
        else:
            return (self.name, "Safety drive!")

class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):

        if self.speed >= 40:
            return (self.name, "Stop!!!")
        else:
            return (self.name, "Safety drive!")



class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)



TownCar_in = TownCar('Nissan', 'white', 59, False)
SportCar = Car('Mitsubishi', 'red', 260, False)
WorkCar_in = WorkCar('Man', 'orange', 110, False)
PoliceCar = Car('Lada', 'gray', 130, True)

print(TownCar_in.show_speed())
print(WorkCar_in.show_speed())
print(SportCar.show_speed())
print(PoliceCar.turn_toleft())
print(PoliceCar.turn_toright())


