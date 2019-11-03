from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
data = ["epl","primera","bundesliga","seria","ligue1","eredivisie"]
rank=""
name=""
team=""
score=""
for i in range(0,6) :
  driver.get("http://sports.news.naver.com/wfootball/record/index.nhn?category={}&tab=player".format(data[i]))
  bs = BeautifulSoup(driver.page_source.encode("utf-8","ignore"),"html.parser")
  area = bs.find("ul",{"class":"lead_inner"})
  print("*"*20)
  print(data[i])
  for a in area.find_all("li") :
    title =""
    title = a.find("strong",{"class":"lead_title"}).text.strip()
    print(title)
    for b in a.find_all("div",{"class":"text"}):
      rank = b.find("b",{"class":"rank_num"}).text.strip()
      name = b.find("span",{"class":"name"}).text.strip()
      team = b.find("span",{"class":"team"}).text.strip()
      score = b.find("div",{"class":"stat"}).text.strip()
      print(rank,name,team,score)

  
