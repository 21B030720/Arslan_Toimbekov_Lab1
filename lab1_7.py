a = str(input())
a = a[::-1]
num = 0
sum = 0
for i in range(len(a)):
    sum += int(a[i]) * (2**num)
    num += 1
print(sum)