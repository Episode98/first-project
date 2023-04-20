#30cm 자를 만들고 길이를 입력하면 그 위치를 화살표로 표시하는 프로그램 작성

rule = int(input("길이를 입력하세요 : "))
for i in range(rule):
   print('┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬')
   print("___________________________")



#음악 플레이어를 만들려고 한다. 현재 3분 50초 분량의 노래가 있다
#진행된 노래 분량을 입력 받아 그림으로 표시하고 몇% 진행했는지 수치로 나타내는 프로그램을 작성하시오
#(복습필요 그려볼것)
pp = ''
song = int(input("재생시간 입력 :"))
per = int(song/230*100)
for i in range(0,int(per/4)):
    pp += '■'
print(pp,per,'%')
    
# 서우님 코드
data = ''
time = int(input('재생시간 :'))
per = int(time/230 * 100)
for i in range(0,int(per/4)):
    data += '■'
print(data,per,"%")


# 다음과 같은 결과가 나올 수 있도록 프로그램을 작성하시오
#3 4 5 6 7
#4 5 6 7 8
#5 6 7 8 9
for i in range (3,7+1):
    print(i, end="")
print()
for i in range (4,8+1):
    print(i ,end="")
print()
for i in range (5,9+1):
    print(i,end="")

#두 수를 입력 받아 큰 수에서부터 작은 수까지 출력 되도록 프로그램을 작성하시오 (틀림,복습필요)
num1 = int(input("수를 입력하세요 : "))
num2 = int(input("수를 입력하세요 : "))
if num1 < num2:
   for i in range(num2,num1-1,-1):
    print(i,end="")
else:
  for i in range(num1,num2-1,-1):
    print(i,end="")

#수를 입력 받아 0부터 입력 받은 수까지 3의 배수를 출력되도록 프로그램을 작성 (틀림,복습필요)

n1 = int(input("수를 입력하세요 : "))
for i in range (0,n1):
      print(i)


#정답 서우님 코드
num1 = int(input('수를 입력하세요: '))
for i in range(1,num1+1):
    if i%3==0:
        print(i, end=' ')


#수를 입력받아 0을 제외한 7의 배수를 입력 받은 수 만큼 출력하시오 (틀림, 복습필요)
itu = int(input("수를 입력하세요"))
for i in range (1,itu+1):
    print(i)

# 정답 원채형 코드
input = int(input("input number:"))
for i in range(1, input+1):
        print(i * 7)


#수를 입력 받아 1부터 입력 받은 수 사이의 2의 배수와 3의 배수를 출력 (단. 2와3의 공배수는 출력 제외)
# tty = int(input("수를 입력하세요 : "))
# for i in range(1,tty+1):
#    if tty%2 ==0 and tty%3 ==0:
#       print(i, end="")
# for i in range(1,tty+1):
#    if 



# 서우님 코드
for i in range(1,4):
    for j in range(1,5):
        print(i*j, end=' ')
    print()



# #다음과 같이 나올 수 있도록 프로그램 작성 (복습필요)
a = "■■■■■"
b = "□□□□□"
ne = int(input("수를 입력하세요 :"))
for i in range(0,2):
    print(a)
    for p in range(1,ne):
        print(b)
print(a)


# 구구단 나오도록 작성
dan = int(input('단을 입력하세요 '))
print("=== %d단 ==="%dan)
for i in range(1,10):
    result = dan * i
    print(dan,"X",i,"=",result)

dan = int(input('단을 입력하세요 '))
print("=== %d단 ==="%dan)
for i in range(1,10):
    result = dan * i
    print(dan,"X",i,"=",result,end=' ')