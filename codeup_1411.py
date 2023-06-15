# Codeup_Python 기초5-1.1차원배열_1411: 빠진 카드

N = int(input())
a=[int(input()) for i in range(N-1)]
for i in range(1,N+1):
    if i not in a:
        print(i)
