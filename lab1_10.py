a = str(input()) # Ввод строки
l = a.split(" ") # Присвоение слов строки к листу
b = "" # Результат 
for i in range(len(l)): # Логика
    if len(l[i]) >= 3:
        b += l[i] + " "
print(b) # вывод результата
