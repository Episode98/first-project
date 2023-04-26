# 쌀 100통이 저장되어 있는 창고에 암수1쌍의 쥐가 있다 쥐 한마리가 하루에 20g의 쌀을 먹고 10일마다 쥐의수가
# 2배씩 증가한다 며칠만에 창고의 쌀이 모두 쥐의 먹이가 될까 그리고 쥐는 총 몇마리인가? (한통은80KG이다)

# rice = 80 * 100 * 100 # 총 쌀의 양 g
# mo = 2 # 시작쥐
# day_count = 0 # 날짜 값

# while rice > 0:
#     day_count+=1  #매일 지나는 날짜
#     rice = mo_eat-= rice/1000
#     mo_eat = day_count*20 # 하루에 먹는양
#     if rice%10 == 0:  #10일지날때마다 늘어나는 쥐
#         mo*2
    
#     print("총날짜는{rice}, 쥐는 총 {mo}")

# 건일이 코드
rice_kg = 100 * 80 * 100  # 총 쌀의양
mouse_count = 2           # 쥐 마리수
day_count = 0             # 카운팅 날짜

while rice_kg > 0:        # 총 쌀의양이 0보다 클때 코드를 반복할건데
    rice_eat = mouse_count * 20 # 쥐가 하루에 먹는 양 2 * 20
    rice_kg -= rice_eat / 1000 # 쌀을 쥐가 먹는데 걸리는 날짜 (????)
    day_count += 1             # 날짜값 매일 카운트
    if day_count % 10 == 0:    
        mouse_count *=2        # # 10일이 지났을때 쥐가 2배로 증가

print(f'{day_count}일만에 쥐의 먹이가 되었고, 쥐는 총 {mouse_count}마리 입니다.')


rice = 8000000
day = 1
mouse = 2

while True:  # 값이 있으면 출력
    if (day % 10 == 0): # 10일마다 쥐가 2배로증가
        mouse *= 2
    day += 1            # 매일 올라가는 날짜 1,2,3,4,5
    rice -= mouse * 20  # 총 쌀의양에 쥐가 먹는양을 뺀다
    if rice <= 0:       # 쌀이 0보다 작아졌을때 출력
        print(day,'일', mouse,'마리')
        break


mil = 1   # 첫 밀알개수
n = 1
while mil < 64:
    n+=1
    mil*=2
    print(mil,"개")



# 전설에 따르면 체스 발명자는 왕으로 부터 받을 상을 말하도록 요구 받았을 때 발명자가 말하길 체스판의
# 첫번 째 사각형에는 밀알을 1개, 두번째 사각형에는 2개 세번째 사각형에는 밀알을 4개 등으로 총 64칸에 밀알을 2배씩
# 채워주기를 요구 했다, 이 발명가가 요구한 밀알의 개수는?
n = 1
mil = 1
while n <= 64:
    n += 1
    mil *= 2 
print(mil,'개')


# 수를 입력 받아 1부터 입력 받은 값 까지의 합(1)을 구하고
# 수를 입력 받아 1부터 입력 받은 값 까지의 합(2)를 구하여
# (1)과 (2)의 합(3)을 구하고 1부터(3)까지의 합을 구하시오

a = (int(input("입력:")))
b = (int(input("입력:")))
print(f"a : {a}")
print(f"b : {b}")
c = a+b
d = (c)

print(f"1부터 {c}까지의 합: {d}")