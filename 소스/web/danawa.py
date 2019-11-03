# danawa.py

'''
    우리가 requests로 get을 해서 얻어오는 페이지 정보는
    브라우저에서 소스보기 했을 때의 정보라고 보면 된다. (단순한 페이지의 소스)

    페이지 소스 보기로 보이는 정보가 있고,
    브라우저로 페이지를 열어야만 정보가 보이는 것이 있다.
    (해당 페이지를 브라우저가 해석한 것을 F12 키 눌러서 볼 수 있다.)

pip install selenium
'''

# 프로그램 기능 : 다나와 노트북 제품정보 페이지에서 제품명,가격,상세스펙,순위 를 가공
#                1페이지부터 지정한 페이지까지 이동하면서 반복


from selenium import webdriver
from bs4 import BeautifulSoup
import time # 시간 관련 모듈

# Chrome 클래스의 인스턴스 생성 = chromedriver.exe 가 구동 (크롬브라우저 실행)
driver = webdriver.Chrome()

# get() : 해당 URL로 이동시킨다.
driver.get("http://prod.danawa.com/list/?cate=112758")

# 빈 리스트 만들기
data = []

page_count = 4

for page in range(1, page_count+1) : #1만 수행
    if page != 1 : # 1페이지 일 때는 그냥 수행! (두 번째 수행부터 페이지 이동!)
        driver.execute_script( "movePage({})".format(page) ) # movePage(2) 를 수행
        time.sleep(1) # 페이지를 이동시키고 1초간 대기! (이동되는 시간 고려)

    # 파싱을 BeautifulSoup로 했었다. driver 즉, 브라우저의 페이지정보를 가져와야한다.
    bs = BeautifulSoup( driver.page_source.encode("utf-8","ignore"), "html.parser")

    # bs 에는 해당 페이지의 모든 정보가 들어있다!!

    # <div id="productListArea"> 만 가져오기
    area = bs.find( "div", {"id":"productListArea"} )

    # <div class="prod_main_info"> 가 하나의 제품이기 때문에,
    # 모든 것을 리스트화해서 하나씩 info에 담겠다.
    for info in area.find_all("div", {"class":"prod_main_info"}) :
        # info 에는 제품 하나에 대한 정보가 들어있다.

        # 1) 제품명
        # <a class="prod_name"> 의 텍스트
        name = "제목없음"
        if info.find( "a", {"class":"prod_name"} )  :
            name = info.find( "a", {"class":"prod_name"} ).text.strip()
        elif info.find( "a", {"name":"productName"} ) : # 대소문자
            name = info.find( "a", {"name":"productName"} ).text.strip()
          
        # 2) 가격 (스펙별로 가격이 다를 수 있다 = 1개가 아닐 수 있다.)
        count = 0
        price = ""
        for price_list in info.find_all( "p", {"class","price_sect"} ) :
            if count != 0 :
                price += " / "

            # 가격은 price_sect 아래 있는데 여러 개 일 경우 price_sect가 많다.
            # 하나씩 빼서 text를 가져오고 앞에 가격에 / 를 붙여서 잇는다.
            price = price + price_list.text.strip().replace(",", "")
            
            count += 1
        
        # 3) 스펙
        # <div class="spec_list"> 의 모든 text를 사용
        spec = "스펙없음"
        if info.find( "div", {"class":"spec_list"} ) : # 실제 반환이 True가 아닌데..
            spec = info.find( "div", {"class":"spec_list"} ).text.strip().replace(",", "")
        elif info.find( "li", {"class":"spec_item"} )  :
            spec = info.find( "li", {"class":"spec_item"} ).text.strip().replace(",", "")
        
        # 4) 순위
        # <strong class="pop_rank"> 의 text인데, 광고 상품이나 2페이지부턴 순위가 없다.
        rank = "순위없음"
        if info.find("strong", {"class":"pop_rank"}) : # 없는 걸 대비
            rank = info.find("strong", {"class":"pop_rank"}).text.strip()

        # 완성된 내용들 리스트에 넣기
        data.append( [page, rank, name, price, spec] ) # 페이지,순위,이름,가격,스펙
        #print("===========================")
        #print( "제품명 :", name )
        #print( "가격 :", price )
        #print( "상세스펙 :", spec )
        #print( "순위 :", rank )

# 브라우저 종료
driver.close()

# 읽은 내용을 파일로 저장하기
with open("danawa_notebook.csv", "w") as file :
    # csv파일은 comma seperated value (콤마(,)로 구분된 값을 가진 파일)
    # csv는 엑셀에서 콤마 기준으로 한 셀씩 자동 분리해서 보여준다.

    # 페이지,순위,이름,가격,스펙
    file.write("page,rank,name,price,spec\n") # 첫 째 줄은 제목용도로 사용할 것

    for i in data :
        file.write( "{},{},{},{},{}\n".format( i[0], i[1], i[2], i[3], i[4] ) )





