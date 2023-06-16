# Codeup_Python 기초5-1.1차원배열_1420: 3등 찾기

n=int(input())
a=[]
b=[]
for i in range(n):
    a.append((input().split()))
    b.append(int(a[i][1]))
b.sort()
c=str(b[-3])
for i in range(n):
    if c in a[i][1]:
        print(a[i][0])
