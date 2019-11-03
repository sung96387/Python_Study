'''
출력 하는 함수 : print()

* 표준 입출력 Standard input/output
    stdin, stdout --> stdio
   IDLE나 콘솔(cmd.exe)에서 입/출력 하는 방식

   [입력 함수 iuput()]
       1. input() --> 입력대기 상태 --> 입력 후 엔터!
          >> 입력된 값이 '문자열'로 '반환'된다.
       2. input("입력 받기 전 출력할 문자열")
          [A]
          print("입력 : ")
          input()
          [B]
          input("입력 : ")


'''
print("="*20)
print("{:^20}".format("input"))
print("="*20)

# input() # 입력 대기 상태
# print("입력완료")
'''
 input()은 입력 대기 상태가 되기 때문에
 계속 주석처리하면서 공부합니다.
'''

# input() : ()안의 문자열이 출력된다.
# input("입력해보세요 : ")

# 입력된 내용이 '반환' 되어 print함수로 출력했다.
# print( input("입력 : "))

# 반환 값은 '문자열'
# print( input("숫자 입력 :") +10) # 오류 -> 형변환 하면 가능 ==> int(input("숫자 입력:"))

# 변수에 저장하여 사용
# my_str = input("입력 : ")
# input("입력 : ") 이 코드가 "123" 으로 대체됐다.
# print("입력할 문자열 : ",my_str)
# print("타입은?? :", type(my_str))

# 숫자로 형변환 
# num1 = int(input("첫 번째 숫자 입력 : "))
# num2 = int(input("두 번째 숫자 입력 : "))
# print("두 수의 합 = {}".format((num1+num2)))

# 형변환 : 원하는 자료형의 타입으로 '대상'을 묶는다.
# list(), tuple(), int(), str(), float() ...

# int()
print( "int(1.1) :", int(1.1)) # 소수 -> 정수
print( "int('11') :",int('11')) # 문자열 - > 정수
# print( "int('1.1') :",int('1.1')) # 문자열 - > 정수
# 문자열에는 숫자만 있어야 한다.(오류)

# 변수에 대입 후 사용
'''
num = input("제곱할 숫자 입력 : ") # 현재 문자열
num = int(num)
# 문자열 '3'을 가리키던 num이 숫자 3 을 가리키게 됐다.
print(num*num)
'''

# 여러 개의 값 입력 받기 (1)
# 문자열 함수 split()을 활용하기

'''
# split()복습
my_str = "하.하.하"
print(my_str.split(".")) # 리스트 형태로 변환
my_str = "하 하 하"
print(my_str.split()) # 괄호 안에 문자 입력 x -> 공백

# 받은 변수의 개수와 '입력한 값의 개수'가 같아야 한다.
#                     -> split( )나눌 문자열의 수
num1, num2, num3 = input("숫자 3개 입력 : ").split()
# 여러 개의 값을 입력 받긴 했지만 나눈 값들이 '문자열'
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
print("입력한 숫자들의 합 : ",(num1+num2+num3))
# 1. input()으로 문자열 3개 받음 -> "1 2 3"
# 2. "1 2 3".split() 으로 리스트로 변환
#     ['1', '2', '3']
# 3. 3개의 변수에 리스트의 각 요소를 순서대로 대입
# 4. 각 변수(문자렬)를 정수로 변환
print("입력완료")
'''

print()
'''
# 여러 개의 값 입력 받기 (2)
# map() 함수 활용하기 -> 편하다.
# map(함수명, 반복)
a, b = map(int,['1', '2'])
# a, b = int('1'), int('2')
# a,b = 1, 2
print(a+b)

# num1, num2 = map(int, input("~~~").split() )
num1, num2 = map(int, input("두 수 입력 : ").split())
#                      -> 리스트 형태
print(num1 + num2)

# 1. input()으로 문자열 입력 받음"109 1"
# 2. "109 1".split()으로 리스트로 변환
#   ['109' , '1']
# 3. map() 함수를 활용하여 int('109'), int('1')
# 4. num1, num2 = 109, 1
'''

# 문자열 입력 연습 : 출력시 .format()사용
'''
    1. 사각형 면적 구하기
        가로, 세로를 입력 받고 면적 계산
        면적 = 가로 X 세로
    [출력결과]
    가로, 세로 : 2 5
    면적은 10 입니다.

    2. 사칙연산 프로그램
        두 수를 입력 받고 사칙연산!
        단, 나눗셈 결과가 소수이면 둘째 자리까지 출력

    [출력결과]
    두 수 입력 : 11 3
    11 + 3 = 14
    11 * 3 = 33
    ...
    11 / 3 = 3.67

    3. 주차요금 계산기
       최초 60분 : 1000원
       이후 1분마다 100원씩 증가
    [출력결과]
    주차 시간 입력(최소 60분) : 75
    주차 요금은 2500원입니다.
'''

num1, num2 = map(int, input("가로, 세로  : ").split())
print("면적은 {}입니다.".format((num1*num2)))

num1, num2 = map(int, input("두 수 입력 :").split())
print("{} + {} = {}".format(num1,num2,num1+num2))
print("{} * {} = {}".format(num1,num2,num1*num2))
print("{} - {} = {}".format(num1,num2,num1-num2))
print("{} / {} = {:.2f}".format(num1,num2,num1/num2))
# .format 사용시 소수점 나타내기 기억!

time1 = int(input("주차 시간 입력(최소 60분) :"))
time2 = time1 - 60
print("주차 요금은 {}원입니다.".format(1000+time2*100))

















