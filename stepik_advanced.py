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

#Кремниевая долина 🤖🌶️🌶️
ls = [input() for i in range(int(input()))]
s_main = 'anton'
s_temp = ''
for s in ls:
    s_temp = s
    for i in s_main:
        if i in s_temp:
           s_temp = s_temp[s_temp.find(i):]
        else:
            break
    else:
        print(ls.index(s) + 1, end=' ')

#Роскомнадзор запретил букву stepik
word = input() + ' запретил букву'
a = [chr(i) for i in range(1072,1184) if chr(i) != 'ё']
for x in a:
    if x in word:
        print(word, x)
        word = word.replace(x, '').replace('  ', ' ').strip()

# Камень, ножницы, бумага
def word_chek(new_word):
    result = 0
    if new_word == 'камень': result = 1
    elif new_word == 'ножницы': result = 2
    elif new_word == 'бумага': result = 3
    elif new_word == 'ящерица': result = 4
    elif new_word == 'Спок': result = 5
    return result

def game_chek(timur, ruslan):
    s_result = ''
    if timur == 1 and ruslan == 2: s_result = 'Тимур'
    elif timur == 2 and ruslan == 3: s_result = 'Тимур'
    elif timur == 3 and ruslan == 1: s_result = 'Тимур'
    elif timur == 1 and ruslan == 4: s_result = 'Тимур'
    elif timur == 2 and ruslan == 4: s_result = 'Тимур'
    elif timur == 3 and ruslan == 5: s_result = 'Тимур'
    elif timur == 4 and ruslan == 5: s_result = 'Тимур'
    elif timur == 4 and ruslan == 3: s_result = 'Тимур'
    elif timur == 5 and ruslan == 1: s_result = 'Тимур'
    elif timur == 5 and ruslan == 2: s_result = 'Тимур'

    if timur == 1 and ruslan == 3: s_result = 'Руслан'
    elif timur == 2 and ruslan == 1: s_result = 'Руслан'
    elif timur == 3 and ruslan == 2: s_result = 'Руслан'
    elif timur == 1 and ruslan == 5: s_result = 'Руслан'
    elif timur == 2 and ruslan == 5: s_result = 'Руслан'
    elif timur == 3 and ruslan == 4: s_result = 'Руслан'
    elif timur == 4 and ruslan == 1: s_result = 'Руслан'
    elif timur == 4 and ruslan == 2: s_result = 'Руслан'
    elif timur == 5 and ruslan == 3: s_result = 'Руслан'
    elif timur == 5 and ruslan == 4: s_result = 'Руслан'

    if timur == ruslan: s_result = 'Ничья'
    return print(s_result)

game_chek(word_chek(input()),word_chek(input()))

#Проверка четности
def digit(num1, num2):
    if num1 % num2 == 0: return 'делится'
    else: return 'не делится'
print(digit(int(input()),int(input())))

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in list1:
    total += sum(i)
    counter += len(i)
print(total / counter)

#Список по образцу
n = int(input())
ls = []
for i in range(n):
    ls2 = []
    for k in range(n):
        ls2.append(k + 1)
    ls.append(ls2)
print(*ls, sep = '\n')

#Упаковка дубликатов 🌶️
ls_original = input().split()
ls_new = [[ls_original[0]]]
for i in range(1, len(ls_original)):
    if ls_original[i] == ls_original[i - 1]:
        # list[-1] - (-1) индекс, добавление в последний вложенный спиоск
        ls_new[-1].append(ls_original[i])
    else:
        ls_new.append([ls_original[i]])
print(ls_new)

#Подсписки списка
ls_original = input().split()
ls = [[]]
for i in range(len(ls_original)):
    for j in range(len(ls_original) - i):
        ls.append(ls_original[j:j + i + 1])
print(ls)

#Вывести матрицу 1
n, m = int(input()), int(input())
# Создаем сразу матрицу по заданным N и M
ls = [[input() for _ in range(m)] for _ in range(n)]
#Выводим матрица через циклы
for i in range(n):
    for j in range(m):
        print(ls[i][j], end=' ')
    print()
#Вывод матрицы построчно
# for st in maxtix:
    # print(*st)

#След матрицы ↘️
n = int(input())
ls = [input().split() for _ in range(n)]
summ = 0
for i in range(n):
    summ += int(ls[i][i])
print(summ)

#Больше среднего
n = int(input())
# Формируем матрицу через преобразование каждого элемента введенной строки в список
# после вкладываем полученный список в основной список(в матрицу)
ls = [[int(x) for x in input().split()] for _ in range(n)]
for i in ls:
    mean = 0
    for j in i:
        if j > (sum(i) / n): mean += 1
    print(mean)

# Максимальный в области 1
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
# Формируем матрицу из половины квадрата по диагонали через срез
ls_new = [ls[i][:i + 1] for i in range(n)]
ls_temp = []
for i in ls_new:
    ls_temp.append(max(i))
print(max(ls_temp))

# Максимальный в области 2 🌶️
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
mx = ls[0][0]
for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j or
            i <= j and i >= n - 1 - j) and ls[i][j] > mx:
            mx = ls[i][j]
print(mx)

#Суммы четвертей
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
up, left, right, down = 0, 0, 0, 0
for i in range(n):
    for j in range(n):
        if i < j and i > n - 1 - j: right += ls[i][j]
        if i < j and i < n - 1 - j: up += ls[i][j]
        if i > j and i < n - 1 - j: left += ls[i][j]
        if i > j and i > n - 1 - j: down += ls[i][j]
