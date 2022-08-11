from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd;

from Classes import Match, Round, Season
from Modules import calendar, filesystem
import Resources.Constants

def main():
    
    driver = webdriver.Chrome(executable_path='C:/Users/Ethar/Documents/Programming_Projects/Python/RugScrape/chromedriver.exe')

    driver.get("https://www.premiershiprugby.com/gallagher-premiership-rugby/fixtures-results/")

    content = driver.page_source

    soup = BeautifulSoup(content, "html.parser")

    #Create Season
    season = createNewSeason(soup)

    #Create Rounds
    allRounds = createRounds(soup, season)
    #Selects each mach
    matchContainer = soup.select('div[class*="fixtures__teams"]')



    for match in matchContainer :
        homeTeam = match.find('div', attrs={"itemprop" : "homeTeam"}).text.strip()
        awayTeam = match.find('div', attrs={"itemprop" : "awayTeam"}).text.strip()

        dateTime = match.find('meta', attrs={"itemprop" : "startDate"}).attrs["content"]

        round = match.find_all_previous('div', class_="fixtures__heading")[0].text.strip()
        location = match.parent.find('span',class_ = "fixtures__venue").text.strip()

        broadcaster = False
        try:
            broadcaster = match.parent.find('span', class_="fixtures__broadcaster")
        finally:
            currentMatch = Match.Match(homeTeam, awayTeam, dateTime, location, broadcaster)
            season.addMatchToSeason(round, currentMatch)
            # calendar.createIcal(currentMatch) # @TODO Removed untill filesystem is created


    season.printSeason()
    driver.close

def createRounds(soup, season):
    roundHeaders = soup.select('div[class*="fixtures__heading"]')
    for round in roundHeaders:
        currentRound = Round.Round(round.text.strip())
        season.addRoundToSeason(currentRound)


def createNewSeason(soup) -> Season:
    return Season.Season(soup.title.text)
    
if __name__ == "__main__":
    main()