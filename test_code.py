my_dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'}
ls = [int(i) for i in input()]
ls_new = [my_dict[i] for i in ls]
print(*ls_new)