# Codeup_Python 기초3.단순 반복문_1274: 소수 판별

n=int(input("자연수를 입력하세요: "))
a=[i for i in range(2,n+1) if n%i==0]
if len(a)==1:
    print('prime')
else:
    print('not prime')


# 위의 코드를 더 간결하게 만들어보았다. 수의 특성을 이용해서 불필요한 연산을 줄였다. 
n = int(input("자연수를 입력하세요: "))
a = n >= 2                              # a의 초기값으로 n>=2로 설정해서 n이 2이상이면 소수로 가정한다. 
for i in range(2, int(n**0.5) + 1):     # 2부터 n의 제곱근까지 약수를 찾는다. 제곱근까지만 범위로 설정하는 이유는 둘 중 한쪽은 반드시 n의 제곱근보다는 작거나 같기 때문이다. 그러니 제곱근이하의 수 중에서 약수가 존재하면 어차피 소수가 아닐테니, 중복되는 약수들이 있을 제곱근이후 숫자는 볼 필요도 없다. (불필요한 연산 줄일수있다)
    if n % i == 0:                      # 약수가 있으면, 소수가 아니므로 a를 False로 만든다. 
        a = False
        break
print('prime' if a else 'not prime')