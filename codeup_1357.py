# Codeup_Python 기초4-2.중첩반복문_1357: 삼각형 출력하기 4

a=0
n = int(input("자연수를 입력하세요: "))
while a<n:
    for i in range(1,n+1):
        print('*'*i)
        a+=1
if a>=n:        # 역순인 *표 출력하는 부분
    for i in range(n-1,0,-1):
        print('*'*i)


# join함수를 이용해보았다. 
n = int(input("자연수를 입력하세요: "))
stars = []
for i in range(1, n+1):
    stars.append('*'*i)
print('\n'.join(stars))
print('\n'.join(stars[-2::-1]))


# 리스트컴프리헨션 사용
n=int(input("자연수를 입력하세요: "))
[print('*'*i) for i in range(1,n+1)]    #리스트컴프리헨션을 사용했지만, 생성된 리스트를 반환하지 않고 반복작업만 수행하게 하였다. 
[print('*'*i) for i in range(n-1,0,-1)]


# 만약 리스트컴프리헨션으로 리스트를 반환한다면 이렇게 코드 짜겠지.
# a = ['*'*i for i in range(1,n+1)]
# print(a)
# 이렇게 쓰면 ['*', '**', '***', '****'] 이런 결과가 나온다.
