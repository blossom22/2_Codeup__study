# Codeup_구조체연습_4751: 아시아 정보올림피아드

from collections import defaultdict
n = int(input())
nation = defaultdict(int)
cnt = 0     # 메달을 딴 인원수 카운트
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key=lambda v:(-v[2]))     # 점수를 기준으로 내림차순한다
for i in range(n):
    if cnt!=3:
        if nation[data[0][0]]<2:
            nation[data[0][0]] += 1
            print(data[0][0], data[0][1])
            cnt+=1
            del(data[0])
        else:
            del(data[0])
    else:
        break