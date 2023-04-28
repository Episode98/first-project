#임의의 개수로 실수를 입력받아 최소값과 최대값을 제외한 나머지
#점수들의 합계를 반환하는 함수 정의(가변인자 활용)
a = []
for i in range(int(input("임의의 개수 입력:"))):
    a.append(float(input("실수 입력:")))

def f(*a):
    result = 0
    for i in range(len(a)):
        result += a[i]
    result -= (min(a)+max(a))
    return result
print(f(*a))

#합계에 해당하는 값과 개수를 입력 받아 평균을 반환하는 함수 정의

a = []
for i in range(int(input("임의의 개수 입력:"))):
    a.append(int(input("아무숫자 입력:")))
    
def avg(*a):
    result = 0
    for i in range(len(a)):
        result += a[i]
    result //= len(a)
    return result
print(avg(*a))

#cm값을 inch값으로 변환하는 함수 (1 Inch == 2.54cm) 정의

def inch():
    a =int(input("cm를 인치로 바꿔드려요:"))
    inch = a* 0.39
    return round(inch,2)
print(inch())

# 파일의 용량을 매개변수로 입력 받아 bit 단위로 반환하는 함수 정의
a = int(input("숫자 입력:"))
b = input("g,m,k를 비트로 바꿔줘요:")

def byte(a,b):
    if b == "g":
        a = a*125000
    elif b == "m":
        a = a*125
    elif b == "k":
        a = a*8
    return f"{a}비트입니다"
print(byte(a,b))

#인자로 N을 전달하면 N에 대한 팩토리얼을 반환하는 함수 정의
def fac(a):
    result = 1
    for i in range(a):
        result = result*(i+1)
    return result
a = int(input("팩토리얼 변환:"))
print(fac(a))


#인자로 N을 전달하면 거꾸로 만든수를 반환하는 함수 정의
a = input()
def rev(a):
    a = a[::-1]
    return a
print(rev(a))


# 재귀함수
value = 0
def recu():
    global value ## global 변수명 -> 바깥의 변수를 가져다가 사용하겠다
    print('\t'*value, end="")
    print(f'[value:{value}] 재귀!')
    if value == 3:
        print('\t'*value, value, 'Function End!')
        return
    value += 1
    recu()
    value -= 1
    print('\t'*value, value, 'Functionimage.png End!')

recu()