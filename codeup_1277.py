# Codeup_Python 기초3.단순 반복문_1277: 몇 번째 데이터 출력하기

n=int(input("자연수를 입력하세요: "))
a=list(map(int, input("수를 입력하세요: ").split()))
print(a[0], a[n//2], a[n-1])