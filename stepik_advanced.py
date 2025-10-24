#
from decimal import *
from fractions import Fraction
import math
import string
from random import *

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

# Вывести матрицу 2
n, m = int(input()), int(input())
# Создаем сразу матрицу по заданным N и M
ls = [[input() for _ in range(m)] for _ in range(n)]
ls_copy = [[ls[i][j] for i in range(n)] for j in range(m)]
#Выводим матрица через циклы
for i in range(n):
    for j in range(m):
        print(ls[i][j], end=' ')
    print()
print()
#Вывод матрицы построчно через цикл
for i in ls_copy:
    print(*i)

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

tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4), (5, 6, 10, 2, 1, 77)]
new_tuples = [(i[:-1]) + (100,) for i in tuples]
print(new_tuples)

#Вершина параболы
tup = tuple([int(input()) for _ in range(3)])
ls_temp = [0.0, 0.0]
ls_temp[0] = -(tup[1] / (2 * tup[0]))
ls_temp[1] = (4 * tup[0] * tup[2] - tup[1] ** 2) / (4 * tup[0])
tup = tuple(ls_temp)
print(tup)

# Конкурсный отбор
n = int(input())
# Ввод вложенных кортежей
tp = tuple(tuple(input().split()) for _ in range(n))
for i in tp: print(*i)
print()
for i in tp:
    if int(i[1]) >= 4: print(*i)

# Последовательность Трибоначчи
n = int(input())
m1, m2, m3 = 1, 1, 1
for i in range(n):
    print(m1, end = ' ')
    m1, m2, m3 = m2, m3, m1 + m2 + m3

# 8.4 Основы работы с множествами
# Три слова
s1, s2, s3 = [set(i) for i in input().split()]
if s1 == s2 == s3: print('YES')
else: print('NO')

# 8.5 Методы множеств. Часть 1
# Уникальные символы 1
ls = [set(input().lower()) for i in range(int(input()))]
for i in ls: print(len(i))

# Счетчик верных решений ✅🌶️🌶️
student = set()
n = int(input())
correct = 0
for _ in range(n):
    resualt = input().split(': ')
    if resualt[1] == 'Correct':
        correct += 1
        student.add(resualt[0])
if correct:
    print(f'Верно решили {len(student)} учащихся')
    print(f'Из всех попыток {round((correct / n) * 100 + 0.001)}% верных')
else: print('Вы можете стать первым, кто решит эту задачу')

# Общие числа
set1, set2 = set(input().split()), set(input().split())
set3 = set1 & set2
# Обрати внимание на ключ сортировки key=int
ls = sorted(set3, key=int)
print(*ls)

# Общие цифры
ls = [set(input()) for i in range(int(input()))]
set1 = ls[0]
for i in range(1, len(ls)):
    set1.intersection_update(ls[i])
print(*sorted(set1))

#Все цифры 🔢
set1 = set(input())
set2 = set(input())
flag = set1.issuperset(set2)

# Вывод в скобках (
# (кортеж, где 0 индекс NO и 1 индекс YES)
# [обращение по индексу из значения flag(или 0(true) или 1(false)])
print(('NO', 'YES')[flag])

#Урок математики 🧠
set1, set2, set3 = [set(input().split()) for _ in range(3)]
print(*sorted((set1 | set2 | set3) - (set1 & set2 & set3), key=int))

#Урок биологии
set1 = set(int(i) for i in input().split())
set2 = set(int(i) for i in input().split())
set3 = set(int(i) for i in input().split())
set_new = set(range(11))
print(*sorted(set_new - set1 - set2 - set3))

#8.8 Генераторы множеств и frozenset
# {выражение for переменная in последовательность}
words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
newset = {i[0].lower() for i in words}
print(*sorted(newset))

# Книги на прочтение 📚
m, n = int(input()), int(input())
flag = 0
home = {input() for _ in range(m)}
ls = [('NO', 'YES')[input() in home] for _ in range(n)]
print(*ls, sep='\n')

n = int(input())
res = {input() for _ in range(int(input()))}
for _ in range(n - 1):
    res &= {input() for _ in range(int(input()))}
print(*sorted(res), sep= '\n')

users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
newlis = []
for el in users:
    if 'email' not in el or el['email'] == '' : newlis.append(el['name'])
print(*sorted(newlis))

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

