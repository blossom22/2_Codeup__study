# Codeup_Python 기초5-1.1차원배열_1425: 자리 배치

n, c = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
b = []
for i in range(n):
    b.append([a[i]])
for i in range(n):
    if i < c:
        print(*b[i], end=' ')
    elif i == c:
        print(*b[i], end=' ')
    else:
        print(*b[i], end=' ')
    if (i + 1) % c == 0 or i == n - 1:      # i가 c의 배수이거나 마지막 행인경우, 한번의 줄바꿈을 한다. 
        print()