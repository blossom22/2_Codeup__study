# Codeup_Python 기초5-1.1차원배열_1412: 알파벳 개수 출력하기

import string
s = input("문장을 입력하세요: ")
alpha = {i: 0 for i in string.ascii_lowercase}      # 알파벳 개수를 저장할 딕셔너리 설정
for char in s:
    # 소문자 알파벳인 경우에만 개수 세기
    if char.islower():              # islower, isupper는 각각 함수앞의 문자(여기서는 char)가 소문자인지, 대문자인지 확인해서 boolean형태로 출력한다. 
        alpha[char] += 1            # 소문자인경우, 그 char에 해당하는 value를 1더해

for i, count in alpha.items():      # 사용되지 않은 알파벳에 대해 0으로 표시
    if count == 0:
        print(f"{i}:0")
    else:
        print(f"{i}:{count}")
