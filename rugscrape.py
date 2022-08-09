from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd;


from Classes import Match, Round
from Modules import calendar, filesystem


matches = []
driver = webdriver.Chrome(executable_path='C:/Users/Ethar/Documents/Programming_Projects/Python/RugScrape/chromedriver.exe')

driver.get("https://www.premiershiprugby.com/gallagher-premiership-rugby/fixtures-results/")

content = driver.page_source

soup = BeautifulSoup(content, "html.parser")

#Selects each mach
matchContainer = soup.select('div[class*="fixtures__teams"]')


for x in matchContainer :
    homeTeam = x.find('div', attrs={"itemprop" : "homeTeam"}).text.strip()
    awayTeam = x.find('div', attrs={"itemprop" : "awayTeam"}).text.strip()

    dateTime = x.find('meta', attrs={"itemprop" : "startDate"}).attrs["content"]

    round = x.find_all_previous('div', class_="fixtures__heading")[0]
    location = x.parent.find('span',class_ = "fixtures__venue").text.strip()

    broadcaster = False
    try:
         broadcaster = x.parent.find('span', class_="fixtures__broadcaster")
    finally:
        current = Match.Match(homeTeam, awayTeam, dateTime, location, broadcaster)
        current.printMatch()

    

driver.close