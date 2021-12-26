time = int(input('Enter time in second '))
hour = time // 3600
minute = time // 60 - hour * 60
second = time % 60
print(f'{hour:02}:{minute:02}:{second:02}')