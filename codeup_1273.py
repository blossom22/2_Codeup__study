# Codeup_Python 기초3.단순 반복문_1273: 약수 구하기

n=int(input("자연수를 입력하세요: "))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")


# 아래는 리스트 컴프리헨션으로 푼 방식이다. 
n=int(input("자연수를 입력하세요: "))
a=[i for i in range(1,n+1) if n%i==0]
print(*a)       # 리스트의 원소들을 대괄호 없이 출력하려면 리스트이름앞에 * 붙여서 출력시키면된다. 
