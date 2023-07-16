# Codeup_Python 기초100제_1620: 자릿수의 합

def f(a):
    b = sum(int(i) for i in a)
    print(b) if b<10 else f(str(b))
a = input()
f(a)


# lambda를 써서 코드를 간결하게 만들수있다
f=lambda a:print(a)if(int(a)<10)else f(str(sum(int(i)for i in a)))
f(input())