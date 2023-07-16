# Codeup_Python 기초100제_1581: (함수 작성+포인터) swap 함수 만들기 (Call by Reference)
f = lambda a,b:print(b,a) if a>b else print(a,b)
a,b=map(int,input().split())
f(a,b)