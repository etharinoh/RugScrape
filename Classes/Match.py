from ast import Str
from datetime import datetime
from Resources import Constants

from .Season import Season;

class Match:
    def __init__(self, home, away, dateTime, location, broadcaster, parent) -> None:
        #Regular strings handled
        self.homeTeam = home
        self.awayTeam = away
        self.location = location

        # Takes the time object provided and converts into a datetime object
        self.dateTime = datetime.strptime(dateTime, '%Y%m%dT%H%M%SZ')
        
        # if the broadcaster feild is not false then it will be set to the img title, else "TBC"
        self.broadcaster = broadcaster.img.attrs["title"] if (broadcaster) else "TBC" 

        self.id = home + "," + away + "," + self.dateTime.strftime('%y%m%d%H%M')
        self.parent = parent

        season = self.getSeason()
        teamHome = season.getTeam(home)
        teamHome.addMatch(self)

        teamAway = season.getTeam(away)
        teamAway.addMatch(self)

        self.icalFilePath = Constants.SEASONS_FOLDER + season.name + '\\' + parent.roundName
        
    def getSeason(self) -> Season:
        return self.parent.parent


    def getDate(self) -> datetime:
        return self.dateTime

    def getDateAsString(self) -> Str:
        return self.dateTime.strftime('%H:%M on %d %b')

    def printMatch(self):
        print(self.homeTeam + " vs " + self.awayTeam + " at " + self.getDateAsString() + " "+ self.location + " Broadcaster: " + self.broadcaster) #broadcaster