#Информация об учебных курсах 🎓
course = {'CS101': {'room': 3004, 'prepod': 'Хайнс', 'time': '8:00' },
          'CS102': {'room': 4501, 'prepod': 'Альварадо', 'time': '9:00' },
          'CS103': {'room': 6755, 'prepod': 'Рич', 'time': '10:00' },
          'NT110': {'room': 1244, 'prepod': 'Берк', 'time': '11:00' },
          'CM241': {'room': 1411, 'prepod': 'Ли', 'time': '13:00' }}
number = input()
print(f'{number}: {course[number]['room']}, {course[number]['prepod']}, '
      f'{course[number]['time']}')

# Набор сообщений 📩
symbol_numbers = {'1': '.,?!:',
                  '2': 'ABC',
                  '3': 'DEF',
                  '4': 'GHI',
                  '5': 'JKL',
                  '6': 'MNO',
                  '7': 'PQRS',
                  '8': 'TUV',
                  '9': 'WXYZ',
                  '0': ' '}
s = input().upper()
s_new = ''
for el in s:
    for key, value in symbol_numbers.items():
        if el in value: print(key * (value.index(el) + 1), end= '')

# Код Морзе
letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.',
         '--.', '....', '..', '.---', '-.-', '.-..',
         '--', '-.', '---', '.--.', '--.-', '.-.', '...',
         '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
         '-----', '.----', '..---', '...--', '....-', '.....',
         '-....', '--...', '---..', '----.']
s = input().upper()
mydict = dict(zip(letters, morse))
for key in s:
    if key in mydict: print(mydict[key], end= ' ')

#Квадраты ключей
result = {}
for i in range(1, 16): result.setdefault(i, i ** 2)
print(result)

#Результирующий словарь
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result = dict1.copy()
for key, value in dict2.items():
    result[key] = result.get(key, 0) + value

#Подсчет вхождений
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for i in text:
    result[i] = result.setdefault(i, 0) + 1
print(result)

#Наиболее встречающеся слово
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
ls = s.split()
mydict = {}
v_max = 0
key_max = 0
for el in ls:
    mydict[el] = mydict.setdefault(el, 0) + 1
    if mydict[el] > v_max:
        v_max = mydict[el]
        key_max = el
print(key_max)

#Список pets
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}
for el in pets:
    result.setdefault(el[1:], []).append(el[0])
print(result)

# Самое редкое слово 🌶️
ls = [i.lower().strip(".,!?:;-") for i in input().split()]
mydict = {}
for i in ls:
    mydict[i] = ls.count(i)
result = {}
min_count = min(mydict.values())
for key, value in mydict.items():
    if value == min_count:
        result[key] = value
print(min(result))

# Исправление дубликатов 🌶️
ls = input().lower().split()
mydict = {}
ls_new = []
for el in ls:
    if el not in ls_new: ls_new.append(el)
    else:
        mydict[el] = mydict.get(el, 0) + 1
        ls_new.append(el + '_' + str(mydict[el]))
print(*ls_new)

# Словарь программиста 📘
it_dict = {}
for _ in range(int(input())):
    k, v = input().split(': ')
    it_dict[k.lower()] = v
for _ in range(int(input())):
    s = input().lower()
    print(it_dict.get(s, 'Не найдено'))

#Анаграммы 1
s1 = sorted(input())
s2 = sorted(input())
dict1, dict2 = dict(zip(range(len(s1)), s1)), dict(zip(range(len(s2)), s2))
print('YES') if dict2 == dict1 else print('NO')

# Анаграммы 2
s1 = sorted([i for i in input().lower() if i.isalpha()])
s2 = sorted([i for i in input().lower() if i.isalpha()])
dict1, dict2 = dict(zip(range(len(s1)), s1)), dict(zip(range(len(s2)), s2))
print('YES') if dict2 == dict1 else print('NO')
# Тоже самое через фукнцию
def s(word):
    res = {}
    for i in word.lower():
        if i.isalpha():
            res[i] = res.get(i, 0) + 1
    return res
print(("NO", "YES")[s(input()) == s(input())])


# Словарь синонимов
dict_sinonim = {}
for _ in range(int(input())):
    k, v = input().split()
    dict_sinonim[k] = v
sinonim = input()
for k, v in dict_sinonim.items():
    if sinonim == k: print(v)
    if sinonim == v: print(k)

# Страны и города
country = {}
for _ in range(int(input())):
    c, *cities = input().split()
    country[c] = cities
for _ in range(int(input())):
    k = input()
    for key, value in country.items():
        if k in value: print(key)

