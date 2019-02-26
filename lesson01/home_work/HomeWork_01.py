#Дз от Пака

#EASY
#Задача-1: Дано произвольное целое число (число заранее неизвестно).
#Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
#Подсказки:
#* постарайтесь решить задачу с применением арифметики и цикла while;
#* при желании решите задачу с применением цикла for.

#код пишем тут...
print("Please enter number: ")
num = input()

i = 0
while i <len(num):
    print(num[i])
    i+=1

#Задача-2: Исходные значения двух переменных запросить у пользователя.
#Поменять значения переменных местами. Вывести новые значения на экран.
#Подсказка:
#* постарайтесь сделать решение через дополнительную переменную
#или через арифметические действия
#Не нужно решать задачу так:
#print("a = ", b, "b = ", a) - это неправильное решение!

print("Please enter 2 variable")
_a = input("Variable 1: ")
_b = input("Variable 2: ")

_c = _a
_a = _b
_b = _c

print("Variable 1: ", _a, "Variable 2: ", _b)


#Задача-3: Запросите у пользователя его возраст.
#Если ему есть 18 лет, выведите: "Доступ разрешен",
#иначе "Извините, пользование данным ресурсом только с 18 лет"

age = int(input("Please enter age: "))

if age >= 18:
    print("Access is allowed")

elif age <= 17:
    print("Sorry, use this resource only with 18 years")

else:
    print("error")


#NORMAL
#Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
#Например, дается x = 58375.
#Нужно вывести максимальную цифру в данном числе, т.е. 8.
#Подразумевается, что мы не знаем это число заранее.
#Число приходит в виде целого беззнакового.
#Подсказки:
#* постарайтесь решить задачу с применением арифметики и цикла while;
#* при желании и понимании решите задачу с применением цикла for.


number = input("Please enter number:")

i = 0

while i < len(number):
    print(max(number))
    break 


#Задача-2: Исходные значения двух переменных запросить у пользователя.
#Поменять значения переменных местами. Вывести новые значения на экран.
#Решите задачу, используя только две переменные.
#Подсказки:
#* постарайтесь сделать решение через действия над числами;
#* при желании и понимании воспользуйтесь синтаксисом кортежей Python.
#a = input("Input a: ")
#b = input("Input b: ")
#a,b = b,a


a1 = input("Enter a: ")
b1 = input("Enter b: ")

a1,b1 = b1,a1

print("The program changed places, a now:",a1, "b now: ",b1)


#Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
#ax² + bx + c = 0.
#Коэффициенты уравнения вводятся пользователем.
#Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
#import math
#math.sqrt(4) - вычисляет корень числа 4


import math

#a = int(input())

#b = math.sqrt(a)

#print(b)


print("The program outputs the roots of the square equation view's: ax² + bx + c = 0")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = (b**2) - (4*a*c)

if D > 0:
    _D = math.sqrt(D)
    x1 = ((-b) - _D) / (2*a)
    x2 = ((-b) + _D) / (2*a)
    print("X1 = ", x1)
    print("X2 = ", x2)

elif D == 0:
    x1 = (-b) / (2*a)
    print("The equation has only one root X = ", x1)

elif D < 0:
    print("The equation has no roots")


#HARD
#Задание-1:
#Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу

print("Checking numbers")

n = int(input("Enter number: "))

for aa in range (2, n):

    if (n % aa) == 0:
        print("Number: ", n, "is not easy")
        break

    elif (n % aa) > 0:
        print("Prime number: ", n)
        break



#Задание-2
#Найдите n-ое число Фибоначчи



#Задание-3
#Вывести на экран:
#AAABBBAAABBBAAABBB
#BBBAAABBBAAABBBAAA
#AAABBBAAABBBAAABBB
#(таких строк n, в каждой строке m троек AAA)

