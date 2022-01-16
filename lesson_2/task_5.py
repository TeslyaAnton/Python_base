my_list = [9, 8, 7, 6, 5, 4, 3, 3, 2, 1]
user_num = int(input('Enter number 1-9 '))
i = 0
for n in my_list:
    if user_num <= n:
        i +=1
    else:
        break
my_list.insert(i, user_num)
print(my_list)