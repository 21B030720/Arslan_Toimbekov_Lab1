l = []
a = int(input())
sum = int(0)

for i in range(a):
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
for i in range(sum):
    print(l[i])