from random import randint
number_list = [randint(-5, 5) for _ in range(10)]
answer_list = [el for el in number_list if number_list.count(el) == 1]
print(f'numbers list\n{number_list}\nanswer\n{answer_list}')