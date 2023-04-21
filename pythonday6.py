# 구구단을 다음과 같이 출력되도록 프로그램을 작성하시오(중첩for활용)

dan = int(input('단을 입력하세요 '))
print("=== %d단 ==="%dan)
for i in range(1,10):
    result = dan * i
    if(i==6):
        print()
    print(dan,"X",i,"=",result,end=' ')

for i in range(1,10):
    print()
    for j in range(1,10):
        print(f"{j}x{i}={j*i}", end=" ")

a = 2
for i in range(0,2):
    print(a)


# 종속이 안됐을때에 값
for i in range(1,10):
    print(i)
for k in range(2,5):
    print(k)

# 예제
for i in range(1,6):
    for j in range(1,6):
        print(i,end='')
    print()

# 별 한줄 (가로)
q = "*"
for i in range(0,5):
    print(q,end="")

# 별 한줄 (세로)
q = "*"
for i in range(0,5):
    print(q)

# 별 다섯줄 (세로)
q = "*****"
for i in range(0,5):
    print(q)

# 12345 다섯줄 (세로)
q = 12345
for i in range(0,5):
    print(q)


# Q4 동일한 숫자 가로줄 세로줄
for i in range(1,6):
    for j in range(1,6):
        print(i, end="")
    print()    #이 공백이 줄바꿈을 해줌

# Q5 12345 다섯줄
q = 12345
for i in range(0,5):
    print(q)

# Q6 12345 줄바꿈23456 으로 56789까지 만들기

for i in range(1,6):
    for j in range(1,6):
        print(i,end='')
        i += 1
    print()

# Q7 역순으로 56789 ,45678 진행 (왜 range값에 0을 넣어야 작동하는지도 질문)
for i in range(5,0,-1):
      for j in range(1,6):
            print(i,end="")
            i+=1
      print()

# Q8 한개씩 늘려가기 * ** *** ****
q = "*"
for i in range(0,5):
        print(q*i)

# Q9 한개씩 줄여가기 ***** ****

q = "*"
for i in range(5,0,-1):
    print(q*i)

for i in range(2,10):        # 1번 for문
    for j in range(1, 10):   # 2번 for문
        print(i*j,end=" ")
    print(" ")