class DivisionByNull:
    def __init__(self, divisible, denominator):
        self.divider = divisible
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divisible, denominator):
        try:
            return (divisible / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))