c = 0
a = float(input())
char = input()
if char == 'k':
    c = int(input())
    a /= 1024
    m = "{0:." + str(c) + "f}"
    if True:
        print(m.format(a))
else:
    print(int(a) * 1024)