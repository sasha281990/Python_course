# Программа получает на вход строку и ваша задача вывести первый элемент данной строки

a = input()
print(a[0])

# Программа получает на вход строку и ваша задача вывести последний символ этой строки

a = input()
print(a[-1])

# Программа получает на вход строку и ваша задача вывести первые 4 символа этой строки
# Гарантируется, что вводится будет строка длиной не менее 4 символов

a = input()
print(a[:4])

# Программа получает на вход строку и ваша задача вывести последние 4 символа этой строки
# Гарантируется, что вводится будет строка длиной не менее 4 символов

a = input()
print(a[-4:len(a)])

# Программа получает на вход строку. Ваша задача вывести все символы этой строки, которые имеют четные индексы

a = input()
print(a[::2])

# Программа получает на вход строку. Ваша задача вывести все символы этой строки, которые имеют нечетные индексы

a = input()
print(a[1::2])

# Программа получает на вход строку. Ваша задача развернуть строку и вывести ее на экран.

a = input()
print(a[::-1])

# Выведите каждый третий символ строки в обратном порядке, начиная с последнего.

a = input()
print(a[::-3])