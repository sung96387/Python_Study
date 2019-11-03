# 08_function.py
'''
C언어 - 함수
파이썬 - 함수
JAVA - 메서드 (method)

    [함수] function , 기능     print() input() int()
       특정 작업을 수행하는 문장들을 하나로 묶은 것

       - 함수를 사용하는 이유
         1. 높은 재사용성
             > 한 번 만들어 놓으면 언제든 호출 가능
         2. 중복된 코드 제거
         3. 코드의 구조화
             > 작업 단위로 나누어서 구조의 단순화

[함수의 기본 구조]
def 함수이름(매개변수) :   <-- 이후 부터 수행문
    수행문 (함수의 기능 수행)
    수행문
    return 반환 값

def : define 정의하겠다.
함수이름 : 변수명 같은 개념. 어떤 기능을 수행하는지 명시
          어떠한 기능을 수행하기 때문에 '동사'가 많이 들어감
          
매개변수 : 함수가 기능 수행에 있어 필요한 값을 받음
          (개수 제한이 없다.)
          print()  <-- 매개변수 값 전달 안 함 = 개행만
          print(12) <- 매개변수로 정수 전달 => 정수출력
          print("abc") <- 문자열 전달 -> 문자열 출력
          
반환 값 : 함수 기능이 끝나고 마지막에 함수를 호출한 곳으로
          반환해주고 싶은 값
          my_str = input("입력하세요 : ")    >> 안녕하세요 라고 입력
                    return "안녕하세요"
          my_str은 "안녕하세요" 를 가리킨다.
          print( input("") )  --> IDLE에 안녕하세요 출력

          결국, input("입력하세요 : ") 는 return "안녕하세요" 에 의해
          "안녕하세요" 로 치환된거나 다름 없다.
          my_str = "안녕하세요"
          print("안녕하세요")
        
    매개변수 = 입력 값 (함수를 사용하는 쪽에서 입력할 값)
    반환 값 = 결과 값 (함수를 사용하는 쪽에서 받을 값)

    1. 입력값, 결과값 둘 다 있다.
    2. 둘 다 없다.
    3. 둘 중 하나만 있다. (2가지 경우)
    총 4가지 형태로 만들 수 있다. (필요, 목적에 따라 만들기 나름)

    * 반환 값은 보통 '기능 수행의 결과 값' 이나 '기능 수행의 성공/실패 여부'
'''
print("="*20)
print("{:^20}".format("function"))  # fn , func
print("="*20)

# 1. 입력 값, 결과 값 둘 다 있다.
# 이 함수의 기능 : 매개변수로 받은 2개의 값을 더한 결과 반환
def add( a, b ) :  # 믹서기 같은 존재
    return a+b

# 위에서 함수를 정의(def) 해놨기 때문에!
# 그 아래부터는 우리가 만든 함수 (사용자 정의 함수)를
# 자유롭게 사용할 수 있다.
print( add(1,5) ) # print( 1+5 ) # print( 6 )
print( add(100, 200) )
# 2. 입력 값, 결과 값 둘 다 없다.  ->  print()
def say_ho() :
    print("Ho~~~")  # 함수 안에서 함수 사용!

say_ho()

# 3. 입력 값, 결과 값 둘 중 하나만 있다
def say( talk ) : # 확성기 같은 존재
    print( talk )

say("Ho! Ho!")
say("안녕")
# 함수는 사용 후 원래 위치로 다시 돌아온다.

def get_ho() :
    return "Ho~~Ho!!"
ho = get_ho()
print( ho )
print( get_ho() )
# 반환이 있는 함수는 변수에 대입, 다른 곳에 바로 사용
print()

# 함수에서 여러 개의 값 반환 -> 거짓말! 튜플로 반환
# 모든 언어에서는 반환 값은 오로지 1개 (또는 없거나)
a = 1, 2, 3
print( type(a) )
def calc( a, b ) :
    return a+b, a-b, a*b, a/b
    # return (a+b, a-b, a*b, a/b)

print( calc( 2, 1 ) )
a, b, c, d = calc(3, 2)
print(a)
print()

# 리스트 언패킹 (unpacking) : 포장을 푼다 (패키지푼다)
def print_numbers(a, b, c) :
    print( a, b, c )

print_numbers(1,2,3)
my_list = [4, 5, 6]
#print_numbers( my_list ) #오류!
# my_list 는 리스트자료형으로써 a에만 대입이 된다.
# b,c는 값을 받지 못했기 때문에 오류가 발생
print_numbers( *my_list ) # *을 붙이면서 4,5,6과 같이 된다.

