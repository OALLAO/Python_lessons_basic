#EASY
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# Учесть проверку на то что папка не пуста и на то, что такая папка уже существует

import os

def create_dir(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print(f'{name} already exist')

def remove_dir(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print(f'{name} folder does not exist')

inp = ''
quantity_dirs = range(1,10)

while inp != '3':
    inp = input('Please enter number:\n'
                '1. Create dirs\n'
                '2. Remove dirs\n'
                '3. Exit\n'
                'Enter: ')
    if inp == '3':
        break
    elif inp == '1':
        for i in quantity_dirs:
            i = str(i)
            create_dir('dir_'+ i)

    elif inp == '2':
        for i in quantity_dirs:
            i = str(i)
            remove_dir('dir_'+ i)


# Задача-2:
# Напишите скрипт, который выводит в консоль список файлов и папок в указанной директории.

def listdir_list():
    print('list of files and folders: ')
    for i,e in enumerate(os.listdir(), start=1):
        print(f'{i}.{e}')


listdir_list()

#NORMAL

# Написать две программы:
# Одна принимает через argparse число N и текст S и в цикле N раз выводит S в консоль
# А вторая программа принимает через input число M
# И указанное кол-во раз спрашивает через input N и S и запускает первую программу через os.system

#HARD

# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

# BASE_PATH = r"D:\Programming education\Access course\The basics of the language Python (Online)\Lesson 5\test"
# # Определить какие у меня в папке расширения у файлов
# ext = set()
# for i in os.listdir(BASE_PATH):
#     if os.path.isfile(os.path.join(BASE_PATH, i)):
#         print(os.path.splitext(i))
#         ext.add(os.path.splitext(i)[1]) # добавить в множество расширение текущего файла
#
# # print(ext)
# # Создаем папки
# for e in ext:
#     if not os.path.exists(os.path.join(BASE_PATH, e)):
#         os.mkdir(os.path.join(BASE_PATH, e))
#
# # Переносим файлы в соответствующие каталоги
# for i in os.listdir(BASE_PATH):
#     if os.path.isfile(os.path.join(BASE_PATH, i)):
#         os.rename(os.path.join(BASE_PATH, i),
#                   os.path.join(BASE_PATH, os.path.splitext(i)[1], i))

import os

BASE_PATH = r"D:\Programming education\Access course\The basics of the language Python (Online)\Lesson 5\test"
for i in os.listdir(BASE_PATH):
    if os.path.isdir(BASE_PATH):
        for j in os.listdir(os.path.join(BASE_PATH,i)):
            if os.path.isfile(os.path.join(BASE_PATH,i,j)):
                os.rename(os.path.join(BASE_PATH, i, j), os.path.join(BASE_PATH, j))
for i in os.listdir(BASE_PATH):
    if os.path.isdir(os.path.join(BASE_PATH,i)):
        os.rmdir(os.path.join(BASE_PATH,i))
