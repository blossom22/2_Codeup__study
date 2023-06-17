# Codeup_Python 기초5-2.문자열_1418: t를 찾아라

a = input()
b = len(a)
for i in range(b):
    if a[i] == 't':
        print(i+1, end=' ')

# 코드 5~7번째줄을    [print(i+1, end=' ') for i in range(b) if a[i]=='t']    이렇게 간결하게 바꿀 수 있다. 