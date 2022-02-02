l = []
a = int(input())
for i in range(a):
    s = str(input())
    if s.count("@gmail.com"):
        pos = int(s.find("@gmail.com"))
        s = s[0: pos]
        l.append(s)
for i in range(len(l)):
    print(l[i])