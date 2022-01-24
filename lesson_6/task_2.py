class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, weight=25, thickness=5):
        return f'{self._length} * {self._width} * {weight} * {thickness} = ' \
               f'{(self._length * self._width * weight * thickness) / 1000}'

road = Road(5000, 20)
print(road.asphalt_mass())