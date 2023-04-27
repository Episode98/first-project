# 숫자를 입력 받아 음수를 판별하는 함수 정의
def cor():
    cot = int(input("숫자를 입력하세요 : "))
    if 0 > cot:
        print("음수입니다")
    else:
        print("양수입니다")
cor()




# 태어난 년도를 2자리로 입력하여 나이를 구하는 함수 정의
def age(value):
    if (value>23):
        ret = 123-value +1
    else:
        ret = 23-value +1
    return ret
value=int(input("태어난 년도  입력: "))
print(age(value),'살')


# 태어난 년도를 2자리 혹은 4자리로 입력 받아 우리나라 나이를 반환하는 함수 정의
def age():
 year = int(input("숫자를 입력하세요 : "))
 if year > 1000:
    tt = 2024-year
 elif year < 100:
    tt = 124-year
 print(tt)
age()


# 숫자를 입력받아 절대값을 반환하는 함수 정의

def power():
    num = int(input("숫자를 입력하세요 : "))
    if num < 0:
        ret = num*-1
    elif num > 0:
        ret = num
    print(ret)

power()


# 1부터 입력한 수 까지의 합을 반환하는 함수 정의
def plus():
    num = int(input("숫자를 입력하세요 : "))
    if num > 0:
        sum = 0    
    for i in range(1, num+1):
        sum += i
    return sum
print(sum)

plus()



# 표준체중을 구하는 공식
def average():
    he = float(input("신장을 입력하세요 : "))
    we = int(input("체중을 입력하세요 : "))
    if True:
        ar_kg = (he-100)*0.9
    print("표준체중은",int(ar_kg),"kg 입니다")
    if True:
        factor = we/ar_kg*100
    print("비만도는",int(factor),"%입니다")

average()



