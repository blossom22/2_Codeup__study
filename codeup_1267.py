# Codeup_Python 기초3.단순 반복문_1267: n개의 수 중 5의 배수의 합

n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
b=0
for i in range(n):
    if a[i]%5==0:
        b+=a[i]
print(b)

# 위에서 푼 것은 입력 받은 수를 반복문에서 하나씩 확인하며 5의 배수인지 검사하고 더하는 방식이다. 
# 이렇게 하지않고 리스트 컴프리헨션을 사용하여 5의 배수인 수들만 따로 추출하여 계산하면 반복문의 실행 횟수를 줄일 수 있을것이다. 
# 리스트 컴프리헨션은 리스트안에서 코드를 작성한다. 예를들어 [x for x in range(11)] 이런식으로 작성하는데, 앞의 x가 내가 리스트에 넣은 원소들이다. 
# 얘는 또 조건거는 것도 가능해서 for문과 if문을 같이쓰는 것도 가능하다. 이때 if문은 for문은 다음에 쓴다. 예: [x for x in range(1, 11) if x % 2 == 0]
# 아래는 리스트 컴프린헨션을 사용한 해결법이다. 

n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
b=[num for num in a if num % 5 == 0]
print(sum(b))