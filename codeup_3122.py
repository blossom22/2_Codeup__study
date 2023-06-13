# Codeup_Python 기초4-2.중첩반복문_3122: 마름모 출력하기 2

n = int(input("길이를 입력하세요: "))
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n-2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))