def factorial_num(number):
    f_num = 1
    for i in range(number + 1):
        yield f'{i}! = {f_num}'
        f_num *= i + 1
for x in factorial_num(int(input('Enter Factorial you need know: '))):
    print(x)