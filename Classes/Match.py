from ast import Str
from datetime import datetime;

class Match:
    def __init__(self, home, away, dateTime, location, broadcaster) -> None:
        #Regular strings handled
        self.homeTeam = home
        self.awayTeam = away
        self.location = location

        # Takes the time object provided and converts into a datetime object
        self.dateTime = datetime.strptime(dateTime, '%Y%m%dT%H%M%SZ')
        
        # if the broadcaster feild is not false then it will be set to the img title, else "TBC"
        self.broadcaster = broadcaster.img.attrs["title"] if (broadcaster) else "TBC" 


    def getDate(self) -> datetime:
        return self.dateTime

    def getDateAsString(self) -> Str:
        return self.dateTime.strftime('%H:%M on %d %b')

    def printMatch(self):
        print(self.homeTeam + " vs " + self.awayTeam + " at " + self.getDateAsString() + " "+ self.location + " Broadcaster: " + self.broadcaster) #broadcaster
