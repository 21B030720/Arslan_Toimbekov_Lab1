l = [] # лист, которая будет содержать результаты
a = int(input()) # вводимое количество дней
sum = int(0) # просто так

for i in range(a): # логика
    b = int(input())
    if b <= 10:
        l.append("Go to work!")
        #l[sum] = "Go to work!"
    elif b <= 25:
        l.append("You are weak")
        #l[sum] = "You are weak"
    elif b <= 45:
        l.append("Okay, fine")
        #l[sum] = "Okay, fine"
    else:
        l.append("Burn! Burn! Burn Young!")
        #l[sum] = "Burn! Burn! Burn Young!"
    sum += 1
for i in range(sum): # вывод результата
    print(l[i])