# 가변인수 : 매개변수가 몇 개가 될 지 모를때...! 사용
#   예를들면 print() 우리가 , 나열하는게 다 매개변수
#   print(1,2,3)

# 함수에 ex가 붙으면 extend : 확장 -> 기능이 확장된 함수
def add_ex( *args ) : # arguments : 입력 인자들
    # 언패킹 (리스트 -> 값의 나열)
    #  [4, 5, 6]   --> 리스트 (자료형)
    #  *[4, 5, 6]  --> 4 5 6 (단순한 나열)

    # 패킹 (값의 나열 -> 튜플)
    #  1, 2, 3, 4, 5 를 *args 받았다. (단순한 나열)    
    #  args        --> (1, 2, 3, 4, 5) 튜플 (자료형)
    
    print("args = ", args)
    print("*args = ", *args)
    add_sum = 0

    for i in args :
        add_sum += i

    return add_sum

print( add_ex( 1,2,3,4,5 ) )
print( add_ex( 1,2,3,4,5,6,7,8,9,10 ) )

# args와 일반 매개변수 혼용
# opt에 들어온 수의 배수를 더한다
# 고정된 일반매개변수를 먼저 지정해야 한다!
# 가변인수는 마지막에 사용
def calc_choice( opt, *args ) :
    result = 0

    for i in args : # 튜플!
        result += (i*opt) # opt가 2라면, 2배수를 더함

    return result
print( calc_choice( 1,1,2,3 ) )
print( calc_choice( 2,1,2,3,4,5,6 ) )

my_list = [1,2,3]
print( my_list )  # [1, 2, 3]
print( *my_list ) # 1 2 3
#           *args = 1,2,3,4,5
#            args = (1,2,3,4,5)  -> for i in args :
print()

# 키워드 인수 : 함수의 매개변수명을 키워드로 사용
#  ex)    "{name}은 학생입니다.".format(name="한수창")

def print_info( name, age, phone ) :
    print("이름 :", name)
    print("나이 :", age)
    print("전화 :", phone)

print_info( "한수창", 20, "010-1234-1234" )

# 순서 상관 없다. (.format에서도 순서 상관 없었다)
# 매개변수명을 알아야 사용이 가능하다.
print_info(age=20, phone="010-1122-2233", name="홍길동")
print()

# print_info("한수창", 20) # 오류!

# 매개변수에 초기값 지정
def print_info( name, age, phone="010-xxxx-xxxx" ) :
    print("이름 :", name)
    print("나이 :", age)
    print("전화 :", phone)

print_info("한수창", 20) # phone에 기본값이 있어서 가능
print_info("한수창", 20, "010-1234-1111")

# 매개변수 초기값 순서..!
# 매개변수에 초기값을 지정하면 맨 뒤로가야 한다. (문법오류)
# default 값이 있는 매개변수는 뒤로 몰자!
'''
def print_info( name, age=20, phone ) :
    print("이름 :", name)
    print("나이 :", age)
    print("전화 :", phone)
    
print_info("한수창", "010-1234-1111")
'''

# 재귀함수 : 함수가 자기 자신을 다시 호출하는 형태
#  잘못 사용하면 한도끝도없이 나 자신만을 호출! -> 런타임오류
#                           런타임오류 : 실행도중 오류
# StackOverflow : 스택이라는 메모리 공간이 넘친 오류
#  함수 사용 시 스택 메모리 공간을 사용한다.

def count_down(count) :
    # num = count
    # print("함수시작->입력값 :", num)
    
    if count == 0 :
        return
    
    print("카운트다운 :", count)

    count -= 1 # if문 조건에 만족하기 위한 감소
               # 반복문에서의 '조건변수' 역할
    count_down(count) # 나 자신 함수를 다시 호출!
    #print("함수끝->입력값 :", num)

count_down(5)

print()
print()

a = 5 # <-- 얘가 전역변수

# 지역변수, 전역변수
# 전역변수 : 전체 영역에서 사용가능한 변수 (우리가 사용하던)
# 지역변수 : 특정 지역에서만 사용가능한 변수 (수행문 안)

value = "전역변수"

def func1() :
    print(value) # 전역변수는 어디서든 접근 가능

def func2() :
    #print(value) # 오류! 아래서 같은 이름으로 지역변수만듦
    # 특정지역에서 전역변수를 다시 만들었으면,
    # 그 지역에서는 원래 있던 전역변수는 사용할 수 없다.
    
    value = "func2의 지역변수"
    valueFunc2 = "func2의 지역변수"
    #print(valueFunc2) # 제대로 찍힌다! (정상)
    print(value)

