# 파이썬에서 사용하는 '자료'의 종류를 알아본다.
# data type -> 자료형

'''
    [1. 숫자형(Number)]
      정수(integer)         : -10, 0, 10
      실수(floating-point)  : 11.1, -10.1
      지수표현(exponent)    : 20.1e1, 20.1E1
      2진수(binary-number)  : 0b10, 0B10 -> 10진수 2
      8진수(octal-number)   : 0o10, 0O10 -> 10진수 8
      16진수(hexa)          : 0x10, 0X10 -> 10진수 16

      사칙연산 : + - * /
      제곱연산 : **
      나머지연산 : %
      몫 연산 : //
      
'''

print("======================")
print("1. 숫자형")
print("======================")

print("[기본 숫자형]")
print("정수 :", 10, 0, -10)
print("실수 :", 10.4435, -10.123)
print("지수 :", 20.1e1) # e,E 우측 숫자만큼 소수점 이동
print("지수 :", 20.1e-1) # -1 왼쪽 , +1 오른쪽, 0 그대로

#20.1e1  = 20.1 *  10^1   = 201.0
#20.1e-1 = 20.1 *  10^-1  = 2.01

#print() 는 숫자를 10진수로 출력
print("2진수 0b10 =", 0b10)
print("8진수 0o10 =", 0o10)
print("16진수 0x10 =", 0x10)
print()

