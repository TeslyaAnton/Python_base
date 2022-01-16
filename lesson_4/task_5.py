from functools import reduce

def my_list(el_1, el_2):
    return el_1 * el_2
answer_list = [el for el in range(100, 1001, 2)]
print(f'List\n{answer_list}\nanswer\n{reduce(my_list, answer_list)}')

