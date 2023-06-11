# Codeup_Python 기초4-2.중첩반복문_1353: 삼각형 출력하기 1

n = int(input("자연수를 입력하세요: "))
for i in range(1,n+1):
    print('*'*i)

# join함수로도 풀 수 있다.
n = int(input("자연수를 입력하세요: "))
print('\n'.join('*' * (i + 1) for i in range(n)))