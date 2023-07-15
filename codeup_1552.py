# Codeup_Python 기초100제_1552: 함수로 소수 부분만 리턴하기

def f(n):
    decimal_part = n - int(n)
    formatted_decimal = "{:.14f}".format(decimal_part)
    print(formatted_decimal)

n = float(input())
f(n)