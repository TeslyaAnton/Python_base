num = int(input('Enter number '))
max_num = 0
while num > 0:
    number = num % 10
    if number > max_num:
        max_num = number
    num = num // 10
print(f'Max number = {max_num}')