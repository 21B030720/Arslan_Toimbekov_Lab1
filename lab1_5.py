l1 = input() # ввод строки
l2 = l1.split(' ') # присвоение каждого слова строки к лист
a, b = l2 # присвоение переменным значения с листа. Хотя мог укоротить первые 3 строки до 2
a = int(a) #  убеждаюсь, что переменная - это число
b = int(b) # тоже самое
truth = True # логика буллеана, которую можно перевести в ложь любым несоответсвием с требованием
# логика, находящая несоответствие
if a > 500:
    truth = False
else:
    for i in range(2, a//2):
        if(a % i == 0):
            truth = False
if b % 2 == 1: 
    truth = False

if truth: # вывод результата в зависимости буллеана логики
    print("Good job!")
else:
    print("Try next time!")
