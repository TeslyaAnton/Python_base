user_need = int(input('Enter month number you want to know? №1-12 '))
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
              8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
month_list = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
if user_need in month_dict:
    print(f'The {user_need}th month of the year is {month_dict[user_need]}')
    print(f'The {user_need}th month of the year is {month_list[user_need - 1]}')
else:
    print('Error')







