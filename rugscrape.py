from lib2to3.pytree import convert
from socket import SOL_UDP
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime;
import pandas as pd;


matches = []
driver = webdriver.Chrome(executable_path='C:/Users/Ethar/Documents/Programming_Projects/Python/RugScrape/chromedriver.exe')

driver.get("https://www.premiershiprugby.com/gallagher-premiership-rugby/fixtures-results/")

content = driver.page_source

soup = BeautifulSoup(content, "html.parser")

#Selects each mach
matchContainer = soup.select('div[class*="fixtures__teams"]')


for x in matchContainer :
    homeTeam = x.find('div', attrs={"itemprop" : "homeTeam"})
    awayTeam = x.find('div', attrs={"itemprop" : "awayTeam"})

    dateTime = x.find('meta', attrs={"itemprop" : "startDate"}).attrs["content"]
    dateTime = datetime.strptime(dateTime, '%Y%m%dT%H%M%SZ')
    dateTimeConvert = dateTime.strftime('%H:%M on %d %b')

    round = x.find_all_previous('div', class_="fixtures__heading")[0]
    location = x.parent.find('span',class_ = "fixtures__venue").text.strip()
    # broadcaster = x.parent.find('span', class_="fixtures__broadcaster").img.title.strip()
    print(homeTeam.text.strip() + " vs " + awayTeam.text.strip() + " is in " + round.text.strip() + " at " + dateTimeConvert + " at "+ location) #broadcaster

driver.close