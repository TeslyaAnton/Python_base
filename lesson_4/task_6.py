from itertools import count, cycle
my_count = count(7)
my_cycle = cycle('ABC')
for _ in range(3):
    print('(count, cycle) = ({},{})'.format(next(my_count), next(my_cycle)))