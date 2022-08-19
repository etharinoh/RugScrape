# The code library to be used for all calendar operations
from Modules import filesystem
import json
import Resources
from icalendar import vCalAddress, Calendar, Event
import datetime
import pytz

calendarDict = dict

""""
By providing a match an ical can be created
"""
def createMatchIcal(match):
    cal = Calendar()
    cal.add('prodid', '-//created by RugScrape.py//')
    cal.add('version', '1.0')

    matchEvent = createEvent(match)
    
    cal.add_component(matchEvent)
    filesystem.writeCalendarToDisk(cal, match)

def createSeasonCalendar(season) -> Calendar:
    seasonCal = createCalendarRequirements()

    for round in season.roundsDict.values():
        for match in round.matchDict.values():
            matchEvent = createEvent(match)
            seasonCal.add_component(matchEvent)
    
    filesystem.writeCalendarToDisk(seasonCal, match)
    

def createTeamCalendar(team) -> Calendar:
    teamCal = createCalendarRequirements()

    for match in team.getMatches():
        matchEvent = createEvent(match)
        teamCal.add_component(matchEvent)

    filesystem.writeCalendarToDisk(teamCal, match)

def createCalendarRequirements() -> Calendar:
    cal = Calendar()
    cal.add('prodid', '-//created by RugScrape.py//')
    cal.add('version', '1.0')

    return cal

def createEvent(match) -> Event:
    matchEvent = Event()
    # name desc, location
    matchEvent.add('location', match.location)
    matchEvent.add('summary', match.homeTeam + ' vs '  + match.awayTeam)
    matchEvent.add('description', match.homeTeam + ' vs '  + match.awayTeam) #This is the body of the email, whre extra info needs putting


    # event timings
    endTime = match.dateTime + datetime.timedelta(hours=2)
    matchEvent.add('dtstart', match.dateTime)
    matchEvent.add('dtend', endTime)

    with open('Resources/MailingList.json') as json_file:
        mailingList = json.load(json_file)
    for user in mailingList:
        matchEvent.add('attendee', user["email"])
    
    return matchEvent

def readIcal():
    pass

# create a different version for sending a whole Season, Round, Match
def sendIcals():
    pass

