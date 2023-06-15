# Codeup_Python 기초5-1.1차원배열_1416: 2진수 변환

print(format(int(input()),'b'))

# 이렇게도 풀수있다. bin을 쓸경우, 접두어를 빼줘야해서 슬라이싱 했다. 
num = int(input())
binary = bin(num)[2:]
print(binary)