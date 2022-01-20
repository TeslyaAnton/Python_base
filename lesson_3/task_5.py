def get_sum(*args):
    sum = 0
    q = False
    for num in args:
        try:
            if num:
                sum += float(num)
        except ValueError:
            q = True
    return sum, q

general_sum = 0

while True:
    args_n = input('Введите числа через пробел: ').split(' ')
    sum, mega_q = get_sum(*args_n)
    general_sum += sum
    print(f'сумма {general_sum}')

    if mega_q:
        break