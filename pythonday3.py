#  if의 값이 ture면 실행 아니면 실행하지않고 넘긴다

val = 100
if val:
      print('true')
      print(val)

val2 = 0
if val2:
      print('False')
      print(val2)

 #  if 의 값이 False면 else의 값을 실행한다

# 숫자를 입력 받아 음수를 판별하시오 (숫자를 입력하세요 : -2 , 7)

n1 = int(input("숫자를 입력하세요 : "))

if (n1>0):
      print(n1,"을 입력하였습니다")
else:
      print("음수이며" ,n1,"을 입력하였습니다")


#   태어난 년도를 2자리 혹은 4자리로 입력 받아 우리나라 나이를 구하는 프로그램을 작성하시오.
age = int(input("태어난 년도를 4자리로 입력하시오 : "))
age2 = (2023-age)+1
print(age,"년에 태어난 당신은" ,age2,"살입니다")

#   2자리
age3 = int(input("태어난 년도를 입력하시오 : "))
age4 = (123-age3+1)
if (age3< 123):
    print(age3 ,"년에 태어난 당신은", age4, "살 입니다")



#  숫자를 입력 했을 때 절대값을 출력하는 프로그램 작성

n = int(input("숫자를 입력하세요 :"))

if n >= 0:
      print("절대값은" ,n)
elif n <= 0:
      print(n,"의 절대값은",-n)



#   총 게임을 만들려고 한다 총 별 사거리 존재하며 사거리에 따라 사격의 정확도를 게임에 넣으려고 한다
#   사거리를 연습 시키기위한 연습장을 제작 하는데 사용가능한 총은 권총 뿐이다 유효사거리는 50m이며
#   타겟의 거리를 계산하는 프로그램을 작성하시오.

shot = int(input("사용자의 거리를 입력하세요:"))

if  shot > 50:
      print("최대유효사거리보다",shot-50,"멉니다.")
elif shot < 50:
      print("최대유효사거리보다", 50-shot,"가깝습니다.")
elif shot == 50:
      print("최대 유효사거리와 정확히 일치합니다.")


#   엘리베이터 알고리즘을 구현하려고 한다 현재 건물에는 2대의 엘리베이터가 있고
#   A엘리베이터는 5층에 B 엘리베이터는 7층에 있다. 현재 내가 있는 층수를 눌러 가장 가까운
#   엘리베이터를 움직일 수 있도록 프로그램 작성

el = int(input("현재 층수를 눌러주세요 : "))

if 5 > el > 0:
      print("5층 엘리베이터가 내려옵니다")
elif el == 5:
      print("현재 5층입니다")
elif el == 7:
      print("현재 7층입니다")
elif 7 < el:
      print("7층 엘리베이터가 올라옵니다")
elif el == 6:
      print("5,7층 엘리베이터중 먼저 도착하는 엘리베이터에 탑승하세요")





#  비만도를 측정하는 프로그램 작성 (표준체중 kg = 현재신장 (cm -100)*0.9)
#                               (비만도 % = (현재체중 / 표준체중)*100)

he = float(input("신장을 입력하세요 : "))
we = int(input("체중을 입력하세요 "))
kg = ((he - 100)*0.9)
B = ((we / kg)*100)

if B <80:
      print("저체중 입니다")
elif 90 > B >= 80:
      print("경한 저체중입니다")
elif 110 > B >= 90:
      print("정상 체중입니다")
elif 120 > B >= 110:
      print("과체중 입니다")
elif 130 > B >= 120:
      print("경도 비만입니다")
elif 150 > B >= 130:
      print("중증도 비만입니다")
elif 200 > B >= 150:
      print("고도비만 입니다")
elif 200 < B:
      print("비만이 위험수치입니다!")



#  5개의 실수를 입력 받아 최소값과 최대값을 제외한 나머지 점수들의 합계와 평균을 구하시오

a = float(input("점수를 입력하세요 : "))
b = float(input("점수를 입력하세요 : "))
c = float(input("점수를 입력하세요 : "))
d = float(input("점수를 입력하세요 : "))
e = float(input("점수를 입력하세요 : "))

t1 = (b,c,d,e)
t2 = (a,c,d,e)
t3 = (a,b,d,e)
t4 = (a,b,c,e)
t5 = (a,b,c,d)

if a < t1:
      print ("합계는",b+c+d+e,"이며 평균은",(b+c+d+e)/4,"점 입니다")
elif b < t2:
      print("합계는",a+c+d+e,"이며 평균은",(a+c+d+e)/4,"점 입니다")
elif c < t3:
      print("합계는",a+b+d+e,"이며 평균은",(a+b+d+e)/4,"점 입니다")
elif d < t4:
      print("합계는",a+b+c+e,"이며 평균은",(a+b+c+e)/4,"점 입니다")
elif e < t5:
     print("합계는",a+b+c+d,"이며 평균은",(a+b+c+d)/4,"점 입니다")


a = float(input('점수를 입력하세요: '))
b = float(input('점수를 입력하세요: '))
c = float(input('점수를 입력하세요: '))
d = float(input('점수를 입력하세요: '))
e = float(input('점수를 입력하세요: '))

list = [a,b,c,d,e]

sum = (a+b+c+d+e) - (max(list) + min(list))
avg = sum/3

print("합계 : %.1f 평균 : %.1f" % (sum, avg))