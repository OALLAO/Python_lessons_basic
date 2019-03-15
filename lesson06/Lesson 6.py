# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для вычисления (не печати, нужен return) площади, периметра  и вывод значений сторон треугольника на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой треугольник нельзя создать и сделать exit(1)


class Tri:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


        if self.a == 0 or self.b == 0 or self.c == 0:
            return exit('parameters must not contain zero')

    def param(self):
        return 'side a=',self.a,'side b=',self.b,'side c=',self.c

    def s_abc(self):
        p_per = self.per_abc()/2
        return (p_per*(p_per-self.a)*(p_per-self.b)*(p_per-self.c))**0.5, self.param()

    def per_abc(self):
        return self.a + self.b + self.c


tri = Tri(6,8,4)

print(tri.per_abc())
print(tri.s_abc())


# Задание-2:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно) комплексными числами \ матрицами \ светофор \ микроволновка
