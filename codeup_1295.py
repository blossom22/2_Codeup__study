# Codeup_Python 기초3.if~else_1295: 알파벳 대소문자 변환
# chr와 ord함수로 푸는 방식이다. 
a=input("원문을 입력하세요: ")
b=[]
for i in range(len(a)):
    if 96<ord(a[i])<123:
        b.append(chr(ord(a[i])-32))
    elif 64<ord(a[i])<91:
        b.append(chr(ord(a[i])+32))
    else:
        b.append(a[i])
print(''.join(b))



# swapcase라는 함수를 쓰는 방법도 있다. 이 함수는 영문 대소문자를 전환해준다. 
print(input().swapcase())
