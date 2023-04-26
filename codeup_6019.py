# Codeup_Python 기초100제_6019: 연월일 입력받아 순서 바꿔 출력하기
y, m, d = input("연,월,일을 '.'으로 구분하여 입력하세요: ").split('.') 
print(d,m,y, sep='-')