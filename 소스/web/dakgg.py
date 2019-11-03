from selenium import webdriver
from bs4 import BeautifulSoup

def get_status(mode_name, summary) :
    class_value = mode_name + " modeItem"
    mode = summary.find("section", {"class":class_value})
    data = []
    if mode.find("div", {"class":"mode-section tpp no_record"}) :
        data.append( "기록없음" )
    else :
        tpp = mode.find("div", {"class": "mode-section tpp"})

        grade = tpp.find("p", {"class":"grade-name"}).text.strip()
        rating = tpp.find("div", {"class":"rating"}).find("span", {"class":"value"}).text.strip()
        top = tpp.find("span", {"class":"top"}).text.strip()
        data.append( [grade, rating, top] )

    return data

def print_status(mode_name, data):
    if data[0] == "기록없음":
        print("{} 모드 : {}".format(mode_name, data[0]))
        return

    for i in data:
        print("[{} 모드 기록]".format(mode_name))
        print("등급 :", i[0])
        print("점수 :", i[1])
        print("백분율 :", i[2])


# 크롬브라우저 실행! chromedriver.exe 경로
driver = webdriver.Chrome()

# PhantomJS --> warning 뜨지만 되긴 됨
# driver = webdriver.PhantomJS()

# 사이트 이동
driver.get("https://dak.gg/?hl=ko-KR")

print( driver.title )


e_name = driver.find_element_by_name("name")
e_name.send_keys("soo_chang")
e_name.submit()

bs = BeautifulSoup( driver.page_source.encode("utf-8","ignore"), "html.parser")
summary = bs.find("div", {"class":"modeSummary"})

total_data = []
data = get_status("solo", summary)
total_data.append(data)
data = get_status("duo", summary)
total_data.append(data)
data = get_status("squad", summary)
total_data.append(data)

print_status("솔로", total_data[0])
print_status("듀오", total_data[1])
print_status("스쿼드", total_data[2])

driver.close()
