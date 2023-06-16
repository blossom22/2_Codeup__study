# Codeup_Python 기초5-1.1차원배열_1440: 자리 배치

n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
    b.append([])

for i in range(n):
    c = a[:]
    for j in range(n-1):
        d = c[i]
        del c[i]
        if a[i] > c[j]:
            b[i].append('>')
            c.insert(i, d)
        elif a[i] == c[j]:
            b[i].append('=')
            c.insert(i, d)
        else:
            b[i].append('<')
            c.insert(i, d)
    print('{0}: '.format(i+1), ' '.join(b[i]), sep='')