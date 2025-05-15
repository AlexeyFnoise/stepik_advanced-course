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