# Codeup_Python 기초3.if~else_1206: 배수

a, b=map(int, input("자연수를 입력하세요: ").split())
if a%b==0:
    c=a//b
    print("{}*{}={}".format(b,c,a))     # format말고 다른식으로 문자열 속에 값을 넣는 방법은 아래에 적어두었다. 
elif b%a==0:
    c=b//a
    print("{}*{}={}".format(a,c,b))
else:
    print("none")

# %d 쓰는방법
# print('%d*%d=%d'%(b,c,a)) 
# 참고로 %s는 문자열을 넣는 것이고, %d는 숫자를 넣을때 쓴다.