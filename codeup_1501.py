# Codeup_Python 기초5-3.2차원배열_1501: 2차원 배열 채우기 1

n = int(input())
a = n**2+1
for i in range(1, a):
    print(i, end=' ')
    if i % n == 0:
        print()