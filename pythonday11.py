#  리스트 컴프리헨션을 사용하여 1부터 100사이의 홀수 숫자 리스트 생성
odd_numbers = [num for num in range(1, 100) if num % 2 == 1]
print("Odd numbers:" ,odd_numbers)
print(type(odd_numbers))

# 집합 컴프리헨션을 사용하여 1~10까지의 제곱수 집합(set) 생성
squares = {num**2 for num in range(1,11)}
print("Squares: ", squares)
print(type(squares))

# 딕셔너리 컴프리헨션을 사용하여 15~25사이의 숫자와 제곱수 쌍의 딕셔너리 생성
number_square_pairs = {num: num**2 for num in range(15,26)}
print("Number-Square pairs:", number_square_pairs)
print(type(number_square_pairs))

# 리스트 [1,2,3,2,4,2,5]에서 index{}함수를 활용하여 값2의 모든 인덱스를 리스트로 생성
list=[1,2,3,2,4,2,5]
indices= [num for num in range(len(list)) if list[num]==2]
print(indices) 


txt = input('저장할 파일명')
name = input('이름:')
age = input('나이:')

file=open(f'{txt}.txt','w')
data = f'이름:{name}\n나이:{age}' 
file.write(data)
print('저장되었습니다.')
file.close()


rtxt= input('불러올 파일명:')
file=open(f'{rtxt}.txt','r')
rdata = file.read()
print(rdata)
print('모두 읽었습니다')
file.close()