#
a, b = int(input()), int(input())
print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) ** 0.5, sep='\n')

#
mass, rost = float(input()), float(input())
imt = mass / (rost * rost)
if imt < 18.5: print('Недостаточная масса')
elif 18.5 <= imt <= 25: print('Оптимальная масса')
elif imt > 25: print('Избыточная масса')

#
s = len(input()) * 60
print(f'{s // 100} р. {s % 100} коп.')

#
animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса",
           "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
print(animals[int(input()) % 12])

#Задача Иосифа Флавия 🌶️🌶️
n, k = int(input()), int(input())
s = [i for i in range(1, n + 1)]
while len(s) > 1:
    for q in range(0, k - 1):
        s.append(s[q])
    del s[:k]
print(*s)

#Координатные четверти
def definition_quarter(x, y):
    quarter = 0
    if x == 0 or y == 0: quarter = 0
    if x < 0 and y > 0: quarter = 2
    elif x > 0 and y > 0: quarter = 1
    elif x < 0 and y < 0: quarter = 3
    elif x > 0 and y < 0: quarter = 4
    return quarter

n = int(input())
ls = [input().rsplit() for i in range(n)]
qu1, qu2, qu3, qu4 = 0, 0, 0, 0
for i in ls:
    x, y = int(i[0]), int(i[1])
    temp = definition_quarter(x, y)
    if temp == 0: continue
    elif temp == 1: qu1 += 1
    elif temp == 2: qu2 += 1
    elif temp == 3: qu3 += 1
    elif temp == 4: qu4 += 1
print(f'Первая четверть: {qu1}' + '\n' +
      f'Вторая четверть: {qu2}' + '\n' +
      f'Третья четверть: {qu3}' + '\n' +
      f'Четвертая четверть: {qu4}')