# Телефонная книга 📒
dict_book = {}
for _ in range(int(input())):
    number, name = input().lower().split()
    dict_book.setdefault(name, []).append(number)
for _ in  range(int(input())):
    s = input().lower()
    #Можно вывести так
    print(*dict_book[s]) if s in dict_book else print('абонент не найден')
    # А можно вот так, без ввода строки S выше
    # print(*dict_book.get(input.lower(), ['абонент не найден']))

# Секретное слово
s = input()
my_dict = {}
for _ in range(int(input())):
    value, key = input().split(': ')
    my_dict[int(key)] = value
for i in s: print(my_dict[s.count(i)], end='')

#Генератор словарей
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95,
           1, 36, -38, -19, 1, 6, 87]
result = {i: numbers[i] ** 2 for i in range(len(numbers))}
print(result)

#Генератор словарей 5
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(el.split(':')[0]): el.split(':')[1] for el in s.split()}
print(result)

#Генератор словарей 6
numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21,
           35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
result = {i: sorted([k for k in range(1, i + 1) if i % k == 0])for i in numbers}
print(result)

#Генератор словарей 7
words = ['hello', 'bye', 'yes', 'no', 'python',
         'apple', 'maybe', 'stepik', 'beegeek']
result = {i: [ord(symb) for symb in i]for i in words}
print(result)

#Генератор словарей 8
letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D',
           4: 'E', 5: 'F', 6: 'G', 7: 'H',
           8: 'I', 9: 'J', 10: 'K', 11: 'L',
           12: 'M', 13: 'N', 14: 'O', 15: 'P',
           16: 'Q', 17: 'R', 18: 'S', 19: 'T',
           20: 'U', 21: 'V', 22: 'W', 23: 'X',
           24: 'Y', 26: 'Z'}
remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
result = {key: value for key, value in letters.items() if key not in remove_keys}

#Генератор словарей 9
students = {'Timur': (170, 75), 'Ruslan': (180, 105),
            'Soltan': (192, 68), 'Roman': (175, 70),
            'Madlen': (160, 50), 'Stefani': (165, 70),
            'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67),
            'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
            'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80),
            'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80),
            'Mary': (175, 69), 'Jane': (190, 80)}
result = {k: v for k, v in students.items() if v[0] > 167 and v[1] < 75}

#Генератор словарей 10
tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12),
          (13, 14, 15), (16, 17, 18), (19, 20, 21),
          (22, 23, 24), (25, 26, 27), (28, 29, 30),
          (31, 32, 33), (34, 35, 36)]
result = {i[0]: i[1:] for i in tuples}
print(result)

#Генератор словарей 11
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
result = [{i: {k: q}}for i, k, q in zip(student_ids, student_names, student_grades)]
print(result)

#Итоговая работа на словари 1
my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
my_dict = {i: [i for i in my_dict[k] if i <= 20]for k in my_dict}

#Итоговая работа на словари 2
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
result = sorted([i + '@' + key for key, value in emails.items() for i in value])
print(*result, sep= '\n')

#Итоговая работа на словари Минутка генетики 🧬
dnk_to_rnk = {"G":"C", "C":"G","T":"A","A":"U"}
result = [dnk_to_rnk[i] for i in input()]
print(*result, sep= '')

#Итоговая работа на словари Порядковый номер
s = input().split()
reult = {}
for el in s:
    reult[el] = reult.get(el, 0) + 1
    print(reult[el], end=' ')

#Итоговая работа на словари Scrabble game
const = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
s = input().upper()
count = 0
for key, value in const.items():
    for i in s:
        if i in value: count+= key
print(count)

#Итоговая работа на словари Строка запроса 🔎
def build_query_string(params):
    return '&'.join([f"{key}={value}" for key, value in sorted(params.items())])

# Итоговая работа на словари Слияние словарей 🌶️
def merge(values):      # values - это список словарей
    result = {}
    for d in values:
        for key in d:
            result.setdefault(key, set()).add((d[key]))
    return result

# Итоговая работа на словари Опасный вирус 😈
result = {}
dict_oper = {'W': 'write', 'R': 'read', 'X': 'execute'}
for _ in range(int(input())):
    x = input().split()
    result[x[0]] = [dict_oper[i] for i in x[1:]]
for _ in range(int(input())):
    x = input().split()
    if x[0] in result[x[1]]: print('OK')
    else: print('Access denied')

