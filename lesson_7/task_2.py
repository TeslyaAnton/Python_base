class Textil:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_square_c(self):
        return self.size / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Расход ткани \n'
                   f' {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_c = round(self.size / 6.5 + 0.5)

    def __str__(self):
        return f'на пальто {self.square_c}'


class Suit(Textil):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'на костюм {self.square_j}'

coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.get_sq_full)
print(suit.get_sq_full)
print(suit.get_square_c())
print(suit.get_square_j())