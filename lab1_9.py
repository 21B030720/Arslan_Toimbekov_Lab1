l = [] # лист, содержащий все адресы
a = int(input()) # ввод числа адресов
for i in range(a): # логика отбора номеров
    s = str(input())
    if s.count("@gmail.com"):
        pos = int(s.find("@gmail.com"))
        s = s[0: pos]
        l.append(s)
for i in range(len(l)): # вывод всех подходящих адресов
    print(l[i])