# Итоговая работа на словари Покупки в интернет-магазине 🛒🌶️
result = {}
for _ in range(int(input())):
    key1, key2, value = input().split()
    result.setdefault(key1, {})
    result[key1][key2] = result[key1].get(key2, 0) + int(value)
for key, value in sorted(result.items()):
    print(f'{key}:')
    for i in sorted(value): print(i, value[i])

# 12.1 Модуль random. Часть 1
# import random
n = int(input())    # количество попыток
for _ in range(n):
    print(random.choice(['Орел', 'Решка']))

# генерация пароля
# import random
length = int(input())    # длина пароля
s = ''
for _ in range(length):
    if random.randint(0, 1) == 1: s += chr(random.randint(65, 90))
    else: s += chr(random.randint(97, 122))
print(s)

# Лотерейный билет
# import random
print(*sorted([random.randint(1, 49) for _ in range(7)]))

# Приведенный ниже код:
#
# import string
#
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
# выводит:
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# 0123456789
# 0123456789abcdefABCDEF
# 01234567
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c

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

# Напишите функцию generate_ip()
# import random
def generate_ip():
    return f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'
generate_ip()

# Почтовый индекс в Латверии
# import random, string
# from random import randint, choice
def generate_index():
    s = string.ascii_uppercase
    return f'{choice(s)}{choice(s)}{randint(0, 99)}_{randint(0, 99)}{choice(s)}{choice(s)}'
generate_index()

#Лотерейный билет
# import random
my_set = set()
while len(my_set) != 100:
    my_set.add(random.randint(1000000, 9999999))
    print(*my_set, sep = '\n')

# Игра в бинго
# import random
numbers = random.sample(list(range(1, 76)), 25)
matrix = [numbers[i:i + 5] for i in range(0, 21, 5)]
matrix[2][2] = 0
for i in range(5):
    for j in range(5):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

#Тайный друг 🕵🏻🌶️
# import random
my_friend =[input() for _ in range(int(input()))]
random.shuffle(my_friend)
for i in range(len(my_friend)):
    print(f'{my_friend[i - 1]} - {my_friend[i]}')

# Генератор паролей 1
# import random
# import string
def generate_password(length):
    smbl = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
    smbl = ''.join([symbol for symbol in smbl if symbol not in 'IloO'])
    return ''.join(random.sample(smbl, length))
def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')

# Генератор паролей 2
# import random
# import string
def generate_password(length):
    upper_case = [i for i in string.ascii_uppercase if i not in 'IO']
    lower_case = [i for i in string.ascii_lowercase if i not in 'lo']
    digits = list(string.digits[2:])
    chars = upper_case + lower_case + digits
    result = [random.choice(i) for i in (upper_case, lower_case, digits)]
    result += [random.choice(chars) for i in range(length - 3)]
    return ''.join(result)
def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]

n, m = int(input()), int(input())
print(*generate_passwords(n, m), sep='\n')

# 12.3 Метод Монте-Карло и Bogosort
# import random

n = 10**6       # количество испытаний
k = 0
s0 = 16
for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)
    if x**3 + y**4 + 2 >= 0 and 3 * x + y ** 2 <= 2: k += 1
print((k / n) * s0)

# 12.3 Метод Монте-Карло и Bogosort
# import random
n = 10 ** 5
k = 0
s0 = 4

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1: k += 1
print((k / n) * s0)

# 13.1 Модуль decimal
# from decimal import *
num = Decimal(input())
tup = num.as_tuple().digits
print(max(tup) + min(tup) * (abs(num) >= 1))

#Математическое выражение
# from decimal import *
d = Decimal(input())
print(d.exp() + d.ln() + d.log10() + d.sqrt())

# 13.2 Модуль fractions

# 13.1 Вывод дробных чисел
numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76',
           '0.71', '1.97', '2.54', '3.67', '0.14', '4.29', '1.84', '4.07',
           '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29',
           '5.12', '4.02', '6.95', '1.62', '2.26', '0.45', '6.91', '7.39',
           '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63',
           '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
for el in numbers: print(f'{el} = {Fraction(el)}')

# 13.2 Сумма
s = ('0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 '
     '0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 5.26 4.83 7.13 1.22 1.02 '
     '7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 '
     '5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021')
ls = [float(i) for i in s.split()]
print(Fraction(str(min(ls) + max(ls))))

# 13.2 Сократите дробь
m, n = int(input()), int(input())
print(Fraction(m, n))

