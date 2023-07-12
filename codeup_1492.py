# Codeup_Python 기초5-3.2차원배열_1492: 1차원 누적 합 배열 만들기 5-1

n = int(input())
a = list(map(int, input().split()))
b = 0
c = []
for i in a:
    b += i
    c.append(b)
print(*c)