print(f'Верхняя четверть: {up}', f'Правая четверть: {right}',
      f'Нижняя четверть: {down}', f'Левая четверть: {left}', sep='\n')

# Таблица умножения
n, m = int(input()), int(input())
ls = [[i * j for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        print(str(ls[i][j]).ljust(3), end='')
    print()

# Максимум в таблице 🔝
n, m = int(input()), int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
x, y = 0, 0
el_max = ls[0][0]
for i in range(n):
    for j in range(m):
        if ls[i][j] > el_max:
            el_max = ls[i][j]
            x = i
            y = j
print(x, y)

# Обмен столбцов ⏸️
n, m = int(input()), int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
s = input()
swap_i, swap_j = int(s[0]), int(s[2])
for i in range(n):
    ls[i][swap_j], ls[i][swap_i] = ls[i][swap_i], ls[i][swap_j]
for i in ls:
    print(*i)

#Обмен диагоналей 🔃
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n):
    ls[i][i], ls[n - i - 1][i] = ls[n - i - 1][i], ls[i][i]
for i in ls: print(*i)

# Зеркальное отображение 🦋
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
for i in range(n // 2):
    for j in range(n):
        ls[i][j], ls[n - i - 1][j] = ls[n - i - 1][j], ls[i][j]
for i in ls: print(*i)

#Ходы коня 🐎
x, y = input()
n = 8
ls = [['.'] * n for _ in range(n)]
y = n - int(y)
x = ord(x) - 97
ls[y][x] = 'N'
for i in range(n):
    for j in range(n):
        if abs(i - y) * abs(j - x) == 2:
            ls[i][j] = '*'
for i in ls: print(*i)

# Магический квадрат ✨🌶️
n = int(input())
ls = [[int(x) for x in input().split()] for _ in range(n)]
digits = [i for i in range(1, n ** 2 + 1)]
d1, d2, = 0, 0
for i in range(n):
    j_summ, i_summ = 0, 0
    for j in range(n):
        j_summ += ls[j][i]
        i_summ += ls[i][j]
        if ls[i][j] in digits:
            digits.remove(ls[i][j])
    d1 += ls[i][i]
    d2 += ls[i][n - i - 1]
    if j_summ != i_summ:
        break
if j_summ == i_summ == d1 == d2 and digits == []: print('YES')
else: print('NO')

#Шахматная доска
n, m = input().split()
ls = [[0] * int(m) for _ in range(int(n))]
for i in range(int(n)):
    for j in range(int(m)):
        if (i + j) % 2 == 0: ls[i][j] = '.'
        else: ls[i][j] = '*'
for i in ls:
    print(*i)

#Побочная диагональ
n = int(input())
ls = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == n - i - 1: ls[i][j] = 1
        elif (i > j or i < j or i == j) and i > n - 1 - j: ls[i][j] = 2
for i in ls:
    print(*i)

#Заполнение 1
n, m = [int(i) for i in input().split()]
ls = [[0] * m for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        count += 1
        ls[i][j] = count
for i in range(n):
    for j in range(m):
        print(str(ls[i][j]).ljust(3), end=' ')
    print()

#Заполнение 2
n, m = [int(i) for i in input().split()]
ls = [[0] * m for _ in range(n)]
count = 0
for i in range(m):
    for j in range(n):
        count += 1
        ls[j][i] = count
for i in range(n):
    for j in range(m):
        print(str(ls[i][j]).ljust(3), end=' ')
    print()

#Заполнение спиралью 🌀🌶️🌶️
n, m = [int(i) for i in input().split()]
ls = [[0] * m for _ in range(n)]
x, y = 0, 0
dx, dy = 0, 1
ls[0][0] = 1
count = 2
while count <= n * m:
    if 0 <= x + dx <= n - 1 and 0 <= y + dy <= m - 1 and ls[x + dx][y + dy] == 0:
        ls[x + dx][y + dy] = count
        count += 1
        x += dx
        y += dy
    else:
        if dy == 1:
            dy = 0
            dx = 1
        elif dx == 1:
            dx = 0
            dy = -1
        elif dy == -1:
            dy = 0
            dx = -1
        elif dx == -1:
            dx = 0
            dy = 1

for i in range(n):
    for j in range(m):
        print(str(ls[i][j]).ljust(3), end=' ')
    print()

# Сложение матриц
n, m = [int(i) for i in input().split()]
ls1 = [[int(x) for x in input().split()] for _ in range(n)]
input()
ls2 = [[int(x) for x in input().split()] for _ in range(n)]
ls_new = [[ls1[i][j] + ls2[i][j] for j in range(m)] for i in range(n)]
for i in ls_new:
    print(*i)

# Умножение матриц 🌶️
s_temp = 0
n, m = [int(i) for i in input().split()]
ls1 = [[int(x) for x in input().split()] for _ in range(n)]
input()
n1, m1 = [int(i) for i in input().split()]
ls2 = [[int(x) for x in input().split()] for _ in range(n1)]
ls_new = [[0] * m1 for _ in range(n)]
for i in range(n):
    for q in range(m1):
        for k in range(m):
            s_temp += ls1[i][k] * ls2[k][q]
        ls_new[i][q] = s_temp
        s_temp = 0
for i in ls_new:
    print(*i)

# Возведение матрицы в степень 🌶️
n = int(input())
ls1 = [[int(x) for x in input().split()] for _ in range(n)]
x = int(input())
ls2 = ls1
for _ in range(x - 1):
    ls3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for q in range(n):
            for k in range(n):
                ls3[i][q] += ls1[i][k] * ls2[k][q]
    ls1 = ls3
for i in ls1:
    print(*i)