user_str = input("enter a phrase don't forget the space bar ").split()
for i, word in enumerate(user_str, 1):
    print(f'{i}. {word[:10]}')