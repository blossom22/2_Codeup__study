# Codeup_Python 기초5-1.1차원배열_1407: 문자열 출력하기 1

a = list(input())
for i in range(len(a)):
    if a[i] == ' ':
        a[i] = ''
print(''.join(a))


# 사실 replace함수를 쓰면 간단히 해결된다.
print(input().replace(' ',''))