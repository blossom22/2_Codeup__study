# Codeup_Python 기초100제_6064: 정수 3개 입력받아 가장 작은 값 출력하기
# 단, 3항 연산을 사용해서 풀어라. 
a, b, c = map(int, input("정수 3개를 입력하세요: ").split())
d = (a if a<b else b) if ((a if a<b else b)<c) else c
print(d)