# Операции над дробями
m, n = input(), input()
print(f'{m} + {n} = {Fraction(m) + Fraction(n)}',
      f'{m} - {n} = {Fraction(m) - Fraction(n)}',
      f'{m} * {n} = {Fraction(m) * Fraction(n)}',
      f'{m} / {n} = {Fraction(m) / Fraction(n)}', sep= '\n')

# Сумма дробей 1
n = int(input())
print(sum([Fraction(1, i ** 2) for i in range(1, n + 1)]))

# Сумма дробей 2
n = int(input())
print(sum([Fraction(1, math.factorial(i)) for i in range(1, n + 1)]))

# Юный математик 🤓🌶️
n = int(input())
ls = []
for i in range(1, n - 1):
    for j in range(i + 1, n):
        k = Fraction(i, j)
        if k.numerator + k.denominator == n: ls.append(k)
print(max(ls))

# Упорядоченные дроби
n = int(input())
m_set = set()
for i in range(1, n):
    for j in range(i + 1, n + 1):
        m_set.add(Fraction(i, j))
print(*sorted(m_set), sep = '\n')

#Комплексные числа
z1, z2 = complex(input()), complex(input())
print(f'{z1} + {z2} = {z1 + z2}\n'
      f'{z1} - {z2} = {z1 - z2}\n'
      f'{z1} * {z2} = {z1 * z2}\n')

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
x = 0
for num in numbers:
    if abs(num) > abs(x): x = num
print(x, abs(x), sep='\n')

n = int(input())
z1, z2 = complex(input()), complex(input())
print(z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1))

# 14.1 Модуль черепашки. Часть 1
import turtle
def triangle(side):
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.forward(side)
    turtle.left(120)
    turtle.exitonclick()
triangle(int(input()))

# 14.2 Модуль черепашки. Часть 2
def shalom(num):
    for _ in '123':
        turtle.forward(num)
        turtle.left(120)
    turtle.forward(num / 3)
    turtle.left(120)
    turtle.forward(num / 3 * 2)
    turtle.right(120)
    for _ in '123':
        turtle.forward(num)
        turtle.right(120)
shalom(100)

# Напишите программу, которая рисует изображение мишки в соответствии с образцом.
size = int(input())  # Размер головы (радиус большого круга)
pensize = size * 0.1  # Размер пера
turtle.Screen().setup(600, 1000)
turtle.hideturtle()
turtle.pensize(pensize)
turtle.speed(0)

parts = {1: {"pos": (0, 0), "size": size,  # Голова
             "circle": True, "color": "brown"},
         2: {"pos": (0, 0), "size": size * 0.6,  # Нос
             "circle": True, "color": "orange"},
         3: {"pos": (0, size * 0.3), "size": size * 0.3,  # Ноздри
             "circle": False, "color": "gray"},
         4: {"pos": (0, size * 0.6), "size": size * 0.1,  # Кончик
             "circle": True, "color": "yellow"},  # носа
         5: {"pos": (size * -0.5, size * 1.2), "size": size * 0.1,  # Левый
             "circle": True, "color": "black"},  # глаз
         6: {"pos": (size * 0.5, size * 1.2), "size": size * 0.1,  # Правый
             "circle": True, "color": "black"},  # глаз
         7: {"pos": (size * -0.85, size * 1.8), "size": size * 0.3,  # Левое
             "circle": True, "color": "red"},  # ухо
         8: {"pos": (size * 0.85, size * 1.8), "size": size * 0.3,  # Правое
             "circle": True, "color": "red"}}  # ухо


def bear(pos, size, circle, color):
    turtle.penup()
    turtle.goto(pos)
    turtle.pencolor(color)
    turtle.pendown()
    if circle:
        turtle.setheading(0)
        ycor = pos[1]
        while (size > 0):
            turtle.circle(size)
            size -= pensize - 1
            ycor += pensize - 1
            turtle.goto(pos[0], ycor)
    else:
        turtle.setheading(90)
        turtle.forward(size)


for i in range(1, 9):
    bear(parts[i]["pos"], parts[i]["size"], parts[i]["circle"], parts[i]["color"])


