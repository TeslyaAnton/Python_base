def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result

print(f'Возведение в степень: {my_func_2(int(input("введите целое число Х: ")), int(input("введите отрицательное число Y: ")))}')