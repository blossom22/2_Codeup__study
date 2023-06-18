# Codeup_Python 기초5-2.문자열_6131: 일차 방정식 ax±b=c의 해 구하기

a = input()
b = a.index('x')
c = a.index('=')

n = int(''.join(a[c+1:]))
d = int(''.join(a[:b]))

if a[b+1] == '+':
    result = (n - int(''.join(a[b+2:c]))) / d
else:
    result = (n + int(''.join(a[b+2:c]))) / d

print('{:.2f}'.format(result))