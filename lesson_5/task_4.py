russ_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_88.txt', 'w', encoding='utf-8') as new_file:
    with open('text_8.txt', encoding='utf-8') as my_file:
        new_file.writelines([line.replace(line.split()[0], russ_dict.get(line.split()[0])) for line in my_file])