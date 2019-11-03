'''
    [3. 리스트(list) 자료형]
        데이터들의 목록
        순서가 있다.
        값의 중복이 가능

        상당히 편리하다

        리스트명 = [요소1, 요소2, ...]
'''

print("="*20)
print("{:^20}".format("3.List"))
print("="*20)

print("[리스트 만들기]")
a = [] # 빈 리스트
b = [1, 2, 3] # 숫자를 요소로 가진 리스트
c = ["AA", "BB", "CC"] # 문자열을 요소로 가진 리스트
d = [1, 2 , "AA", "BB"] # 혼합된 리스트
e = [1, "AA", [2, "BB"]]
# 리스트를 요소로 가진 리스트
# (혼합된 리스트 안에 다른 혼합된 리스트)

print("리스트 a :", a)
print("리스트 b :", b)
print("리스트 c :", c)
print("리스트 d :", d)
print("리스트 e :", e)
# [] 대괄호로 묶인 것이 리스트

print("리스트 c type:", type(c))
# 자료의 실제 자료형을 구하는 함수
print()

print("[리스트 인덱싱, 슬라이싱]")
stu_list = ["한수창", "홍길동" , "이몽룡"] #studentList
print("학생 목록:", stu_list)
print("첫 번째 학생 :", stu_list[0])
print("type :", type(stu_list[0]))

print("마지막 학생 :", stu_list[-1])
# print(stu_list[100] # 마찬가지로 범위 초과 시 오류!

print("현재 리스트는 문자열이 들어 있다" + stu_list[0])
soochang = stu_list[0]
print("첫번째 학생은 " + soochang + "입니다.")
print()

# 이중 리스트 인덱싱
stu_list = ["한수창", "홍길동" , ["성춘향", "임꺽정"]]
print( stu_list[2][0])
print( stu_list[2][1]) #3번째(index=2) 요소에서 다시 요소 접근
print( stu_list[2]) # 3번째(index=2) 요소는 list이다.
print()

# 이중 리스트 슬라이싱 : 문자열과 동일
print( stu_list[0:2]) # 슬라이싱의 결과는 리스트!
# 문자열 슬라이싱 -> 결과는 문자열
print( stu_list[2][0:1] )
# 0번 인덱스 요소만 가져오지만, (1개이지만)
# 리스트 슬라이싱이기 때문에 결과도 리스트
print()

print("[리스트 연산하기]")
a = [1,2,3]
b = [4,5,6]
print("리스트 더하기 :", (a+b))
c = a + b
print("리스트를 더한 변수는 ? ",c)
print("리스트 반복하기 :" , (a*3))
d = a*3
print("리스트를 곱한 변수는 ? ",d)
print()

print("[리스트 수정하기 (변경, 삭제)]")
a = [1, 2, 3, 4, 5, 6]
print("변경 전 :", a)
a[2] = 4
print("변경 후 :", a)

#연속된 범위의 수정
#a[0:2] = 0 # 0,1 두칸에 0값 하나 대입 # 리스트  슬라이싱의 결과는 리스트이기 때문에
a[0:2] = [0] # 리스트를 대입 
print("변경 후 :", a)

a[0:2] = [6,7,8] # 하나씩 값이 들어간다!
print("변경 후 :", a)

a[0] = [3, 4] # 0번 인덱스 위치에 리스트 추가
# 0번 요소에 값을 대입 --> 대입한 자료가 리스트 
print("변경 후 :", a)
print()

# 리스트 요소 삭제
a[0] = []
print("변경 후 :", a)

del(a[0])
print("변경 후 :", a)
# 해당 요소를 통째로 삭제

a[0:3] = []
print("변경 후 :", a)

# 인덱싱 후 [] 대입 -> 빈 리스트를 그위치에!
# 슬라이싱 후 [] 대입 -> 그 위치를 비워라(삭제)

del(a[0:2]) # a 리스트의 범위를 지정하여 삭제
print("변경 후 :", a)

del(a) # 리스트를 가리키던 a를 삭제
# print("변경 후 :", a)

'''
    리스트 인덱싱 연습하기
    
    [출력결과]
    2018년 새해가 밝았습니다. 내년은 2019년 입니다.

a = [2018, "입니다.", "새해", [" 내년", "가 밝았습니다."],"은 ", ["년 "] ]

'''
a = [2018, "입니다.", "새해", [" 내년", "가 밝았습니다."],"은 ", ["년 "] ]
print(a[0],a[5][0],a[2],a[3][1],a[3][0],a[4],a[0]+1,a[5][0],a[1],sep="")
print("[리스트 관련 함수]")

a = [1, 2, 3]
print("리스트 a :", a)

# append() : 리스트 가장 뒤에 요소 추가
a.append(4)
print("리스트 a :", a)
a.append([5,6])
print("리스트 a :", a)

# sort() : 정렬하기 : 숫자, 알파벳
a = [9,2,8,2]
print("리스트 a:", a)
a.sort()
print("리스트 a :", a)
a.sort(reverse=True) # 정렬 방법 / 내림 차순 / 오름 차순 /기본값은 오름 차순
print("리스트 a :", a)

