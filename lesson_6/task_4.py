from random import choice


class Car:
    derection = ['Go north', 'Go east', 'Go west', 'Go south']

    def __init__(self, name, color, speed, p=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = p
        print(f'Car: {name} has a color: {color}.\nThis police car? {p}')

    def go(self):
        print(f'{self.name}: Car went')

    def stop(self):
        print(f'{self.name}: Car stop')

    def turn(self):
        print(f'{self.name}: Car turned {choice(self.derection)}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}.'


class TownCar(Car):

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding' if self.speed > 60 else super().show_speed()


class WorkCar(Car):

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speeding' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    pass


class PoliceCar(Car):

    def __init__(self, name, color, speed):
        super().__init__(name, color, speed, p=True)


police_car = PoliceCar('"УАЗ"', 'СпецЦвет', 140)
work_car = WorkCar('ВИС- "Пирожок"', 'белый', 40)
sport_car = SportCar('F1', 'Красный', 290)
town_car = TownCar('Матиз', 'Зеленый', 65)

list_car = [police_car, work_car, sport_car, town_car]

for i in list_car:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
