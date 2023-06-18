# Codeup_Python 기초5-2.문자열_1754: 큰 수 비교

a,b = map(int, input().split())
if a>b:
    a,b=b,a
print(a,b)