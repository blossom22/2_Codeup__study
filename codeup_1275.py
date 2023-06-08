# Codeup_Python 기초3.단순 반복문_1275: k 제곱 구하기

a,b=map(int, input("수를 입력하세요: ").split())
print(a**b)


# math모듈의 pow함수를 쓰는 방법도 있다. 주의할 것은 얘는 float으로 결과를 출력해서 정수를 얻으려면 반올림과정이 필요하다. 
import math
a, b = map(int, input("수를 입력하세요: ").split())
print(round(math.pow(a, b)))