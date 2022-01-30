my_dict = {}
with open('subjects.txt', encoding='utf-8') as my_file:
    for line in my_file:
        name, stats = line.split(':')
        name_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        my_dict[name] = name_sum
print(f'{my_dict}')