# Напишите программу, которая случайным образом рисует снежинки разного цвета и размера в соответствии с образцом.
# Глобальные переменные ------------------------------------------------------------
SCREEN_SIZE = 400  # Размер квадратного холста
ACCESS_X = set(range(-SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 1))  # Доступные точки
ACCESS_Y = set(range(-SCREEN_SIZE // 2, SCREEN_SIZE // 2 + 1))  # по "x" и "y"

turtle.Screen().setup(SCREEN_SIZE, SCREEN_SIZE)  # Размер холста
turtle.Screen().bgcolor("cyan")  # Цвет холста
turtle.pencolor("blue")  # Цвет пера
turtle.speed(0)  # Скорость анимации черепашки
turtle.hideturtle()  # Видимость черепашки выключена
def star():
    global ACCESS_X, ACCESS_Y

    max_size = 0.4  # Макс. значение интервала для выбора размера снежинки
    while (max_size >= 0.2):
        size = random.uniform(SCREEN_SIZE * 0.02, SCREEN_SIZE * max_size)
        x0 = random.choice(tuple(ACCESS_X))  # Выбор коор. "x" из доступных точек
        y0 = random.choice(tuple(ACCESS_Y))  # Выбор коор. "y" из доступных точек
        xcors = set(range(int(x0 - size / 2), int(x0 + size / 2)))  # Множества занятых
        ycors = set(range(int(y0 - size / 2), int(y0 + size / 2)))  # точек "x" и "y"

        # Если область свободна, приступаем к рисованию
        if (len(xcors - ACCESS_X) == 0 and len(ycors - ACCESS_Y) == 0):
            turtle.penup()
            turtle.goto(x0, y0)  # Центр снежинки с выбранными выше координатами
            turtle.pendown()

            quarter = size / 2 / 4  # Четвертая часть луча снежинки
            for _ in range(8):  # Цикл для рисования восьми лучей
                for _ in range(4):  # Цикл для рисования четырех веточек на данном луче
                    turtle.left(30)
                    turtle.forward(quarter)
                    turtle.backward(quarter)
                    turtle.right(60)
                    turtle.forward(quarter)
                    turtle.backward(quarter)
                    turtle.left(30)
                    turtle.forward(quarter)
                turtle.backward(size / 2)
                turtle.left(45)

            ACCESS_X -= xcors  # Занятые снежинкой точки
            ACCESS_Y -= ycors  # убираем из доступных
            print(len(ACCESS_X), len(ACCESS_Y))  # Кол-во доступных точек
            break
        else:  # Если область занята, то уменьшаем макс. значение
            max_size -= 0.1  # интервала для выбора размера снежинки

while (len(ACCESS_X) > SCREEN_SIZE * 0.2 and
       len(ACCESS_Y) > SCREEN_SIZE * 0.2):
    star()
print("DONE!")

# Напишите программу, которая рисует знак STOP по образцу.
from turtle import *
speed(0)
hideturtle()
side = 110
angle = 180 * (8 - 2) / 8
x, y = 0, 0
colors = ('black', 'white', '#EA0F0F')

for i in range(3):
    penup()
    goto(x, y)
    color(colors[i])
    begin_fill()
    pendown()
    for _ in range(8):
        forward(side)
        left(180 - angle)
    end_fill()
    x += 2
    y += 5
    side -= 4

penup()
color(colors[1])
goto(55, 70)
write('STOP', align='center', font=('Arial Narrow', 75, 'normal'))

done()

"""Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) 
и возвращает приветствие в соответствии с образцом."""
def count_args(*args):
    ls = [i for i in args if type(i) in (int, float)]
    if len(ls) == 0: return 0.0
    else: return sum(ls) / len(ls)
print(count_args(input()))

"""Функиция принимает аргументы и выводит приветствие всех"""
def greet(name, *args):
    s = " and ".join((name,) + args)
    return f'Hello, {s}!'

"""Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов 
и печатает именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, 
при этом имена аргументов следуют в алфавитном порядке (по возрастанию)"""
def print_products(*args):
    ls = [i for i in args if type(i) == str and len(i) > 1]
    if len(ls) == 0: print('Нет продуктов')
    else:
        for i in range(1, len(ls) + 1):
            print(f'{i}) {ls[i - 1]}')

"""Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает именованные
аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>,
при этом имена аргументов следуют в алфавитном порядке (по возрастанию)."""
def info_kwargs(**kwargs):
    for key,value in sorted(kwargs.items()):
        print(f'{key}: {value}')

ls = [i for i in range(10, 100)]
'''enumerate - возвращает 2 параметра: индекс элемента и сам элемент'''
for inx, el in enumerate(ls):
    print(inx, el)


# 15.4 Функции как объекты
"""Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и 
max() выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое значение элементов."""
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]
print(min(numbers, key=lambda mean: sum(mean) / len(mean)))
print(max(numbers, key=lambda mean: sum(mean) / len(mean)))

"""Напишите программу, которая сортирует список points координат точек плоскости в соответствии с расстоянием от начала координат (точки
(0;0)). Программа должна вывести отсортированный список."""
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
points.sort(key=lambda sort_p: (sort_p[0] ** 2 + sort_p[1] ** 2) ** 0.5)
print(points)

"""Дан список numbers, содержащий кортежи чисел. Напишите программу,
которая сортирует и выводит список numbers в соответствии с суммой минимального и максимального элемента кортежа."""
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100),
           (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
def sum_d(numbers):
    return max(numbers) + min(numbers)
numbers.sort(key=sum_d)
print(numbers)

"""Сортируй как хочешь
Список athletes содержит сведения о спортсменах в виде кортежей: (имя, возраст, рост, вес).
Напишите программу сортировки списка спортсменов по указанному полю:
1: по имени;
2: по возрасту;
3: по росту;
4: по весу.
"""
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39),
            ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
            ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
