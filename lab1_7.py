def a1(sum, num, i, a):
    if i < len(a):
        sum += int(a[i]) * (2 ** num)
        num += 1
        i += 1
        a1(sum, num, i, a)
    else:
        print(sum)


i = 0
a = str(input()) # вводимая строка
a = a[::-1] # перевернуть строку, функция reverse()
num = 0 # счетчик позиции цифры 0 или 1
sum = 0 # будущее число, переведенное в десятеричную систему исчисления
a1(sum, num, i, a)
"""for i in range(len(a)): # логика перевода из двоичной в десятеричную систему исчисления
    sum += int(a[i]) * (2**num)
    num += 1
print(sum) # вывод результата"""
