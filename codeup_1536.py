# Codeup_Python 기초100제_1536: 함수로 가장 작은 값 리턴하기

n=int(input())
a=list(map(int,input().split()))
def f(): 
    print(min(a))
f()

'''
이런 풀이도 가능하다. 
input()함수대신에 sys모듈(파이썬 인터프리터를 제어)을 사용하면 좋다.
반복문으로 여러줄 입력받을때, input()은 시간초과를 발생시킬 수 있다.
참고로 한개의 정수를 입력받을때 sys.stdinreadline()은 한줄 단위로 입력된다(즉, 기본적으로 입력값에 \n도 같이 저장됨)
여러개 정수 입력받을때는 map()함수를 활용한다. 
'''
import sys
n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]      # 여기서 map(int, sys.stdin.readline().split())해도 된다. 난 리스트컴프리헨션을 썼다.
print(min(a))