list = [3, 5.5, 'Python', [7, 3], {4: 'num', 5: 'frost'}, frozenset(), {8, 6},
        True, None, range(8), b'bite', bytearray(b'one'), (1, 2, 3.3),]
for i, this in enumerate(list, 1):
    print(f'{i}  {this} - {type(this)}')