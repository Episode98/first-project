# #몸무게를 파운드(lb)단위로 놓고 체급표에 맞게 프로그램 작성 (못풀었음 복습**) 1번자료 내가푼것

#1번자료
k1 = float(input("몸무게를 입력하세요 : "))
kg = 2.204623 * k1
if  125 >= kg:
     print("당신은 fly급이며 체중은",kg,"파운드 입니다")
elif 135 >= kg and kg> 125:
     print("당신은 bantam급이며 체중은",kg,"파운드 입니다")
elif 145 >= kg and kg> 135:
     print("당신은 feather급이며 체중은",kg,"파운드 입니다")
elif 155 >= kg and kg> 135:
     print("당신은 light급이며 체중은",kg,"파운드 입니다")
elif 170 >= kg and kg> 155:
     print("당신은 welter급이며 체중은",kg,"파운드 입니다")
elif 185 >= kg and kg> 170:
     print("당신은 middle급이며 체중은",kg,"파운드 입니다")
elif 205 >= kg and kg> 185:
     print("당신은 light heavy급이며 체중은",kg,"파운드 입니다")
elif 265 >= kg and kg> 205:
     print("당신은 heavy급이며 체중은",kg,"파운드 입니다")

#2번자료
kg = float(input('몸무게를 입력하세요. '))
lb = kg * 2.2046

if(lb <= 125): result = 'fly'
elif(125 < lb <= 135): result = 'bantam'
elif(135 < lb <= 145): result = 'feather'
elif(145 < lb <= 155): result = 'light'
elif(155 < lb <= 170): result = 'welter'
elif(170 < lb <= 205): result = 'middle'
elif(205 < lb <= 265): result = 'light heavy'
elif(265 < lb): result = 'heavy'

print("당신은",result,"급이며, 체중은",round(lb,4),"파운드입니다.")






# 주민번호 7자리를 입력 받아 나이와 성별을 구하시오 (못풀었음 복습**)
num = str(input('주민번호 7자리를 입력하세요. '))

if (int(num[0:2])>23):
    age = 123 - int(num[0:2]) + 1
else:
    age = 23 - int(num[0:2]) + 1
if(age>=20):
    adult = '성년'
elif(age<20):
    adult = '미성년'
if (num[6]=='2' or num[6]=='4'):
    gender = '여성'
elif(num[6]=='1' or num[6]=='3'):
    gender = '남성'
    
print("당신은",age,gender,"이며",adult,"입니다.")

for i in range(0,5):
      print("a")


lastnum = int(input('마지막 수 입력 : '))
for i in range(0, lastnum):
       print(i+1)


#연속된 문자가 출력되는 프로그램 작성
roop = str(input("입력: "))
for i in range(0,5):
     print(roop)

# 1부터 입력한 숫자까지의 합을 구하는 프로그램을 작성
plus = int(input("숫자를 입력하세요: "))
a=0
for i in range(0,plus+1):
      a+=i
print(a)

# #숫자를 입력받아 입력한 수부터 0까지 카운트 다운하는 프로그램 작성
count = int(input("숫자를 입력하세요: "))
for i in range(count, -1, -1):
      print(i)



# 10 이하의 정수를 5개 입력 받아 짝수이면 출력
for i in range(5):
      jj = int(input("숫자를 입력하세요 :"))
      if jj%2 == 0:
            print(jj)
    
# 수를 입력 받아 1부터 입력한 수 사이의 2의 배수를 출력
tt = int(input("입력 : "))
for i in range(1,tt+1):
            if i%2 == 0:
                    print(i)

# 수를 입력 받아 1부터 입력한 수 사이의 3의 배수를 출력
pp = int(input("숫자를 입력 : "))
for i in range(1,pp+1):
        if i%3 == 0:
                print(i)
# # 수를 입력 받아 1부터 입력한 수 사이의 2의 배수와 3의 배수를 출력
tp = int(input("숫자를 입력 : "))
for i in range(1,tp+1):
        if i%2 ==0:
                print(i)
        elif i%3 ==0:
                print(i)
# 수를 입력 받아 1부터 입력한 수 사이의 2와 4의 공배수를 출력
tf = int(input("숫자 입력 : "))
for i in range (1,tf):
        if i%2 ==0 and i%4 ==0:
                print(i)
# 5개의 점수를 입력 받아 최대값을 출력
scores = []

for i in range(5):
    score = int(input("점수를 입력 : "))
    scores.append(score)

max_score = max(scores)

print('최대값은 {}입니다.',format(max_score))

# 5개의 점수를 입력 받아 최소값을 출력
scores = []

for i in range(5):
    score = int(input("100이하의 점수를 입력 : "))
    while score > 100:
        print('100이상의 점수를 입력하였습니다!')
        score = int(input('100이하의 점수를 입력 : '))
    scores.append(score)

min_score = min(scores)

print('최소값은 {}입니다.'.format(min_score))
# 100이하의 점수 5개를 입력 받아 최대값과 최소값을 제외한 나머지 점수의 합계와 평균을 구하시오
scores = []
for i in range(5):
    score = int(input('점수를 입력 : '))
    scores.append(score)

min_score = min(scores)
max_score = max(scores)

sum_scores = sum(scores) - min_score - max_score

avg_score = sum_scores / 3