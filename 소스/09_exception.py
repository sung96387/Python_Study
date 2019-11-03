'''
    [예외처리]   - exception(예외)
      - 의도치 않은 오류 발생에 대한 처리
       > 개발자가 의도하지 않은 오류를 미리 처리해 놓음
       > 예외처리가 없으면? 프로그램 중단후 오류메세지

       - try, except문

try :
    수행문 --> 일반적인 코드 (예외 발생 예상 코드)
except :
    오류 발생했을 시 수행문
    
'''

'''
# try, except를 통한 예외처리
# 1) 오류 발생 시 except로 바로 점프
# 2) 오류 미 발생 시 try 수행문 모두 수행 , except 수행 x
try :
    # 예외(오류) 발생 예상 지역
    num = int(input("숫자 입력 : "))
    # 여기서 오류 발생 시 try문은 더이상 수행되지 않고
    # except 문으로 점프한다.
    print("입력한 숫자 :", num)
except :
    # 오류 발생시 수행
    print("숫자를 입력하세요!!!")
'''

# finally : try문에 종속되는 문장
#    > 오류 발생/미발생과 상관 없이 무조건 수행되는 문장
# 무조건 가장 마지막에 위치해야한다.!
'''
x = 10

# 어떠한 수를 0 으로 나누면 오류가 발생한다.
try :
    num = int(input("나눌 숫자 입력 :"))
    result = x / num
    print("나눈 결과 :",result)
except: # 모든 에러에 대한 처리 가능 (따로 에러를 지정하지 않았다)
    print("오류 발생")
finally :
    print("끝")
'''
'''
    1. try
    2. except - 예외에 대한 처리
         > 순서상으로 except만 있는 문장은 맨 아래 (if문에서 else과 같은 효과)
    (선택)
    3. else - 오류발생 안 했을 때
    4. finally - 오류 발생 하던 안하던 무조건!
'''

# 어떤 오류인지 찾기 - 다중 except문
'''
try :
                            # split()에 아무 값도 넣지 않으면 공백으로 나누겠다.
    num1, num2 = map(int,input("두 수 입력 : ").split())
    result = num1 / num2

    my_list = [1,2,3] 
    print(my_list[5]) # 인덱싱 접근 오류가 난다!
# e1을 이용해서 오류 메세지를 출력하겠다.
# as의 역활 ~~~ 을 이 이름으로 칭하겠다.
except ZeroDivisionError as e1 : # ZeroDivisionError 오류 일때 이 except문 수행
    print("0 으로 나울 수 없습니다.")
    print(e1)

except ValueError as e2 :
    print("숫자를 입력해주세요.")
    print(e2)
except IndexError as e3 :
    print("인덱싱을 다시 지정해주세요.")
    print(e3)
else : # 오류가 발생하지 않았을 때만 수행되는 문장
    print("성공!")

# else는 try문 가장 끝에 코드를 작성한 것과 같은 효과
# 정상일때만 수행을 한다는 것을 명시하고 싶은 것!
'''

'''
    프로그램에서의 오류
        1) 컴파일 오류
          > 문법자체에 오류
          > 실행 파일이 만들어지지 않는다. (파이썬은 실행 자체가 안 됨)
        2) 런타임 오류
          > 런타임 : 실행 도중
          > 예외 처리는 런타임 오류에 대한 처리
        3) 논리적 오류
          > 프로그램 자체에 오류는 발생하지 않지만,
            개발자가 의도한대로 수행되지 않는다.
            
'''

my_num = input("나눌 숫자 입력 : ")
#######################################################
# my_num 에는 현재 문자열이 들어있다(input에 의해)
# int에 대해서 예외 처리 하고 싶으면, 문자열에 숫자와 - 기호만 있는지 판별
for i in my_num : # 문자열에서 한 글자씩 뽑아온다.
    if i in ["1","2","3", "4"] : #여기 해당되는 문자가 없으면 int하면 안됨
if is_number == True :
    my_num =int(my_num)
else :
    print("숫자를 입력하세요!")
# 입력된 문자열이 숫자로 변환 가능한지 직접 예외처리!
#######################################################
x = 10

# try를 사용하지 않고 우리가 직접 예외 처리
if my_num != 0 :
    print("{} / {} = {}".format(x,my_num,(x/my_num)))
else :
    print("0으로는 나눌 수 없습니다.")























