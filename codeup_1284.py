# Codeup_Python 기초3.단순 반복문_1284: 암호 해독

def p(num):      # 소수판별하는 함수
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):     # num의 제곱근까지만 검사해서 소수인지 판단한다.  
        if num % i == 0:
            return False                        # 소수가 아니라면 False, 소수라면 True
    return True

def fp(num):                                    # num이 두 소수의 곱으로 표현되는 경우를 찾는 함수이다. 
    factors = []
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and p(i) and p(num // i):   # num의 약수이면서, 곱해지는 두 수도 각각 소수인지 확인하는 과정이다. 
            factors.append((i, num // i))           # 곱해지는 두 수도 모두 소수라면 빈리스트에 추가한다. 
            return factors
    return None                                     # for문 다 돌고도 두 소수의 곱을 찾지 못한 경우, None이 되어서(아무 값도 반환X) 나중에 wrong number 출력한다

n = int(input("정수를 입력하세요: "))

prime_factors = fp(n)

if prime_factors:
    first_prime, second_prime = prime_factors[0]    # 가능한 소수 중 가장 작은 소수와의 곱을 찾기 때문에 이 과정이 필요하다. 
    if first_prime <= second_prime:                 # 두 소수가 오름차순으로 정렬되는 과정이다. 
        print(f"{first_prime} {second_prime}")
    else:
        print(f"{second_prime} {first_prime}")
else:
    print("wrong number")