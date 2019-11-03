'''
    [파일 입출력] - file input, output
            - 실제 파일을 생성/쓰기(편집)/읽기/삭제(파일)

            - 파일의 이해 (file)
               > 디렉토리 (directory)
                  폴더 또는 디렉토리라고 한다.
                  파일과 다른 디렉토리를 포함한다.
               > 파일 (file)
                 컴퓨터에서 정보를 저장하는 논리적인 단위(disk)
                 파일은 파일명과 확장자로 식별된다.(10_file_io.py)
                 실행, 쓰기, 읽기, 삭제 등을 할 수 있다.

               기본적으로 '모든 파일'은 메모장으로 열 수 있으며,
               우리가 파이썬으로 파일을 다룰 때도, 메모장으로 열어서
               편집하는 것과 같은 의미.
                 1. 메모장으로 파이썬 소스 파일 연다
                 2. 소스 수정
                 3. 해당 소스 파일을 실행시킨다. --> 이 파이썬의 편집기가 한번에 해준다

              Binary 파일
                   특정 프로그램으로 열어야 알아볼 수 있는 파일
                   메모장으로 열면 깨져서 보인다.
                   엑셀(xlsx), 위드(docx), 한글(hwp) 등...
              Text 파일
                   메모장으로 열었을 때 알아볼 수 있는 파일 (txt,py,html)

            우리가 프로그램으로 다룰 파일 : Text 파일
                > Binary 파일들은 각자 프로그램들이 Text 형태로 읽어서 변환해서 사용
                
[사용법]
파일객체(변수) = open("파일이름", "파일열기모드")
       파일객체 : 변수와 비슷한 의미
       파일이름 : 이 컴퓨터에 존재하는 파일명 (절대경로/상대경로)
       파일열기모드
           r : 읽기모드(read) -> 파일 내용을 읽기만 가능
           w : 쓰기모드(write) -> 파일 내용 쓸때
           a : 추가모드(add) -> 파일 내용 마지막에 내용을 추가할 때


'''
# 파일 읽기
# 파일의 경로를 나타낼 때 폴더는 \로 구분한다.
# 맨 앞에는 드라이브문자:\ <-- windows에서의 절대경로 시작
# C:\최성현\python\소스
print("파일 읽기 시작!")
'''
file = open("C:\\20180227_test.txt","r")
txt = file.read()  # read() : 파일 전체 내용을 '문자열'로 반환
print(txt)
file.close() # 위에서 open한 파일을 닫는다.
# open한 파일을 닫지 않으면, 계속 사용 중이어서 편집 불가
'''

# with 를 이용하여 close() 생략하기
'''
with open("C:\\20180227_test.txt","r") as file :
    txt = file.read()  # read() : 파일 전체 내용을 '문자열'로 반환
    print(txt)
    '''
# with 문이 끝나면 자동으로 close가 된다.

'''
# 파일 내용을 한 줄 씩 읽기 (1)
with open("C:\\20180227_test.txt","r") as file :
    txt = file.readlines() # 리스트 형태로 한 줄씩 반환(\n 개행)
    print(type(txt))
    print(len(txt)) # 리스트의 요소 개수 반환 (몇 줄인지 확인)
    print(txt)
'''

'''
# 파일 내용을 한 줄 씩 읽기 (2)
with open("C:\\20180227_test.txt","r") as file :
    while True : # 무한반복! --> 수행문 안에 break 필요
         txt = file.readline() # 한 줄을 읽어온다.

         if not txt :
             break # while문 탈출!
         # readlines()에서 본 것처럼, 각 요소에 \n가 포함!
         # print() 에서 또 개행을 했다. (end = "\n")
         print(txt) # print(txt,end = "\n") 개행 없앰
'''
# 1) readline()을 반복해서 수행할 때마다, 알아서
#    읽고 난 다음 위치를 읽는다.
# 2) 다음 읽은 내용이 없을 때 txt는 비어있다.  "" <-- False

# 파일 내용에서 단어, 라인 통계 산출

with open("C:\\20180227_test.txt","r") as file :
    txt = file.read() # 전체 내용 읽기
    word_list = txt.split(" ") # 공백으로 나누겠다.
    line_list = txt.split("\n") # 개행 기준으로 라인!
    # split()  --> 공백,개행,탭문자 등 띄어쓴것을 다 나눈다.
    
