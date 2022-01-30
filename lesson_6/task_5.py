class Stationery:
    def __init__(self, title='Something can draw'):
        self.title = title

    def draw(self):
        print(f'Start draw {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'draw with {self.title} pen')


class Pencil(Stationery):
    def draw(self):
        print(f'draw with {self.title} pencil')


class Handle(Stationery):
    def draw(self):
        print(f'draw with {self.title} handle')


star = Stationery()
pen = Pen('Parker')
pencil = Pencil('Hard 2')
marker = Handle('Some')

office_chancellery = [star, pen, pencil, marker]

for i in office_chancellery:
    i.draw()