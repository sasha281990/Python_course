# Программа получает на вход фразу, ваша задача посчитать из скольких слов состоит данная фраза.
# Для удобства будем считать словом любую последовательность символов.

a = input()
print(len(a.split()))

# Ниже перед вами представлен список list_strings, состоящий из строк.
# При помощи метода .join и соединителя - получите строку из этих элементов и выведите ее на экран

list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
print('-'.join(map(str, list_strings)))

# Напишите программу, которая проверяет начинается ли введенная фраза строкой mam вне зависимости от регистра букв
# В качестве ответа необходимо вывести True, если введенная строка начинается с mam,
# во всех остальных случаях нужно вывести False

a = input()
a = a.lower()
print(a[0:3] == 'mam')

# Входные данные
# В отдельных строках вводятся два значения: сперва строка s, затем строка postfix
# Выходные данные
# Нужно вывести True, если введенная строка s заканчивается строкой postfix ,
# во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать

s = input()
postfix = input()
print(s.endswith(postfix))

# Входные данные
# В отдельных строках вводится три значения: сперва строка s, затем строка prefix и потом postfix
# Выходные данные
# Нужно вывести True, если введенная строка s одновременно начинается со строки prefix и
# заканчивается строкой postfix. Во всех остальных случаях нужно вывести False. Регистр букв нужно учитывать

s = input()
prefix = input()
postfix = input()
print(s.startswith(prefix) and s.endswith(postfix))

# Напишите программу, которая проверяет состоит ли введенная строка целиком из десятичных цифр
# В качестве ответа необходимо вывести True, если условие выполняется, во всех остальных случаях нужно вывести False

a = input()
print(a.isdigit())

# Напишите программу, которая проверяет состоит ли введенная строка целиком из заглавных букв
# В качестве ответа необходимо вывести True, если условие выполняется, во всех остальных случаях нужно вывести False

a = input()
print(a.isupper())

# Напишите программу, которая проверяет состоит ли введенная строка целиком из строчных букв
# В качестве ответа необходимо вывести True, если условие выполняется, во всех остальных случаях нужно вывести False

a = input()
print(a.islower())

# На вход программе поступает строка, состоящая из произвольного количества символов.
# Ваша задача дополнить введенную строку до 15 символов в том случае, когда ей не хватает длины.
# Дополнять ее нужно символом -, ставя его в конец строки. В качестве ответа нужно вывести преобразованную строку
# Если поступала на вход строка, у которой уже имелось как минимум 15 символов,
# то преобразований выполнять никаких не нужно. Выведите строку в том виде, в котором она вводилась

a = input()
print(a.ljust(15, '-'))

# На вход программе поступает строка. Ваша задача дополнить ее впереди восклицательными знаками так,
# чтобы длина строки стала 10 символов.
# Если на вход поступила строка, длина которой уже превысила 9 символов, то дополнять ее знаками ! не нужно.
# Просто выведите строку в том виде, в котором она вводилась

a = input()
print(a.rjust(10, '!'))

# При помощи метода .center дополните введенную строку до 15 символов.
# В качестве параметра fillchar возьмите нижнее подчеркивание _

a = input()
print(a.center(15, '_'))

# На вход программе поступает натуральное число, которое не превосходит значение 109
# Ваша задача вывести данное число так, чтобы вывод занимал 10 разрядов. Если у числа не хватает разрядов,
# необходимо добавлять вперед незначащие нули.

a = input()
print(a.rjust(10, '0'))

# Вводится строка, которая может быть окружена символами -, _, !, ?
# Ваша задача избавиться от символов -, _, !, ? и вывести полученную строку

a = input()
print(a.strip('-_!?'))

# Вводится строка, которая может быть окружена символами -, _, !, ?
# Ваша задача убрать`все символы -, _, !, ? слева от строки и вывести полученный результат

a = input()
print(a.lstrip('-_!?'))

# Вводится строка, которая может быть окружена символами -, _, !, ?
# Ваша задача `убрать все символы -, _, !, ? справа от строки и вывести полученный результат

a = input()
print(a.rstrip('-_!?'))

# Входные данные
# Программе поступают последовательно три числа: значения оттенка красного, потом зеленого и затем синего цветов.
# Данные числа варьируются от 0 до 255 включительно
# Выходные данные
# Ваша задача закодировать оттенки цветов согласно RGB модели.
# Не забывайте, что на каждый цвет всегда должно отводиться два разряда.
# Символы букв в шестнадцатеричной системе необходимо записывать в верхнем регистре.
# Примечание: для перевода в 16-ую систему вы можете воспользоваться функцией hex,
# она возвращает строку перевода в 16ую систему, впереди которой находятся два служебных знака 0x

a = int(input())
b = int(input())
c = int(input())

a = hex(a)[2:].zfill(2).upper()
b = hex(b)[2:].zfill(2).upper()
c = hex(c)[2:].zfill(2).upper()

print('#' + a + b + c)
