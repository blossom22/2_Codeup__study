# Codeup_Python 기초100제_6023: 시분초 입력받아 분만 출력하기
# split을 사용하면, 문자열을 내가 지정한 구분자로 잘라서 리스트로 넣는다. 그 후, 인덱싱으로 '분'만 뽑으면 된다. 
a = input("시분초를 입력하세요: ").split(':')
print(a[1]) 