from socket import SOL_UDP
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd;


matches = []
driver = webdriver.Chrome(executable_path='C:/Users/Ethar/Documents/Programming_Projects/Python/RugScrape/chromedriver.exe')

driver.get("https://www.premiershiprugby.com/gallagher-premiership-rugby/fixtures-results/")

content = driver.page_source

soup = BeautifulSoup(content, "html.parser")

matches = soup.find_all('div', class_= "Content_StatsRugbyMDS")
matches = soup.find_all('div', class_= "fixtures__block *")

# matches = soup.select('div[class*="fixtures__block"]')
matchContainer = soup.select('div[class*="fixtures__teams"]')
# hometeam = match
# dateOfMatch = soup.select


print(matchContainer[0].contents)
print(matches)