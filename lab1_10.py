a = str(input())
l = a.split(" ")
b = ""
for i in range(len(l)):
    if len(l[i]) >= 3:
        b += l[i] + " "
print(b)
