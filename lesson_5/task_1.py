with open('text_21.txt', 'w', encoding='utf-8') as f:
    while True:
        line = input('Enter some one: ')
        if not line:
            break
        print(line, file=f)