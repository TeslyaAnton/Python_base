from random import randint
with open('text_9.txt', 'w', encoding='utf-8') as my_file:
    my_list = [randint(1, 100) for _ in range(100)]
    my_file.write(''.join(map(str, my_list)))
print(f'Sum number - {sum(my_list)}')