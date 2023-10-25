# Напишите программу, которая  принимает на вход три целых числа в одной строке через пробел
# и выводит их последовательно через запятую как в примерах ниже

a, b ,c = map(int,input().split())
print(a, b, c, sep=',')

# Программа, считывает натуральное число n, после чего выводит двойное неравенство
# этого числа с его соседними числами.

n = int(input())
print((n - 1), n, (n + 1), sep='<')

# Вам необходимо вывести три фразы, разделяя их тремя дефисами.
# Сами фразы вводятся с клавиатуры на трех разных строчках

a = str(input())
b = str(input())
c = str(input())
print(a, b, c, sep='---')

# В этой задаче мы сами будем решать, какое значение использовать в качестве разделителя в параметре sep
# Программа принимает на вход строку - разделитель, вам необходимо распечатать числа от 1 до 5,
# выводя между ними введенный разделитель

print(1, 2, 3, 4, 5, sep=str(input()))

# Давайте и мы напишем такую программу. Она принимает на вход предложение и и затем печатает его с
# фразой «Сказала она!» в конце определенным образом (см. примеры).
# Пользуйтесь аргументом end и следите за символами, которые печатаются.

a = str(input())
print(a, end=' - Сказала она!')