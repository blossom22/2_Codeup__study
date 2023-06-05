# Codeup_Python 기초3.if~else_1226: 이번 주 로또

a=list(map(int, input('당첨번호를 입력하세요: ').split()))
b=list(map(int, input('내번호를 입력하세요: ').split()))
c=0                     # 동일한 번호개수를 저장하는 변수 c 
for i in range(6):      # 보너스번호 빼고 몇개가 일치하는지 카운트하여 c에 저장한다. 
    if a[i] in b:
        c+=1
if (a[6] in b) and c==5:    # 만약 보너스번호가 같고 c도 5면 2등 출력
    print(2)
elif c==6:
    print(1)
elif c==5:
    print(3)
elif c==4:
    print(4)
elif c==3:
    print(5)
else:
    print(0)
