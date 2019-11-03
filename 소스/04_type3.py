'''
    [5. 딕셔너리(Dictionary) 자료형 ]
      - 사전
      - 형태 : { key1:value1, key2:value2, ... }
      - 순서가 없다.
         > 문자열 포매팅 / format() 에서 키워드와 비슷
          "{name}".format(name="한수창")

      주의사항
        1. key 는 중복되면 안 된다.
        2. key 에 리스트, 딕셔너리 사용 불가
           --> key   : 변하지 않는 값
           --> value : 아무거나  
'''
print("="*20)
print("{:^20}".format("5. Dictionary"))
print("="*20)

print("[딕셔너리 만들기]")
dict1 ={ "축구":"soccer", 2002:"한일",(1,2):("원","투"),"16강":[2002,2010]}
'''
    key     value
   ---------------
   "축구"   "soccer"      문자열 : 문자열
   2002     "한일"        숫자 : 문자열
   (1,2)    ("원","투")   튜플 : 튜플
   "16강"   [2002,2010]   문자열 : 리스트
'''

print(dict1)
print(dict1["축구"]) # 딕셔너리변수[key] --> 해당 value 반환
print(dict1[2002])
print(dict1[(1,2)])  # 이 결과가 ('원','투')
print(dict1[(1,2)][0]) # 위 반환된 튜플에서 0번 index요소를 가져온다.
print()

print("[딕셔너리 추가,삭제]")
dict2 = {1:"a"}
dict2[3] = "c"
dict2["하하"] = [1,2,3]
print(dict2)
# [] 안에 key가 들어가고, value를 대입
# 순서가 없는 딕셔너리는 key,value 쌍을 잘 맞추는 것이 중요

del(dict2["하하"]) # 지우고 싶은 key
print(dict2)
print()

print("[딕셔너리 관련 함수]")
my_dict = { "원": 1, "투":2 }

# keys() : key의 리스트만 모아서 반환
print("my_dict.keys() :",my_dict.keys())
print(list(my_dict.keys())) # list --> ()안에 내용을 리스트로 만들겠다.

my_str =",".join(list(my_dict.keys()))
print(my_str)

# values() : valued의 리스트만 모아서 반환
print("my_dict.values() :",my_dict.values())
print(list(my_dict.values()))

# items() : key, value 쌍으로 얻기
print(my_dict.items())
print(list(my_dict.items()))
print()


my_dict = { "원":1 , "투":2 }
# get() : key로 value 얻기 -> value 반환
print(my_dict.get("원"))
print(my_dict["투"])

print(my_dict.get("쓰리")) # get함수를 사용하면 없는 key일때 None 반환
# print(my_dict["포"]) # 없는 key일 때 오류 발생
print(my_dict.get("포",4)) # key가 없을 때 지정 값을 반환 받겠다.

# clear() : 모두 지우기
my_dict.clear() # 주체가 my_dict // 반환 없음
print(my_dict) # 딕셔너리 {} , 리스트[] , 튜플()

'''
    딕셔너리 연습하기
        my_dict 에서 "한국" 을 뽑아내기

my_dict = { "한국":"Korea", "일본":"Japan", "중국":"China"}
'''
#여기에 코드 작성
my_dict = { "한국":"Korea", "일본":"Japan", "중국":"China"}
korea = my_dict.pop("한국")

print(my_dict) #{'일본':'Japan','중국':'china'}
print(korea) # Korea

print()

'''
    [6. 집합(set) 자료형]
        - 순서가 없다. (딕셔너리처럼 인덱싱 불가능)
        - 중복이 허용되지 않는다. (중복제거 용도 사용)
'''
print("="*20)
print("{:^20}".format("6. Set"))
print("="*20)

print("[집합 만들기]")
my_set1 = set([1,7,2,3,5,3,2,1,2,3,7,5,3,1,3])
# 딕셔너리에서 key 가져올때 list()
print(my_set1)

my_set2 = set("hello")
print(my_set2)

my_set3 = {1,1,2,"hello","hello"}
print(my_set3)
print("my_set3의 type :", type(my_set3))
# ( )   : 튜플
# [ ]   : 리스트
# {k:v} : 딕셔너리
# { }   : 집합
# " "   : 문자열

# 집합에서 특정 값을 가져오고 싶을 때
# 리스트나 튜플로 변환해서 '인덱싱'한다.
my_list1 = list(my_set1)
print("리스트로 변환됨 :", my_list1)
print(my_list1[2])

my_tuple1 = tuple(my_set1)
print("튜플로 변환됨 :", my_tuple1)
print(my_tuple1[2])
print()

print("[집합의 활용]")
my_set1 = {1,2,3,4,5}
my_set2 = {4,5,6,7,8}

# 교집합 : 두 집합에 모두 있는 공통 요소
print( my_set1 & my_set2)
print( my_set1.intersection(my_set2))
# my_set1이 주체가 된다.
# 둘 다 교집합을 구한다!

# 합집합 : 두 집합에 모든 요소를 합친다.
print(my_set1 | my_set2)
print(my_set1.union(my_set2))
      
# 차집합 : A-B ---> A에서 B에 있는 요소 제거
print(my_set1 - my_set2)
print(my_set1.difference(my_set2))

# my_set1이 주체가 되어서 my_set2에 존재하는 요소가 제거
print()


# add(): 값 1 개 추가하기
my_set1 = {1,2,3}
my_set1.add(4)
my_set1.add(4)
print(my_set1)

# update() : 값 여러개 추가하기
my_set1.update([5,5,6,7])
print(my_set1)

# remove() : 특정 값 제거하기
my_set1.remove(5)
print(my_set1)

# my_set1.remove(10) # 없는 값 제거 시 오류!
print()

'''
    [7. Bool 자료형]
        참(True)과 거짓(False)을 판별해주는 자료형

        ======================
        값    True/False
        ======================
        1      True
        0      False
        "12"   True
        ""     False
        [1,2]  True
        []     False
        ()     False
        {}     False
        None   False
        ======================
        거짓(False)가 되는경우
          1. 값(요소)이 비어있다.
           > 문자열, 리스트, 튜플 등
          2. 숫자가 0이다.
          3. None : 값이 없다는 자료형!
'''
# True False None # 실제로 파이썬에서 쓰는 예약어
# 대소문자 다르면 안된다!!!!!
print( bool(1) )# bool() 안에 있는 값이 True/False 반환
print( bool(0) )
a = bool([]) # 빈 리스트 = False
print(a) # 여기서 출력되는 내용은 Bool 자료형의 값
print( type(a)) 

print(bool(True)) # True를 넣으면 True! (당연)






















