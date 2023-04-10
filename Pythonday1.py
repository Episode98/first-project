#파이썬 영어철자를 입력했을 때 맞으면 True 틀리면 False가 나오도록 프로그램 작성
a = str(input("파이썬 영어철자를 입력하세요: "))
print(a == "python")


# 두 수를 입력 받아 
# 첫 번째 수가 두 번째 수의 배수이면 Ture 아니면 False를 출력하는 프로그램 작성
n1 =int(input("첫 번째 수 입력: "))
n2 =int(input("두 번째 수 입력: "))
print(n1%n2==0)


# 하나의 수를 입력받아 12의 약수이면 True 거짓이면 False를 출력하는 프로그램 작성
w = int(input("수 입력: "))
print(12%w ==0)


w1 = int(input("첫 번째 수 입력: "))
w2 = int(input("두 번째 수 입력: "))
print(w1**2 == w2)



# 두 조건이 모두 참 일때 앞의 결과가 True면 뒤도 True , False면 뒤도 False로 판단하는방식을
# short-circuit 평가 라고 한다
print('0 and 1 =', 0 and 1, bool(0 and 1))
print('2 or 3 =', 2 or 3, bool(2 or 3))
print('2 and 4 =', 2 and 4, bool (2 and 4))
print('0 or 3 = ', 0 or 3, bool(0 or 3))


print(bool(-1))
print(bool("hello"))
print('hi' or '\0')
print(0 or 'hello')
print('hello' and 'hi')