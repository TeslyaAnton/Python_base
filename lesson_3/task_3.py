def my_func(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')
my_func(int(input('Аргумент 1: ')), int(input('Аргумент 2: ')), int(input('Аргумент 3: ')))