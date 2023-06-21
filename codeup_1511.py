# Codeup_Python 기초5-3.2차원배열_1511: 테두리의 합

n = int(input())
a=0
arr = [[0] * n for _ in range(n)]
num = 1
for j in range(n):
    for i in range(n):
        arr[j][i] = num
        num += 1
a+=sum(arr[0]+arr[-1])
for i in range(1,n-1):
    a+=arr[i][0]
    a+=arr[i][-1]
print(a)