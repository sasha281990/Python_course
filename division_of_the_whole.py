# Напишите программу, которая найдет сколько полных килограмм умещается в заданное число грамм.

a = int(input())
print(a // 1000)

# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Программа получает на вход сперва число n, а потом k.

n = int(input())
k = int(input())
print(k // n)

# У вас есть N рублей и вы хотите купить максимальное количество пар кроссовок по цене R рублей.
# Сколько пар кроссовок Вы можете себе купить?
# На вход программе поступают два натуральных числа N и R

N = int(input())
R = int(input())
print(N // R)

# Программе поступает на вход одно целое положительное число, ваша задача вывести его последнюю цифру

a = int(input())
print(a % 10)

# Дано целое положительное число, ваша задача вывести разряд сотен этого числа

a = int(input())
print(a // 100 % 10)

# Дано целое положительное трехзначное число, ваша задача найти сумму разрядов этого числа

a = int(input())
print((a % 10)+(a % 100 // 10) + (a % 1000 // 100))

# У Олега в банке есть n евро. Он хочет снять всю сумму наличными. Номиналы еврокупюр равны 1, 5, 10, 20, 100.
# Какое минимальное число купюр должен получить Олег после того, как снимет все деньги?
# На вход программе поступает одно положительные целое число n.

n = int(input())
k_100 = n // 100
n = n % 100
k_20 = n // 20
n = n % 20
k_10 = n // 10
n = n % 10
k_5 = n // 5
n = n % 5
k_1 = n // 1
d = k_100 + k_20 + k_10 + k_5 + k_1
print(d)

# Дано число n. С начала суток прошло n минут. Определите, сколько часов и минут будут
# показывать электронные часы в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23) и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках.

n = int(input())
n = n % 1440
print(n // 60, n % 60)

# Дано целое число n. Выведите следующее за ним четное число.
# Задачу необходимо решить целочисленными операциями без использования условных операторов и\или циклов.

n = int(input())
print((n // 2 + 1) * 2)

# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов в диапазоне
# от 0 до 23, потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд.
# Количество минут и секунд при необходимости дополняются до двузначного числа нулями.
# Программа получает на вход число n - количество секунд, которое прошло с начала суток.
# Выведите показания часов, соблюдая формат.

n = int(input())
h = n // 3600
m = n % 3600 // 60
s = n % 3600 % 60 // 1
print(h, str(m).zfill(2), str(s).zfill(2), sep=':')

