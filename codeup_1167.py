# Codeup_Python 기초3.if~else_1167: 두 번째 수

# 1. sort함수를 사용하는 방법
a = list(map(int, input("정수 3개를 입력하세요: ").split()))
a.sort()
print(a[1])

# 2. 문제의 취지대로 if~else문 사용하는 방법
a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
if a>b:
    if b>c:
        print(b)
    else:
        if a>c:
            print(c)
        else: 
            print(a)
else:
    if b>c:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        print(b)