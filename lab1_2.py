a = input()

sum = 0
for i in range(len(a)):
    p = a[i]
    sum += ord(p)
if sum >= 300:
    print("It is tasty!")
else:
    print("Oh, no!")

