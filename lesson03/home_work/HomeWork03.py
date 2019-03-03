# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, numsing):
    number = number * (10 ** numsing) + 0.41
    number = number // 1
    return number / (10 ** numsing)

print(my_round(123.4567890123, 2))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky(number_n):
    s1 = int(number_n[:1]) + int(number_n[1:2])
    s2 = int(number_n[-1]) + int(number_n[-2])
    if s1 == s2:
        return 'lucky %s ticket' %number_n
    else:
        return 'dont lucky %s ticket' %number_n


number_n = input('Please you ticket: ')
print(lucky(number_n))

#NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonachi(n,m):
    a = 0
    b = 1
    list_f = [0,]
    for i in range(n,m):
        a, b = b, a + b
        list_f.append(a)
    return  list_f[n - 1:m]

print('fibonachi(1, 12): ', fibonachi(1, 12))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


#HARD

# Задание-1

# Написать консольное меню вида:

# 1. Добавить
# 2. Удалить
# 3. Распечатать
# 4. Посчитать
# 5. Выйти

# Надо чтобы
# а) Можно было удобно менять порядок меню и\или добавлять\удалять пункты меню
# б) Каждое действие (добавить, удалить и тд) должно быть функцией
# в) У пользователя надо спросить номер команды
# г) Программа не должна завершаться пока не введется команда Выйти
# д) Проверять на ввод ошибочных данных, там где они могут появиться

database = []
database_filename = 'data.txt'


def add():
    global database
    data = input('Input data')
    database.append(data)

def save():
    global database_filename
    global database
    with open(database_filename, 'w') as f:
        f.write(','.join(database))


def load():
    global database_filename
    global database
    with open(database_filename, 'r') as f:
        database = f.read().split(',')


def delete():
    global database_filename
    global database
    with open(database_filename, 'wb') as f:
        pass

def print_data():
    global database

    if len(database) == 0:
        print('No data')

    for i in database:
        print(i)

def calculate():

    c_a = float(input('Number one:'))
    c_b = float(input('Number two:'))
    c_i = input('Please chois: * , /, -, + : ')

    if c_i == '*':
        print(c_a * c_b)
    elif c_i == '/':
        print(c_a / c_b)
    elif c_i == '-':
        print(c_a - c_b)
    elif c_i =='+':
        print(c_a + c_b)
    else:
        print('Error')

def print_menu(menu):
    for i,m in enumerate(menu, start=1):
        print(f'{i}. {m}')

def get_command(menu):
    command = int(input('Input command: '))

    if 1<= command <= len(menu):
        return command
    else:
        return -1



menu = ['Add', 'Save', 'Load', 'Deleted', 'Print', 'Calculate', 'Exit']
commands = [add, save, load, delete, print_data, calculate, exit]



while True:
    print_menu(menu)
    command = get_command(menu)

    if command == -1:
        print('Wrong command')
        continue

    commands[command-1]()