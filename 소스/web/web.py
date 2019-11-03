# web.py

'''
    웹크롤링
        인터넷 페이지에서 데이터를 가져와 가공하는 것

        > 파싱(parsing)
          특정 데이터에서 내가 원하는 데이터를 추출하는 것
            (특정 패턴이나 순서)

    크롤링을 하려면 대상 페이지의 선행분석이 필수!
      > 페이지마다 구조가 다 다르다.
      > 여기서의 구조란. 그 페이지 만든 개발자마음
      
    파이썬에서의 크롤링
      1. requests 모듈 활용 : html에 모든 데이터가 담겨 있는 페이지
      2. selenium 모듈 활용 : 데이터가 숨겨져 있는 동적페이지일 때 사용


    requests 모듈
      HTTP 요청 처리를 위한 모듈 (통신)
      별도 설치가 필요 (파이썬 설치 시 제공되는 기본 모듈이 아님)

    beautifulsoup4 모듈
      읽어온 HTML 코드를 쉽게 파싱하기 위한 모듈

cmd 창을 열고
pip install requests
pip install beautifulsoup4
'''

import requests as r
from bs4 import BeautifulSoup

# 웹페이지의 데이터 가져오기

#response = r.get("http://www.danawa.com")
# 이렇게 get을 했을때 정보를 가져오지 못하는 페이지들이 있다.
#   IE나 크롬 등이 특정 페이지를 접속할때 나의 브라우저 정보를 함께 보내면서 페이지요청
# 우리도 가짜 브라우저 정보를 함께 보내면서 페이지를 요청해야 한다.

my_headers = {"User-agent" : "Mozilla/5.0"}
response = r.get("http://www.danawa.com", headers=my_headers)

# 가져온 데이터를 BeautifulSoup의 객체(인스턴스)로 만들기 (변환)
soup = BeautifulSoup( response.content, "html.parser" )

# 자료를 제대로 가져왔는지 확인!!
#print( soup ) # html 형태로 만들어진다.

# <div class="main_middle_content"  인 것을 찾아서 main 변수가 사용
main = soup.find( "div", {"class" : "main_middle_content"} )
# my_dict = { "key1":"value1", "key2":"value2" }
#print( main )

# 각각의 정보를 저장할 빈리스트 생성
data = []
product_index = 0

# <ul> 태그만 모두 찾아서 리스트화 하겠다.
for ul in main.find_all("ul") :
    #ul은 각각 하나의 <ul> 태그 내용들이 들어있다. (4개의 <ul> 태그 -> 4번 반복)

    for li in ul.find_all("li") :
        # li는 하나의 <ul>태그 안에서 8개의 <li> 태그를 하나씩 반복한다.
        # <li> 태그 안에 하나의 제품 정보가 들어있다!! (제품명, 가격)

        #print( li.text.strip().replace("\n", " ") ) # <li> 태그 안의 text를 사용하겠다!
        product_index += 1
        product = li.text.strip().replace("\n", " ").replace(",", "")
        data.append( [product_index, product] )

# for문이 모두 수행되면 data 리스트에는 제품 정보들이 들어있다!!

# 읽은 내용을 파일로 저장하기
with open("danawa.csv", "w") as file :
    # csv파일은 comma seperated value (콤마(,)로 구분된 값을 가진 파일)
    # csv는 엑셀에서 콤마 기준으로 한 셀씩 자동 분리해서 보여준다.

    file.write("index,product\n") # 첫 째 줄은 제목용도로 사용할 것

    for i in data :
        file.write( "{},{}\n".format( i[0], i[1] ) ) # 한 줄에 제품 하나씩










