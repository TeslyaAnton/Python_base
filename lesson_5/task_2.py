with open('text_20.txt', 'r', encoding='utf-8') as f_obj:
    answer = [f'{line}. {count.strip()} - {len(count.split())} слово'
              for line, count in enumerate(f_obj, 1)]
    print(answer, f'Всего строк - {len(answer)}.')