print("[숫자 연산하기]")
num1 = 10
num2 = 3
print("[num1 = ", num1, ", num2 = ", num2, "]", sep="")
print("num1 + num2 =", (num1+num2))
print("num1 - num2 =", (num1-num2))
print("num1 * num2 =", (num1*num2))
print("num1 / num2 =", (num1/num2))
print("num1 % num2 =", (num1%num2))
print("num1 // num2 =", (num1//num2))
print("num1 ** num2 =", (num1**num2))

print(" -7 / 3 = ", (-7/3))
print(" -7 // 3 = ", (-7//3))
# // 의 결과는 나눗셈의 결과보다 작은 정수중 가장 큰 수
print()

'''
    [2. 문자형]
      "abc"
      'abc'
        --> 따옴표로 둘러싸이면 문자열

      문자열 만드는 방법 (아래 기호로 묶는다)
        1. 큰 따옴표
        2. 작은 따옴표
        3. 큰 따옴표 3개 연속
        4. 작은 따옴표 3개 연속
        
      이스케이프 문자 ( 특수기능이 있는 문자)
        \n : 개행(줄바꿈) newline
        \t : tab 만큼 공백
        \\ : 출력시 \ 찍기
        \' : ' 찍기
        \" : " 찍기 
'''
print("======================")
print("2. 문자형")
print("======================")
# 문자열을 만드는 네 가지 방법
print('(1) happy day')
print("(2) happy day")
print('''(3) happy day''')
print("""(4) happy day""")

# 각 방법들의 사용 용도
# 1) 문자열 안에 작은 따옴표를 포함시키고 싶을때
#print(''문자열'입니다')
     #'문자열'입니다.
print( "'문자열'입니다." )

# 2) 반대의 경우도 동일하다.

# 3) 이스케이프 문자를 사용.
print( '\'문자열\'입니다.' )
print()

# 4) 여러 줄의 문자열을 출력하기
#     --> ''', """가 사용된다.
print('''파이썬
수업입니다.''')

print('파이썬\n수업입니다.')

# 여러 줄 출력 시 개행 붙이기 : \를 붙이면 개행이 사라진다.
print("""파이썬\
안녕하세요.""")

string = """파이썬\
안녕하세요."""
print(string)
print()

# 문자열과 주석의 관계
print("[문자열과 주석]")
import sys
myString = '''안녕1'''
'''안녕2'''
print('안녕1 count :', sys.getrefcount('''안녕1'''))
print('안녕2 count :', sys.getrefcount('''안녕2'''))
print()

'''
    문자열 연산하기
      1. + 연결하기
      2. * 반복하기
      
'''

print("[문자열 연산하기]")
print("안녕"+"하세요")
print("안녕"*3)
print()

# 곱하기 응용
print("="*20)
print("코드가 깔끔")
print("="*20)

'''
    문자열 다루기 연습문제

    1. 출력 연습
    철수 "안녕? 파이썬 재밌지?"
    영희 "응, 너무 재밌어!"

      1) 작은따옴표 3개 문자열, 이스케이프 문자 사용 x
      2) 큰따옴표 1개 문자열, 이스케이프 문자사용
      3) 조건없이, 대화내용을 한줄로 출력


    2. 연산 연습
      print()3번 사용하여 아래와 같이 출력
      
********************    20개
     파이썬강의         앞에 빈 칸 5개
     파이썬강의
     파이썬강의
******************** 
'''

print("문자열 다루기 연습문제 1")
print("1) 작은따옴표 3개 문자열, 이스케이프 문자 사용 x")
print('철수 "안녕? 파이썬 재밌지?"')
print('영희 "응, 너무 재밌어!"')
print("2) 큰따옴표 1개 문자열, 이스케이프 문자사용")
print("철수 \"안녕? 파이썬 재밌지?\"")
print("영희 \"응, 너무 재밌어!\"")
print("3) 조건없이, 대화내용을 한줄로 출력")
print('철수 "안녕? 파이썬 재밌지?"', end="")
print('영희 "응, 너무 재밌어!"')

print("문자열 다루기 연습문제 2")
print("*"*20)
print((" "*5 +"파이썬강의\n")*3,end="")
print("*"*20)

'''
    문자열 인덱싱
      인덱싱(indexing) : index 색인. 무언가를 가리킨다.
      (중요) 정수로 표현. 순서가 0부터 시작
      -1 하면 뒤에서부터 센다.
'''

print("[문자열 인덱싱]")

#서두르지도 말고, 쉬지도 말고 - 괴테
myStr = "Without haste, but without rest." #32글자.
print(myStr)
print(myStr[0]) # [] 안의 0은 index
print(myStr[10])
print(myStr[-1]) 

# print(myStr[32]) # index 범위 초과 시 오류
# print(myStr[-33]) # 음수 index도 동일하다.

'''
    문자열 슬라이싱
        슬라이싱(slicing) : 조각낸다.

        a[0:3]    콜론(:)으로 인덱스 범위 지정 
        a[시작번호:끝번호] --> 끝번호 문자는 뽑지 않는다.
             시작번호 <= a < 끝번호

        a[시작번호:] -> '시작번호' 부터 '끝' 까지
        a[:끝번호]   -> '처음' 부터 '끝번호' 까지
        a[:]         -> '처음' 부터 '끝' -> 전체 -> a
'''

print("[문자열 슬라이싱]")
myStr = "Without haste, but without rest." # 32글자.
print(myStr[0] + myStr[1] + myStr[2] + myStr[3]) # 불편
print(myStr[0:4]) # 편안
print(myStr[8:13]) # 시작이 0일 필요가 없다.
print(myStr[0:100]) # 슬라이싱은 범위 초과 시 자동으로 마지막까지 출력
print(myStr[8:]) # 시작번호 ~ 끝
print(myStr[:4]) # 시작 ~ 끝번호
print(myStr[:-7]) # 음수 index도 가능. 끝번호 포함 x
print(myStr[:-200]) # 0 ~ -200 . 문자열이 없다!
print(myStr[:]) # print(myStr) 동일!

# myStr[0] = "w" # 이미 만들어진 문자열은 변경할수 없다 -> 오류
# 바꾸고 싶으면? 새로운 문자열을 생성!
newStr = "w" + myStr[1:]
print(newStr)
print()

'''
    문자열 포매팅 (fprmat)
        문자열 내에 어떤 값을 삽입하는 방법
        출력할 문자열의 값들이 변화될때 유용하다.

    포맷 코드 (서식 문자)
        %s 문자열 (string) <- 어떤 값이던 변환해서 넣는다.(만능)
        %c 문자 1개
        %d 정수
        %f 실수(소수)
        %o 8진수
        %x 16진수
        %% %를 삽입!
      
'''

print("[문자열 포매팅]")
print("정수 : %d" % 21) # 정수
print("실수 : %f" % 21.123) # 실수(소수) , 기본 소수점 6자리
print("문자열 : %s" % "문자열 입니다." ) # 문자
print("16진수 : %x" %0x10) # 16진수

print("(형변환)정수->실수 : %f" % 20)
print("(형변환)실수->정수 : %d" % 20.458328) # 값의 손실.

# print("정수 : %d" % "123")  # 문자 -> 숫자 = 에러
print("문자열 : %s " % 123)    # 만능
print("문자열 : %s " % 123.123) # 만능

number = 2018
print("변수 대입 : %d" % number) # 변수를 넣는 것도 가능
print("변수 대입 : %s" % number) 
 
#print("2018년입니다.")
#print("2019년입니다.")
#print("2020년입니다.")
#print("2021년입니다.")

year = 2018
print("%d년입니다." % year)
year += 1 # year = year + 1
# year가 새로운 2019 라는 숫자를 가리킨다.
print("%d년입니다." % year)
year -= 2
print("%d년입니다." % year)
# year *= 2 --> year = year * 2
# year /= 2 --> year = year / 2
# year **= 2
# year //= 2
# year %= 2

print("%d개 이상의 %s 넣기" % (2,"문자열")) # 순서!
print("현재 진행율은 98%입니다.")
# %의 출력은 포맷코드가 쓰이면 %% 두 개를 써야 한다.
print("현재 진행율은 %d%%입니다." %98)
print()

print("[소수점 표현]")
print("기본 6자리 : %f" %3.1)
print("자동 반올림 : %f" %3.12345678)
# 소수점 지정도 반올림을 한다.
print("소수점지정(1) : %.1f" %3.12345678)
print("소수점지정(3) : %.3f" %3.12345678) 
print("소수점지정(10) : %.10f" %3.12345678)
print()

print("[정렬과 공백]")
# 앞에 숫자를 쓰면 숫자 만큼 공간 확보
print("[%s] [%s]" % ("파이썬", "재밌다"))
print("[%20s] [%20s]" % ("파이썬", "재밌다")) # 우측 정렬
print("[%-20s] [%-20s]" % ("파이썬", "재밌다")) # 좌측 정렬
print()

# 여기 까지 맛보기
# 지금부터 중요

print("[고급 문자열 포매팅]")
# 문자열.format() <-- 문자열 포맷함수
print("제 이름은 {}입니다.".format("최성현") )
# print("".format())
print("제 나이는 {0}살 입니다".format(23))

# {} 안에 있는 숫자는 인덱스. format() 안에 있는 값의 인덱스 (0부터시작)
print("01 제 이름은 {}이고 {}살 입니다".format("최성현",23))
print("02 제 이름은 {0}이고 {1}살 입니다".format("최성현",23))
print("03 제 이름은 {1}이고 {0}살 입니다".format("최성현",23))
print("03 제 이름은 {1}이고 {1}살 입니다".format("최성현",23))

# 변수도 대입 가능
name = "최성현"
age = "23"
print("04 제 이름은 {}이고 {}살 입니다".format(name,age))
print("05 제 이름은 {0}이고 {1}살 입니다".format(name,age))
print("06 제 이름은 {1}이고 {0}살 입니다".format(name,age))

# 키워드 사용 
print("07 제 이름은 {name}이고 {age}살 입니다".format(name = "최성현",age = 23))
# {}안에 있는 키워드 name, age는 위에 만들어놓은 변수들과 아무런 관계가 없다.

print("08 제 이름은 {name}이고 {age}살 입니다".format(name = name,age = age))
# 이제서야 name, age 변수가 키워드에 대입되면서 사용되었다.

print("09 제 이름은 {name}이고 {age}살 입니다".format(age = age,name = name))
# 키워드를 사용하면 순서가 상관없다.

print("10 제 {}은 {name}이고 {}살 입니다".format("이름", 23 , name=name))
# 키워드 혼용 시 '반드시' 키워드 값 대입은 format()에서 맨 뒤에 위치해야한다.

# print("10 제 {}은 {name}이고 {}살 입니다".format("이름", name=name, 23 )) => 오류
print()

print("[format()으로 소수점 표현]")
print("소수점 전체자리수 표현 : {}".format(21.1123))
print("소수점 전체자리수 표현 : {}".format(21.123456789123456789))
print("소수점 3자리까지 표현 : {:.3f}".format(21.123456789123456789))
print("소수점 3자리까지 표현 : {0:.3f}".format(21.123456789123456789))
print("소수점 10자리까지 표현 : {:.10f}".format(21.123456789123456789))
# {}안에 : 이 붙는다 --> 형식을 지정

print("[format()으로 정렬하기]")
print("[{}] [{}]".format("Hello", "Python"))
print("[{:20}] [{:20}]".format("Hello", "Python")) # 기본 좌측정렬
# 최소 20칸 확보 후 문자열 쓰기

print("[{:>20}] [{:>20}]".format("Hello", "Python")) # 우측정렬
print("[{:<20}] [{:<20}]".format("Hello", "Python")) # 좌측정렬 (기본값)
print("[{:^20}] [{:^20}]".format("Hello", "Python")) # 가운데정렬 

# 정렬 후 빈칸을 문자로 채우기 --> 정렬 기호 앞에 넣는다.
print("[{:하^20}] [{:하^20}]".format("Hello", "Python"))
print("[{: ^20}] [{: ^20}]".format("Hello", "Python")) # 공백이 기본값
# print()에 sep=" ", end="\n" 가 기본값인 것 처럼
# format()에도 기본 값이 있다.

# {}   --> 자동으로 순서에 맞게 인덱스 번호가 붙는다
# <    --> 정렬 시 기호를 넣지 않으면 기본으로 좌측 정렬이 된다.
# 공백 --> 정렬 시 자동으로 빈 칸은 공백이다.

print()

'''
    문자열 다루기 연습문제

    1. 출력 연습
    철수 "안녕? 파이썬 재밌지?"
    영희 "응, 너무 재밌어!"

      1) 작은따옴표 3개 문자열, 이스케이프 문자 사용 x
      2) 큰따옴표 1개 문자열, 이스케이프 문자사용
      3) 조건없이, 대화내용을 한줄로 출력
'''
#1
print('''철수 "안녕? 파이썬 재밌지?"
영희 "응, 너무 재밌어!"''')
#2
print("철수 \"안녕? 파이썬 재밌지?\"\n영희 \"응, 너무 재밌어!\"")
#3 개행을 붙이는 \를 사용했을 때 뒤에 다른 문자 붙이지 않는다.
print('철수 "안녕? 파이썬 재밌지?"', end="")
print('영희 "응, 너무 재밌어!"')

'''
    2. 연산 연습
      print()3번 사용하여 아래와 같이 출력
      
********************    20개
     파이썬강의         앞에 빈 칸 5개
     파이썬강의
     파이썬강의
******************** 
'''
print("*"*20)
print((" "*5 +"파이썬강의\n")*3,end="")
print("*"*20)

'''
    3. 슬라이싱 연습(1번)
       phoneNumber 에서 숫자만 가져와서 새로운 변수에 저장

phoneNumber = "010-8383-9133"
# 여기에 코드 작성
print(새로운변수) --> 01083839133
'''
phoneNumber = "010-8383-9133"
newNumber = phoneNumber[:3] + phoneNumber[4:8] + phoneNumber[9:]
print(newNumber)
'''
    4. 슬라이싱 연습(2번)
        info에서 이름과 성별을 각각의 변수에 저장

info = "한수창 - 남자"
# 여기에 코드 작성
print(name) --> 한수창
print(sex) --> 남자
'''
info = "한수창 - 남자"
name = info[:3]
sex = info[6:]
print(name)
print(sex)
'''
    5. 포매팅 연습
name = "한수창"
age = "20"
phone = "010-8383-9133"
[출력결과]
이름 : 한수창
나이 : 20
번호 : 010-8383-9133

    1) 포매팅 -> format() 사용하지 않고!
    2) 포매팅 -> format() 사용
    3) 포매팅 사용하지 않고.
'''
name = "한수창"
age = "20"
phone = "010-8383-9133"
#1
print("이름 : %s\n나이 : %s\n번호 : %s" %(name,age,phone))

#2
print("이름 : {}\n나이: {}\n번호 : {}".format(name,age,phone))

#3
print("이름 : " + name + "\n나이 : " + age + "\n번호 : " + phone)
# 코드에 정답은 없다!!
print()

print("[문자열 함수]")
str1 = "I'm a Boy"
print("대문자로(upper) : " + str1.upper())
print("대문자로(upper) : adfhdsjafk".upper())
print(str1)

print("소문자로(lower) : " + str1.lower())
print("소문자로(LOWER) : ADHFDSFDSF".lower())
# upper(), lower() 변환하는 함수는 원래 문자열을 바꾸는 것이 아니라,
# 작업을 완료한후 새로운 문자열을 '반환' 하는것
print()

str2 = "python"
print("제목을 대문자로(title) : " + str2.title())
print("제목을 대문자로(title) : python".title())
print()

str3 = "        공백 제거           "
print("좌우측 공백제거(strip) 사용 x -> " + str3)
print("좌우측 공백제거(strip) 사용 o -> " + str3.strip())
# Web 프로그래밍을 할 때 자주 쓰게 될 것
print( "       좌우측 공백제거        ".strip())

print("좌측 공백제거(lstrip) 사용 x -> " + str3)
print("좌측 공백제거(lstrip) 사용 o -> " + str3.lstrip())
print( "       좌측 공백제거        ".lstrip())

print("우측 공백제거(rstrip) 사용 x -> " + str3)
print("우측 공백제거(rstrip) 사용 o -> " + str3.rstrip())
print( "       좌측 공백제거        ".rstrip())
print()

a = ","
print( a.join("문자열삽입join()"))
print( ",".join("python"))
print( ".".join("C언어"))
print( ",".join("JAVA"))
# 삽입될 문자가 변할 소지가 있다면 변수로 사용 하는게 좋다.(중복코드의 제거)
print()

str3 = "문자열 대체하기(replace) : python python"
str4 = str3.replace("py","Py")
print(str4)
# replace()도 대체된 새로운 문저열이 '반환'
# 반환된 새 문자열을 str4가 가리킨다.
# 찾은 문자열 모두 다 바꾼다.
print()
str5 = "문자열 나누기(split)"
print(str5)
print(str5.split())
# split()은 기준이 되는 '문자'로 대상 문자열을 나눈다.
# () 소괄호 안에 아무것도 넣지 않으면 기준 문자는 공백이다.
str6 = "말을.더듬.더듬.더듬."
print(str6.split("."))
# 출력된 결과는 리스트이다.(list)
print()

str1 = "문자열 위치 찾기(index)" # 문자를 찾아서 찾은 위치(index) 반환 -> 정수
print(str1,str1.index("문"))
print(str1,str1.index("index")) # 일치하는 문자열의 시작하는 위치(index) 반환
# print(str1,str1.index("123")) # 찾는 문자열이 없으면 오류 발생!!!
print("문자열문자열".index("자")) # 처음 찾는 문자의 위치(index)를 반환
print()

str1 = "문자열 위치 찾기(find)"
print(str1,str1.find("문"))
print(str1,str1.find("find")) # 일치하는 문자열의 시작하는 위치(index) 반환
print(str1,str1.find("123")) # 찾는 문자열이 없으면 -1을 반환.
print("문자열문자열".find("자")) # 처음 찾는 문자의 위치(index)를 반환
print()

print("문자열문자열".index("문"))
print("문자열문자열".rindex("문")) # r이 붙으면 뒤에서부터 찾는다. (reverse)

print("문자열문자열".find("문"))
print("문자열문자열".rfind("문")) # r이 붙으면 뒤에서부터 찾는다. (reverse)
print()

print("문자열문자열".index("문",1)) # 1번 index부터 찾아라!
print("문자열문자열".find("문",1))


# 사용빈도 적당 - 대소문자 변환 , 삽입
# 사용빈도 높음 - 대체, 나누기, 찾기, 공백제거


