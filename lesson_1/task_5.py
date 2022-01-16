revenue = float(input('Введите выручку '))
costs = float(input('Введите расходы '))
result = revenue - costs
if result > 0:
    print(f'Прибыль есть {result}')
    print(f'Рентабильносьб составит {100 * result / revenue:.1f}%')
    personal = int(input('Введите колличество сотрудников '))
    print(f'Зп составит {result / personal:.3f} на человека')
elif result < 0:
    print(f'Тревога несем убытки {-result}')
else:
    print('работаем за идею надо что то улучшать!!')