# while(상황에 따른 반복) if 문과 다르게 한 싸이클 돈후 다시 입력값보러 돌아옴 (무한루프?..)

i = 0
while i < 5: # i가 5보다 작으면 
    print(i) # i를 실행
    i+=1     # i에 +1 해서 출력


minval = 100
i = 0
while i !=5:
    n = int(input("수 입력(100이하):"))
    if n> 100:
        print("입력 범위를 확인하세요.")
        i-=1
    if n < minval:
        minval = n
    i+=1
    print(i)
print(f"입력한 점수중 최소값:{minval}")


# 10이하의 정수를 입력하시오(10이상이면 다시 입력 받도록)
while True:
    a = int(input("정수를 입력하세요"))
    if a > 10:
        print("다시입력하세요 ")
    print(a)

while True:
    three = int(input("숫자 입력 : "))
    if str(three == "q"):
        break
    if three%3 == 0:
        print("3의배수입니다")
    else:
        print("다시 입력하세요")
        continue


#3의 배수를 판별하는 프로그램을 작성 (단Q가 입력되면 종료)
#제일먼저 q인지를 판별,아니면 정수로 변환해서 3의 배수를 판별
while True:
 th =  int(input("정수를 입력하세요:"))
 if th == "q":
    break
 if th%3 == 0:
   print("3의 배수 입니다")
 else:
   print("3의 배수가 아닙니다")





# 1자리 숫자를 계속 입력 받아 합과 입력된 개수를 구하시오
# ->1자리 숫자입력받으면 인식하고 10이 넘어갈때 중지시키는것까지 성공 (오답코드)
while True:
    plus = int(input("숫자를 입력하세요 : "))
    if plus < 10 :
        print(plus)
    elif plus > 10 :
         break
    print(plus)


#점심에 시도 (거의 성공****)
num1 = 0 # 횟수
num2 = 0 # 값+?
while True:
    plus = int(input("1,9사이 숫자 입력 : "))
    num1+=1
    num2+=plus #이따 출력 시킬때 plus값을 num에 넣는것이기때문에 출력 num2로?
    if plus < 10:
        print(num2)
    if plus > 10:
        print(num2)
        break
    print(f"시도한 횟수는{num1}이고 합계는{num2}이다")