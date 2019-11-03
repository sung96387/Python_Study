'''
    [반복문]
        조건에 만족하면 수행한다. (조건문과 동일!!)
        언제까지? 조건이 만족하지 않을 때 까지 반복..

        1. while문
            - 조건식이 참(True)이면 계속 수행
            - if문과 구조가 동일하다
                > if   : 참이면 한 번 수행
                > while : 참이면 수행 후 다시 조건식 비교 (계속 반복)
        
        2. for 문
            - 리스트, 튜플, 문자열 (요소가 나열되어있는 자료형)의
              첫 요소부터 마지막 요소까지 차례로 변수에 대입되어 수행문 수행
for 변수 in 리스트(튜플,문자열) :
    수행문 (변수안에 요소가 반복 수행마다 하나씩 대입)
    
        * 공통 (while, for -> 반복문 공통)
             1. break문 : 반복문 탈출(종료/빠져나감)
             2. coutinue문 : 반복문의 첫 문장으로 돌아간다.
                        while문 : 조건식으로 이동 (점프)
                        for문 : 변수에 다음 요소를 대입
            * if문 안에 쓰인다. (특정 조건일때 탈출/점프)
'''

print("="*20)
print("{:^20}".format("반복문"))
print("="*20)

print("[while문]")

num = 0
while num < 3 :
    print("num = {}".format(num))
    num += 1
    
# 반복문에서의 num 이라는 변수는 '조건변수'
# 이 조건변수는 매우 매우 중요하다.
# 조건변수 관련해서 '조건식'과
# 조건변수 값의 변화 (증가,감소 등)에 따라서
# 반복문이 몇 번 반복을 할지 정해진다.

# num 을 1씩 증가시키지 않으면, 계속 0이기 때문에
# 반복문은 끝나지 않는다. ==> 무한루프 현상
# 무한루프는 Ctrl + C 눌러서 종료시킨다.

'''
while True : # 조건이 항상 만족 => 무한루프
    print("무한루프 빠져나오기 : Ctrl + C")
'''

'''
while 조건식에 사용될 변수는
조건식에서 '사용'되는 변수이기 때문에
미리 선언을 해야 한다.
'''
# print(a) # 없는 변수의 사용   - 오류
# while a < 10 : # 마찬가지     - 오류
#    print("aaa")

'''
조건변수 생성
while 조건식 : <-- 조건변수가 들어간다.
    수행문(수행할 코드 + 조건변수 변화식)

조건변수 변화식은 꼭 +,- 같은게 아니어도,
조건식만 언젠가 빠져나올수 있다면 (거짓/False)
얼마든지 자유롭게 사용 가능하다.
'''
# 반복횟수 지정
'''
count = int(input("반복할 횟수 입력 : "))
while count > 0 : # 만족하면 수행 ! 0보다 크면 수행
    print("count ={}".format(count))
    count -=1
'''

# 특정 조건 만족
'''
num = 0

while num != 9 : # num이 9가 아니면 수행
    num = int(input("9를 입력 하면 종료 : "))
'''

'''
# break문 사용 (반복문 강제 종료)
while True : # 무한루프 조건
    num = int(input("9를 입력 하면 종료 : "))
    if num == 9 :
        break # break를 만나는 순간 소속된 반복문 탈출
    
    print("첫 번째 while문 중간!")
    
    while True : # while문 중첩 / 2중 while문
        if num == 3 :
            print("두 번째 while문 탈출!")
            break # 여기서 break는 두번째 while문 탈출
        
    print("첫 번째 while문 끝!")
'''

print()
# continue문 사용
num = 1
while num < 10 : # num이 10보다 작으면 수행
    num += 1 # num 1 증가

    if num % 2 == 1 : # 2로 나눈 나머지 = 1 --> 홀수
        continue # continue 만나는 순간 조건식으로 점
    # 이것도 break와 마찬가지로 소속된 반복문으로 점프
    print(num) # 10도 찍힌다! (9일때 진입)


