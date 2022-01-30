start_km = float(input('Enter start distance '))
finish_km = float(input('Enter finish distance '))
days = 1
while start_km < finish_km:
    start_km += start_km * 0.1
    days += 1
print(f'the goal is completed on {days} days')