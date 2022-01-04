def division(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'Ошибка! Делить на ноль нельзя')
print(division(int(input('Первое число: ')), int(input('Второе число: '))))