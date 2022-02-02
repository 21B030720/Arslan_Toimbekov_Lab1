l1 = input()
l2 = l1.split(' ')
a, b = l2
a = int(a)
b = int(b)
truth = True
if a > 500:
    truth = False
else:
    for i in range(2, a//2):
        if(a % i == 0):
            truth = False
if b % 2 == 1:
    truth = False

if truth:
    print("Good job!")
else:
    print("Try next time!")