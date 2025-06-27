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
numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
result = {i: numbers[i] ** 2 for i in range(len(numbers))}
print(result)

#Генератор словарей 5
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
result = {int(el.split(':')[0]): el.split(':')[1] for el in s.split()}
print(result)