def sorted_name(x):
    return x[0]
def sorted_age(x):
    return x[1]
def sorted_height(x):
    return x[2]
def sorted_mass(x):
    return x[3]
d_athletes = {1: sorted_name, 2: sorted_age, 3: sorted_height, 4: sorted_mass}
command = int(input())
q = sorted(athletes, key=d_athletes[command])
for i in q: print(*i)

"""                                 Математические функции
Напишите программу, которая принимает число и название функции, а выводит результат применения функции к данному числу.
Список возможных функций:
квадрат: функция принимает число и возвращает его квадрат;
куб: функция принимает число и возвращает его куб;
корень: функция принимает число и возвращает корень квадратный из этого числа;
модуль: функция принимает число и возвращает его модуль;
синус: функция принимает число (в радианах) и возвращает синус этого числа."""
import math
def pwr(p):
    def n_power(n):
        return n ** p
    return n_power

command_dict = {'квадрат': pwr(2), 'куб': pwr(3), 'корень': pwr(0.5), 'модуль': abs, 'синус': math.sin}
n = int(input())
command = input()
print(command_dict[command](n))

"""Интересная сортировка-1
На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр. 
При этом, если два числа имеют одинаковую сумму цифр, следует сохранить их взаиморасположение в начальном списке."""
def summator(n):
    return sum([int(i) for i in str(n)])
numbers = [int(i) for i in input().split()]
print(*sorted(numbers, key=summator))

"""Напишите программу, которая с помощью функции map() округляет все элементы списка numbers до 2 десятичных знаков,
а затем выводит их, каждый на отдельной строке."""
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result
def map_2(x):
    return round(x, 2)
numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*map(map_2, numbers))


def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result
def number_if(x):
    return len(str(x)) == 3 and x % 5 == 2
def cube_number(x):
    return x ** 3


numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657,
           1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163,
           345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349,
           831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018,
           1274, 387, 120, 340, 963, 832, 1127]
print(*map(cube_number, filter(number_if, numbers)), sep='\n')

def reduce(operation, items, initial_value):
    acc = initial_value
    for item in items:
        acc = operation(acc, item)
    return acc
def square(s, x):
    return s + x ** 2


numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23,
           35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67,
           62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29,
           84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
print(reduce(square, numbers, 0))

"""Напишите программу для вычисления и вывода суммы квадратов двузначных чисел из списка numbers, которые делятся на 7 без остатка.
Примечание 1. При решении задачи используйте функции filter(), map() и sum().
Примечание 2. На 7 должно делиться исходное двузначное число, а не его квадрат.
Примечание 3. Не забывайте про отрицательные двузначные числа."""
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result


def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def seven_number(x):
    return len(str(abs(x))) == 2 and x % 7 == 0
def square_number(x):
    return x ** 2

numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202,
           58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208,
           231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128,
           143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135,
           7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73,
           197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129,
           39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]

print(sum(map(square_number, filter(seven_number, numbers))))

# from operator import *     #  импортируем все функции
#
# print(add(10, 20))         #  сумма
# print(floordiv(20, 3))     #  целочисленное деление
# print(neg(9))              #  смена знака
# print(lt(2, 3))            #  проверка на неравенство <
# print(lt(10, 8))           #  проверка на неравенство <
# print(eq(5, 5))            #  проверка на равенство ==
# print(eq(5, 9))            #  проверка на равенство ==

