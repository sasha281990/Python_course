# number = 73408
# m = 0
# s = 0
# while number > 0:
#     last_digit = number % 10
#     s = s + last_digit
#     if last_digit > m:
#         m = last_digit
#     number = number // 10
# print(s + m)
#
# a, b = map(int, input().split())  # Ввод чисел
# a1, b1 = a, b                     # для НОК
#
# while b > 0:
#     a, b = b, a % b
# print(f'НОД - {a}')
# print(f'НОК - {a1 * b1 / a}')      # На всякий случай: Произведение(умножить) вводимых чисел делим на НОД
# i = 0
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# else:
#     print("Конец")

# for i in range(13):
#     print("Надо было брать биткоин в 2012!")

# Напишите программу, которая найдет сумму кубов натуральных чисел от 50 до 100 включительно
# 503 + 513 + 523 + 533 + ... + 1003

# a = 0
# for i in range(50, 101):
#     a = a + (i ** 3)
# print(a)
#
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("The factorial of", n, "is", factorial)