# while문 연습
'''
    1. 1부터 10까지 합 구하기
    [출력결과]
    1~10까지 합은 55 입니다.

    2. 1 부터 입력받은 수까지 합 구하기
    [출력결과]
    숫자 입력 : 5
    1 ~ 5까지 합은 15 입니다.

    3. 구구단 7단 출력하기
    [출력결과]
    7 * 1 = 7
    7 * 2 = 14
    ...
    7 * 9 = 63

    4. 입력받은 단 출력하기
    [출력결과]
    단을 입력하세요 : 5
    5 * 1 = 5
    5 * 2 = 10
    ...
    5 * 9 = 45

    5.별(*) 찍기
    입력된 숫자만큼 아래와 같은 모양으로 별 찍기
      > 조건변수 활용
      > 문자열 관련해서 사용
    [출력결과]
    숫자를 입력하세요 : 5
    *
    **
    ***
    ****
    *****

    6. 숫자 맞추기 게임
    1 ~ 100 랜덤으로 정답 숫자 미리 생성
    while문 안에서 숫자를 입력받고
    숫자가 정답이면 탈출

    [출력결과] (정답이 70일 때)
    숫자 입력 : 60
    더 큰 수를 입력해 주세요.
    숫자 입력 : 75
    더 작은 수를 입력해주세요.
    숫자 입력 : 70
    정답입니다!
*[심화] 3회 만에 맞추셨습니다!
(몇 회만에 맞췄는지 출력)
    
'''
'''
num = 1
result = 0
while num <= 10 :
    result += num
    num += 1
print("1부터 10까지의 합은 ",result)

num = int(input("숫자 입력 : "))
result = 0
while num > 0 :
    result += num
    num -= 1
print("1부터 {}까지의 합은 {}".format(num,result))

num = 1
while num < 10 :
    print("7 * {} = {}".format(num,num*7))
    num += 1

dan = int(input("단을 입력하세요 : "))
num = 1
while num < 10:
    print("{} * {} = {}".format(dan,num,num*dan))
    num += 1

# 단일문으로 별찍기 하기
num = int(input("숫자 입력 : "))
count = 0
while count < num :
    count = count + 1
    print("*"*count)

count = 0
num = int(input("숫자 입력 : "))
while count < num :
    count = count + 1
    star = 0
    while star < count :
        star=star+1
        print("*",end="")
    print()

# 랜덤으로 숫자만들기
import random # 파이썬에서 미리 만들어 놓은 random이라는 '모듈'
answer = random.randint(1,100) # 1 ~ 100 중에 랜덤숫자 생성
count = 0
while num != answer :
    num = int(input("숫자 입력 : "))
    if num > answer :
        print("더 작은 수를 입력해 주세요")  
    elif num < answer :
        print("더 큰 수를 입력해 주세요")
    else :
        print("정답입니다!")
    count += 1
print("{}회 만에 맞추셨습니다.".format(count))
'''
'''
print("[for문]")
for a in [1,2,3] :
    print(a) # 숫자

print("a =", a) # for문에서 만든 a 는 for문이 끝나도 유효
# while문은 조건식에 들어가는 변수는 '사용'이 되어야해서
# 미리 만들어진 변수여야 한다.
# for문은 식 안에서 '대입'이 되는 변수라 만들어진다.

for a in ["한국", "일본", "중국"] :
    print(a)

for a in "ABCD1234" :
    print(a) # 문자열일때는 한개 문자씩 대입

for a in [1,2,3,4,5] :
    print("=======") # a를 써야만 하는건 아니다
                     # 몇 회 반복만의 용도
# 반복문에 사용되는 변수 : 반복만을 위한 용도 / 값사용 + 반복

# 리스트 안의 튜플을 순서대로 튜플 변수에 담기
# (a,b) = (1,2)
for (a,b) in [(1,2), (3,4), (5,6)] :
    print(" {} + {} = {}".format(a,b,(a+b)))
# (a,b) 이렇게 사용하는건 눈여겨 볼 필요가 있다!
print()

# range() : 지정한 범위만큼의 숫자를 반환
print(range(10))
print(list(range(10))) # 0 ~ 9
print(list(range(1,10))) # 1 ~ 9
print(list(range(1,10,2))) # 1 부터 시작, 2 씩 건너뛴다.
print(list(range(10,0,-1))) # 10 ~ 1 , -1씩
# range() 에는
# 기본 시작 숫자 : 0
# 기본 건너뛰는 숫자 : 1
# 끝숫자는 포함 안함
'''
print()
'''
# 1~10까지의 합 : 10회 반복
sum1 = 0
# in 은 포함되어있는지 비교하는 연산자가 아니다.
# 포함을 시키는 예약어
for i in range(1,11) :
    sum1 += i
print("1~10 까지의 합 : " , sum1)


# 입력 횟수만큼 반복
count = int(input("반복 횟수 입력 : "))
        # 0 ~ (count-1)
for i in range(count) : # 3을 입력 -> 0,1,2
    print(i)
# 만약 1 ~ count까지라면 range(1,count+1)
'''