def func3() :
    global valueFunc3 # 지역변수를 전역변수로 만들기!
    valueFunc3 = "func3에서 global로 만든 전역변수"

func1()
func2()
# print(valueFunc2) # 이 변수는 func2 에서만 유효한 변수
func3() # global도 함수가 호출되어야 효력이 발생!
print("밖에서 찍어본 value :", value)
print(valueFunc3)




# 함수 연습문제
'''
    1. 홀짝 판별기
        홀수/짝수 판별하는 함수 정의
    [출력결과]
    숫자 입력 : 20
    짝수입니다.
'''
# (1) 홀수/짝수 판별 후 출력하고 값이 없는 함수
# (2) 홀수/짝수 판별결과를 반환하는 함수 (함수를) 호출한 쪽에서 결과 출력
'''
def numfunc1() :
    num = int(input("숫자 입력 :"))
    if num % 2 == 0 :
        print("짝수입니다.")
    else :
        print("홀수입니다.")

numfunc1()

def numfunc2() :
    num = int(input("숫자 입력 :"))
    if num % 2 == 0 :
        return "짝수입니다."
    else :
        return "홀수입니다."

print(numfunc2())
'''
'''
    2. 두 수를 입력 받고, 큰 수에서 작은 수를 뺀
       결과를 반환하는 함수 정의
    [출력결과]
    숫자 입력 : 5 30
    결과 : 25
'''
'''
def numfunc3() :
    a , b = map(int,input("숫자 입력 :").split())
    if a < b :
        return b - a
    else :
        return a - b
    

print(numfunc3())
'''
'''
    3. 1~10 사이의 두 수를 입력 받고.
       그 두 수의 1~100까지 공배수를 출력하는 함수 정의
       (반환 X, 함수에서 직접 출력)
    [출력결과]
    두 수 입력 : 3 5
    결과 : 15 30 45 60 75 90
'''
'''
def numfunc4() :
    a , b = map(int,input("숫자 입력 :").split())
    for i in range(1,101) :
        if i % a ==0 and i % b==0 :
            print(i,end =" ")
        else :
            continue
numfunc4()
print()
'''
'''
    4. 소수 출력하기
        1~입력받은 수까지 소수(PrimeNumber)만 출력하기
            - 소수 : 1과 자기 자신으로만 나누어떨어지는 수
            - 1은 소수가 아님

        함수 : 숫자를 1개 전달 받아서 소수인지 판별 후
               소수이면 True, 아니면 False 반환하기
               이름 : IsPrimeNumber
                       IsPrimeNumber(10) --> Fasle
                       IsPrimeNumber(11) --> True
    [출력결과]
    숫자 입력 : 20
    소수 : 2 3 5 7 11 13 17 19
'''
'''
def IsPrimeNumber(num) :
    # num 이 10이라면, 1~10까지 하나씩 나누어보고 나머지가 0인 개수가 2개면 소수
    # 2~9까지 나누어서 나머지가 0인 개수 0이면 소수
    for i in range(2, num) : # num-1  (2~9)
        if num % i == 0 : # 전달된 숫자를 2~9까지 일일이 나누어본다.
            # 나누어떨어졌다 = 소수가 아니다
            return False

    # 여기까지 진행됐다는 것은, 위에 for문에서 return 되지 않았다 == 소수이다.
    return True

num = int(input("숫자 입력 : "))
for i in range( 2, num+1 ) :
    if IsPrimeNumber(i) == True : # 대충 이런식으로!! 하나씩 검사
        print("{} ".format(i), end="")
'''
'''
num = input("숫자 입력 : ")
    5. 팩토리얼 구하기
        재귀함수를 이용하여 입력받은 수의 팩토리얼 구하기
            팩토리얼 :  5! = 5 * 4 * 3 * 2 * 1 = 120
                       4! = 4 * 3 * 2 * 1     = 24
                       3! = 3 * 2 * 1         = 6
                       2! = 2 * 1
    [출력결과]
    숫자 입력 : 5
    5! = 120
'''
def factorial1(num) :
    if num == 1:
        return 1
    
    return num *factorial1(num-1)
my_num = int(input("숫자 입력 :"))
print( "{}! = {}".format(my_num,factorial1(my_num)))

def factorial2() :
    n = int(input("숫자 입력 : "))
    fac = 1
    for num in range (1,n+1) :
         fac = fac * num
    print("{}! = {}".format(num,fac))
factorial2()
print()