a = [ "C", "v" ,"a" ,"c","V","A"]
print("리스트 a:", a)
a.sort()
print("리스트 a :", a)
a.sort(reverse=True) # 정렬 방법 / 내림 차순 / 오름 차순 /기본값은 오름 차순
print("리스트 a :", a)
# 기본 : 대문자 -> 소문자 순서로 정렬

# sort()와 sorted()
a = [3,1,2]
b = sorted(a)
print("리스트 a:", a)
print("리스트 b:", b)
# sort() : 주체가 a
# sorted() : 정렬한 a를 새로운 객체로 반환
print()

# reverse() : 리스트 뒤집기
a = [1,2,3,9,8,7]
a.reverse()
print("리스트 a:", a)
# 정렬이 되는건 아니다.

# index() : 리스트에서 값을 찾고 인덱스 반환
a = [1,2,3]
print("리스트 a에서 2의 위치:", a.index(2))

a = ["한수창","파이썬",1,2,3]
print("리스트 a에서 한수창의 위치:", a.index("한수창"))
# a.index("하하하") # 없으면 오류!
print()

# insert() : 내가 원하는 위치에 요소 삽입
# append()는 맨뒤에 추

a = [1,2,3]
a.insert(1,5)
print("리스트 a :", a)
print()

# remove(value) : 리스트에서 처음 찾은 value를 삭제
a = [1,2,3,1]
a.remove(1)
print("리스트 a :", a)
print()
# a.remove(5) # 없으면 오류
# a[0] = [] # 0번째 요소를 [] 빈리스트로 변경
# del(a[0]) # 0번째 요소 제거
# a.remove(0) # 0이라는 값을 찾아서 제거

# pop(index) : 리스트에서 index 위치 값을'반환'
#             하면서 그 값을 지운다.
a = [1,2,3,4]
print("리스트 a :", a)
print("a.pop(2)의 결과:", a.pop(2))
print("리스트 a :", a)
print()

# pop()안에 index를 지정하지 않으면 맨 마지막 요소
print("a.pop()의 결과:", a.pop())
# 앞으로 리스트 추가/삭제 등 작업 시 자주 사용!
print("리스트 a :", a)
print()

# count(value) : 리스트에서 value의 개수를 반환
a = [1,2,3,4,5,1,1,2]
print("a에서 1의 개수 :", a.count(1))
a = ["A","B","A"]
print(a.count("A"))
print(a.count("C")) # 없어도 오류 xx, 0을 반환
print()

# extend(list) : 원래의 리스트에 list를 더한다.
a = [1,2]
b = [3,4]

a.extend(b) # b도 어차피 [3,4]
a.extend([5,6]) # 리스트만 들어올수 있다!!
a += [7,8] # a = a + [7,8]
print("리스트 a:",a)
print()

# list 요소들이 문자열로만 이루어진 경우
# 문자열 함수 중 'join'을 이용하여
# 하나의 문자열로 만들 수 있다.
my_list =["대","한","민","국"]
my_str = "".join(my_list)
print(my_list)
print(my_str)

'''
    리스트 활용 연습
    my_list = ["!","요","세","요","하","녕","안"]
    안녕하세요!
    join을 활용하여 my_str에 저장 후 print(my_str).

'''
my_list = ["!","요","세","요","하","녕","안"]
my_list.pop(3)
my_list.reverse()
my_str = "".join(my_list)
print(my_str)
print()

''' 리스트, 튜플 같이 자료들이 모여있는 자료형 '군집'
    [4. 튜플(Tuple) 자료형]
        - 리스트와 비슷하다.
        - 차이점
           1. 생성
               리스트[]
               튜플 ()
           2. 튜플은 한 번 만들면 값을 바꿀 수 없다.
        - 만들어 놓고 변하질 않길 바란다면 튜플 사용
          일반적으로 리스트를 사용한다.
          
'''
print("="*20)
print("{:^20}".format("4.Tuple"))
print("="*20)

print("[튜플 만들기]")
a = ()
b = (1, ) # 요소가 1 개 일때는 뒤에 ,붙여야 한다. ,을 붙이지 않으면 튜플이 아니게 된다.
c = (1,2,3)
d = 1,2,3 # () 소괄호 생략 가능 --> 자료의 나열 = 튜플 
e = ("a", "b", (1,2))

print("튜플 a :", a)
print("튜플 b :", b)
print("튜플 c :", c)
print("튜플 d :", d)
print("튜플 e :", e)

print("d의 타입? :", type(d))
print()

a= 1, 2, 3, 4
# a[0] = 5 # 값 변경 시도 시 오류
# a[0] = () # 마찬가지로 오류
# del(a[0]) # 오류
# a.remove(1) # 당연히 오류 # 튜플에게는 remove가 없다
print(a[0]) # 인덱싱
print(a[0:2]) # 슬라이싱

a = 1,2,3
b = 4,5,6
c = a+b # --> 1,2,3,4,5,6 을 새로 만들었다.
print("튜플 더하기:", c)
print("튜플 곱하기:", c*2) # 이 시점에 새로운 튜플 생성됨
print()





























