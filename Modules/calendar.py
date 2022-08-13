# The code library to be used for all calendar operations
import Modules
import json
import Resources
from icalendar import vCalAddress, Calendar, Event

""""
By providing a match an ical can be created
"""
def createIcal(match):
    cal = Calendar()
    cal.add('prodid', '-//created by RugScrape.py//')
    cal.add('version', '1.0')

    matchEvent = Event()
    matchEvent.add('dtstart', match.dateTime)
    matchEvent.add('location', match.location)
    matchEvent.add('summary', match.homeTeam + ' vs '  + match.awayTeam)

    with open('Resources/MailingList.json') as json_file:
        mailingList = json.load(json_file)
    for user in mailingList:
        matchEvent.add('attendee', user["email"])
    print(matchEvent)
    cal.add_component(matchEvent)
    Modules.filesystem.writeCalendarToDisk(cal)

def readIcal():
    pass

# create a different version for sending a whole Season, Round, Match
def sendIcals():
    pass

def sendIcalsByTeam():
    pass