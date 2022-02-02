a = str(input())
t = input()
l = []
for i in range(len(a)):
    if(a[i] == t):
        l.append(i)
if l[len(l) - 1] != l[0]:
    print(str(l[0]) + " " + str(l[len(l) - 1]))
else:
    print(l[0])