# Codeup_Python 기초5-3.2차원배열_1508: 나도 IQ 150

n = int(input())
m = []
for i in range(1, n+1):
    tmp = [0] * i
    m.append(tmp)
    
for i in range(0, n):
    num = int(input())
    m[i][0] = num
    for j in range(1, len(m[i])):
        m[i][j] = m[i][j-1] - m[i-1][j-1]
        
for i in range(0, n):
    for j in range(0, len(m[i])):
        print(m[i][j], end=' ')
    print()

