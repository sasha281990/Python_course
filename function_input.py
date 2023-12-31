# Напишите программу, которая принимает на вход возраст человека
# (количество полных лет) и выводит сколько лет ему исполнится в следующем году.

a = int(input())
print(a + 1)

# Давайте напишем программу, которая вычисляет площадь квадрата по введенной длине.

a = float(input())
print(a ** 2)

# Напишите программу, которая принимает на вход два целых числа в отдельных строках и выводит на экран их сумму.

a = int(input())
b = int(input())
print(a + b)

# В этом задании необходимо написать программу, которая вычисляет площадь и
# периметр прямоугольника по введенной длине и ширине.

a = float(input())
b = float(input())
s = a * b
p = 2 * (a + b)
print(s, p)

# Дано значение температуры в градусах Фаренгейта.
# Определить значение этой же температуры в градусах Цельсия.
# Температура по Цельсию C и температура по Фаренгейту F связаны следующим соотношением:

f = float(input())
print((f - 32) * 5 / 9)

# Найдите результат выражения ∣a∣+∣b∣
# Значения переменных а и b поступают на вход в отдельных строках
# и могут быть только целого типа

a = abs(int(input()))
b = abs(int(input()))
print(a + b)

# Напишите программу, которая вычисляет длину отрезка
# (т.е. расстояние между двумя точками), заданного двумя значениями x1 и x2 (вещественные числа).

x1 = float(input())
x2 = float(input())
print(abs(x1 - x2))

# Вводится вещественное число и нам нужно его округлить
# до 2 и 3 разряда после запятой и вывести полученный результат через пробел в одной строчке

a = float(input())
b = round(a, 2)
c = round(a, 3)
print(b, c)

# Даны значения двух моментов времени, принадлежащих одним и тем же суткам:
# часы, минуты и секунды для каждого из моментов времени.
# Известно, что второй момент времени наступил не раньше первого.
# Определите, сколько секунд прошло между двумя моментами времени.
# Программа на вход получает три целых числа:
# часы, минуты, секунды, задающие первый момент времени и три целых числа, задающих второй момент времени.

h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
print((h2 - h1) * 3600 + (m2 - m1) * 60 + (s2 - s1))

# Петя учится в школе и очень любит математику.
# Уже несколько занятий они с классом проходят арифметические выражения.
# На последнем уроке учительница написала на доске три положительных целых числа a, b, c.
# Задание заключалось в том, чтобы расставить между этими числами знаки операций '+' и '*',
# а также, возможно, скобки. Значение получившегося выражения должно быть как можно больше.
# Рассмотрим пример: пусть учительница выписала на доску числа 1, 2 и 3.
# Вот некоторые варианты расстановки знаков и скобок:
# Обратите внимание на то, что знаки операций можно вставлять только между a и b,
# а также между b и c, то есть нельзя менять числа местами.
# Так, в приведенном примере нельзя получить выражение (1+3)*2.
# Легко убедиться, что максимальное значение, которое можно получить, — это 9.
# Ваша задача — по заданным a, b и c вывести, какое максимальное значение выражения можно получить.

a = int(input())
b = int(input())
c = int(input())
n1 = a + b + c
n2 = a * b + c
n3 = a + b * c
n4 = a * b * c
n5 = (a + b) * c
n6 = a * (b + c)
print(max(n1, n2, n3, n4, n5, n6))

# Напишите программу, которая вычисляет среднее арифметическое четырех введенных целых чисел.
# Обратите внимание, что числа вводятся в одну строку через пробел

a, b, c, d = map(int, input().split())
print((a + b + c + d)/4)

# Напишите программу, которая находит наилучшую оценку ученика за решение пяти контрольных работ.
# Оценки всех пяти работ вводятся в одну строку, могут быть только целые числа от 1 до 100

a, b, c, d, e = map(int, input().split())
print(max(a, b, c, d, e))

# Известно, что на обработку одного квадратного метра панели требуется 1г сульфида.
# Всего необходимо обработать N прямоугольных панелей размером A на B метров.
# Вам необходимо подсчитать, сколько всего сульфида необходимо на обработку всех панелей.
# И не забудьте, что панели требуют обработки с обеих сторон.

n, a, b = map(int, input().split())
print(n * (2 * a * b))

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

s = int(input())
x = s // 6
print(x, 4 * x, x)

# Однажды, посетив магазин канцелярских товаров, Вася купил X карандашей, Y ручек и Z фломастеров.
# Известно, что цена ручки на 2 рубля больше цены карандаша и на 7 рублей меньше цены фломастера.
# Также известно, что стоимость карандаша составляет 3 рубля.
# Требуется определить общую стоимость покупки.

x, y, z = map(int, input().split())
a = 3 * x
b = y * 5
c = z * 12
print(a + b + c)

# Бандиты Гарри и Ларри отдыхали на природе. Решив пострелять, они выставили на бревно несколько
# банок из-под кока-колы (не больше 10). Гарри начал простреливать банки по порядку, начиная с самой левой,
# Ларри — с самой правой. В какой-то момент получилось так, что они одновременно прострелили одну
# и ту же последнюю банку. Гарри возмутился и сказал, что Ларри должен ему кучу денег за то,
# что тот лишил его удовольствия прострелить несколько банок. В ответ Ларри сказал,
# что Гарри должен ему еще больше денег по тем же причинам.
# Они стали спорить кто кому сколько должен, но никто из них не помнил сколько банок было в начале,
# а искать простреленные банки по всей округе было неохота.
# Каждый из них помнил только, сколько банок прострелил он сам.
# Определите по этим данным, сколько банок не прострелил Гарри и сколько банок не прострелил Ларри.

a, b = map(int, input().split())
print(((a + b) - 1) - a, ((a + b) - 1) - b)