"""Напишите программу, которая с помощью встроенных функций filter(), map(), sorted()
и reduce() выводит в алфавитном порядке список primary городов с населением более 10000000 человек"""
from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

cities = filter(lambda city: city[1] > 10 ** 7 and city[2] == 'primary', data)
cities = map(lambda city: city[0], cities)
cities = sorted(cities)
cities = 'Cities: ' + reduce(lambda city1, city2: f'{city1}, {city2}', cities)
print(cities)


"""Список data содержит слова на русском языке. Напишите программу,
которая сортирует этот список по возрастанию длины слов. В случае, если длины каких-то слов совпадают, – отсортировать
 эти слова в лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела."""
data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
data = sorted(data, key=lambda el: el[1][-1], reverse=True)
for i in data: print(f'{i[1]}: {i[0]}')

"""Список data содержит слова на русском языке. Напишите программу, которая сортирует этот список по возрастанию длины слов.
В случае, если длины каких-то слов совпадают, – отсортировать эти слова в лексикографическом порядке.
Отсортированные слова следует вывести на одной строке, разделив символом пробела."""
data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
        'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
        'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
#Внимание на кортеж в анонимной функции. Условия выполняются последовательно, если по первому условию слова равны, берется второе условие
print(*sorted(data, key=lambda x: (len(x), x)))

mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
              'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271,
              2680434, 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides',
              'bewilder', 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent',
              'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet',
              859105, 'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish',
              'beware', 2618492, 1555062, 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon',
              2284251, 'wednesday', 2709698, 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse',
              'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
mixed_list = max(filter(lambda x: type(x) == int, mixed_list), key=int)
print(mixed_list)

"""Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию значений элементов,
при этом числа должны следовать до строк. Элементы отсортированного списка выведите на одной строке, разделив символом пробела."""
mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday',
              76, 70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort', 13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory', 20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide', 'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66, 'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
print(*sorted(filter(lambda x: type(x) == int, mixed_list)) +
       sorted(filter(lambda x: type(x) == str, mixed_list)))

#Противоположный цвет
print(*list(map(lambda x: 255 - x, [int(i) for i in input().split()])))

#Значение многочлена 🌶️
from functools import reduce
evalute = lambda coeff, x: reduce(lambda s, a: s * x + a, coeff)
print(evalute(map(int, input().split()), int(input())))

"""Функция ignore_command() принимает на вход один строковый аргумент command – команда, которую нужно проверить,
и возвращает значение True, если в команде содержится подстрока из списка ignore, или False – если нет.
"""
def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(filter(lambda x: x in command, ignore))

# """Используя параллельную итерацию сразу по трем спискам countries, capitals и population,
# выведите информацию о стране в формате:"""
countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for x, y, z in zip(countries, capitals, population):
    print(f'{y} is the capital of {x}, population equal {z} people.')



abscissas = [float(i) for i in input().split()]
ordinates = [float(i) for i in input().split()]
applicates = [float(i) for i in input().split()]
print(all(map(lambda x: x[0] ** 2 + x[1] ** 2 + x[2] ** 2 <= 4,
              zip(abscissas, ordinates, applicates))))

Корректный IP-адрес
print(all(map(lambda x: x.isdigit() and 0 <= int(x) <= 255, input().split('.'))))

Интересные числа
a, b = int(input()), int(input())
for i in range(a, b + 1):
    digits = [int(q) for q in str(i)]
    if all(map(lambda x: x != 0 and i % x == 0, digits)):
        print(i, end=' ')

Хороший пароль
s = input()
print('YES'if all((any(i.isdigit() for i in s),
           any(i.islower() for i in s),
           any(i.isupper() for i in s),
           len(s) >= 7)) else 'NO')

Отличники
ls = []
for i in range(int(input())):
    ls.append(any(['5' in input() for q in range(int(input()))]))
print('YES' if all(ls) else 'NO')

def generate_letter(mail, name, date, time, place, teacher = 'Тимур Гуев', number = 17):
    return f'''To: {mail}
Приветствую, {name}!
Вам назначен экзамен, который пройдет {date}, в {time}.
По адресу: {place}.
Экзамен будет проводить {teacher} в кабинете {number}.
Желаем удачи на экзамене!'''

def pretty_print(data, side = '-', delimiter = '|'):
    stroka = f' {delimiter} '.join(map(str, data))
    print('', (len(stroka) + 2) * side)
    print(delimiter, stroka, delimiter)
    print('', (len(stroka) + 2) * side)