# print("word_list : ",word_list)
# print("line_list : ",line_list)
print("단어 개수 : " , len(word_list))
print("라인 개수 : " , len(line_list))
print("전체 글자 수 : ", len(txt)) # 전체 문자열의 요소 개수

print("="*20)
# len() : 요소의 개수를 반환해주는 함수
#      리스트 : [1,2,3] --> 3 반환, ["ABC","A","1"] --> 3반환
#      문자열 : "12345" --> 5 반환
#           for i in "12345" : --> i에는 12345에서 한 문자씩 대입이 되면서 반복되는 for문
'''
# 만약 읽어온 파일에서 문자열이 비어있는 줄을 제외시키고 싶다!
line_list.remove("") # <-- 리스트 요소 중 "" 이 값을 지우겠다.
# 처음으로 찾은 일치하는 요소를 지운다!!
print("라인 개수 : " , len(line_list))

# 전체를 다 지우고 싶다
#   1) 반복문 사용 find("") 있으면 삭제!
#   2) "" <-- 빈 문자열의 개수를 구해서  

count = line_list.count("") # <-- 일치하는 개수 반환
num = 0
while num < count :
    line_list.remove("")
    num += 1
print("라인 개수 : " , len(line_list))
'''
# 읽은 파일객체를 for문에 대입
'''
with open("C:\\20180227_test.txt","r") as file :
    for line in file : # 줄 단위로 대입 된다. (readline처럼)
        print(line,end="")
'''

# 파일 쓰기
# 파일을 쓰기모드로 열 때, 파일이 이미 존재하면 지우고 새로 만든다.
'''
with open("C:\\20180227_test2.txt","w") as file :
    for i in range(1,11) : # 1 ~ 10까지 i에 대입되면서 반복
        txt = "(수정) {}번째 줄입니다.\n".format(i)
        file.write(txt) # 문자열을 쓰기
        # 1) 한 번 쓰면, 알아서 마지막 쓴 위치에 이어 쓴다.
        # 2) 자동으로 개행이 되지는 않는다.
'''

'''
str_list = ["1\n","2\n","3\n"]
str_list2 = ["1","2","3"]
with open("C:\\20180227_test3.txt","w") as file :
    #file.writelines(str_list) # 리스트의 문자열 쓰기
    file.writelines(str_list2) # 리스트의 문자열 쓰기
    # readlines 로 읽은 내용을 writelines 로 쓰면
    # 파일 내용이 그대로 복사가 된다. (read, write가 짝인것 처럼)
'''
with open("C:\\python_exam.txt","r") as file :
    txt = file.readline()
# 파일 입출력 연습
'''
     파일을 읽어서 아래 정보를 출력하기
     파일명(절대경로) C:\\python_exam.txt
     [출력결과]
     전체 글자수 : ??
     전체 단어수 : ??
     전체 라인수 : ??
     '사랑' 단어 수 : ??
     
'''
# 전체 내용을 읽어서 처리
'''
with open("C:\\python_exam.txt","r") as file :
    txt = file.read()
    word_list = txt.split()
    line_list = txt.split("\n")
    print("전체 글자수 : " , len(txt))
    print("전체 단어수 : " , len(word_list))
    print("전체 라인수 : " , len(line_list))
    count = txt.count("사랑")
    print("\'사랑\' 단어수 : " , count)
'''
# 한 줄 씩 처리
line_count = 0
love_count = 0
word_count = 0
total_count = 0
with open("C:\\python_exam.txt","r") as file:
    for line in file :
        line_count += 1
        love_count += line.count("사랑")
        word_count += len(line.split(" "))
        total_count += len(line)
print("전체 글자수 : " , total_count)
print("전체 단어수 : " , word_count)
print("전체 라인수 : " , line_count)
print("\'사랑\' 단어수 : " , love_count)
while True :
    input_str = input("검색할 단어 입력(0 입력 시 종료) : ")
    if input_str == "0" :
        break
    else :
        count = txt.count(input_str)
    print( "{} 단어는 {}개 입니다.".format(input_str, count) )        


  