# for문 활용 예시(1)
'''
score_list = [30,95,65,22,100] # 5명의 점수 목록
num = 0 # 몇 번째 학생인지 담을 변수

for score in score_list :
    num += 1 # 초기 값이 0이었기 때문에 수행 시작부터 1 증가

    #if score >= 60 :
    #   print("{}번째 학생 합격입니다.".format(num))
    #else :
    #    print("{}번째 학생 불합격입니다.".format(num))
    if score < 60 :
       continue # 여기까지만 if문 수행문

    print("{}번째 학생 합격입니다.".format(num))
'''
# for문 활용 예시(2)
# 구구단 출력 - for문 2개가 중첩된 2중 for문 사용
'''
for i in range(2,10) :# i는 구구단의 단 (2~9)
    for j in range(1,10) : # j는 곱해지는 숫자 (1~9)
        print("{} * {} = {}".format(i,j,i*j),end ="\t")
    print()
'''

'''
my_list = [1,2,3]
result = []
for i in my_list :
    result.append(i*5) # 리스트 뒤에 추가

print(result)

# 리스트 안에 for문 포함시키기
result2 = [i*5 for i in my_list]
# 리스트를 그냥 콤마로 나열하면서 쓰면 하나의 값들
# 리스트 안에  for문이 들어가면 하나의 문장(코드)
print(result2)

# range() 사용
result3 = [i*3 for i in range(1, 11)]
print(result3)
# if문 사용
result4 = [i*3 for i in range(1,11) if i % 2==0]
print(result4)
'''
'''
# for문 2개를 리스트에 담기
result5 = [x*y for x in range(1,5) for y in range(2,4)]
# x가 1일 때, y값 2,3
# x가 2일 때, y값 2,3
print(result5)
'''

# for문 연습문제
'''
    1. 1부터 입력받은 수까지 짝수의 합 구하기
    [출력결과]
    숫자 입력 : 5
    1 ~ 5 까지 짝수의 합은 6입니다.

    2. 1~200까지 '3과 4의 공배수'를 더하다가
       더한 수가 1000을 초과한 경우, 반복문을 빠져나오고
       더해진 수와 빠져나올 때의 수 (1~200중 하나)를 출력하기
    [출력결과]
    빠져나온 수 : 156
    더해진 수 : 1092

    3. 1~100 사이 정수 중,
       3의 배수와 5의 배수를 역순으로 출력하기
       단, 3과 5의 공배수는 [15] 와 같이 출력하기

    [출력결과]
    100 99 96 95 93 [90] 87 ... 5 3
  
'''
num = int(input("숫자입력 : "))
result = 0
for i in range(1,num) :
    if i % 2 == 0 :
        result += i
print("1~{} 까지 짝수의 합은 {} 입니다.".format(num,result))

sum1 = 0
for i in range (1,1000) :
    if i % 3 == 0 and i % 4 == 0 :
        sum1 += i
        if sum1 >=1000 :
            break
print("빠져 나온 수 : ", i)
print("더해진 수 : ",sum1)

for i in range(100,1,-1) :
    if i % 5 == 0 and i % 3 == 0 :
        print("[{}]".format(i),end =" ")
    elif i % 5 == 0 :
        print(i,end =" ")
    elif i % 3 == 0:
        print(i,end =" ")
    else :
        continue










