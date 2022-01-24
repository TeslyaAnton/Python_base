with open('staff.txt', 'r', encoding='utf-8') as f:
    staff_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Average salary = {round(sum(staff_dict.values()) / len(staff_dict), 3)}\n'
          f'Staff with salary less than 20k {[n[0] for n in staff_dict.items() if n[1] < 20000]}')