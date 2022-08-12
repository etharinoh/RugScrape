from hashlib import new
from .Team import Team
import Resources.Constants as Constants
import Modules.filesystem as filesystem
from .Round import Round


class Season:
    """
    Initialises an empty dictionary
    """
    def __init__(self, name) -> None:
        self.name = name
        self.roundsDict = dict()
        filesystem.createFolder(Constants.SEASONS_FOLDER, name, [])
        self.teams = dict()

    """
    @TODO Chage to add multiple inits
    
    Initilises a season with a provided round
    """ 
    # def __init__(self, name, round) -> None:
    #     self.name = name
    #     self.roundsDict = {
    #         round.number : round
    #     }

    def getRound(self, roundName) -> any:
        if(roundName):
            found = self.roundsDict.get(roundName)
            if found:
                return found
        print(round + ' not found in season: '+ self.name)
        return False
    """
    Adds one round to a season
    """
    def addRoundToSeason(self, round):
        self.roundsDict[round.roundName] = round

    """
    Adds an array of rounds into the season
    """
    def addRoundsToSeason(self, roundsArr):
        for round in roundsArr:
            self.roundsDict[round.number] = round
    
    """
    Adds a match to a provided round in the season

    round = the round to add to
    match = the match to add
    """
    def addMatchToSeason(self, round, match):
        self.roundsDict.get(round).addMatchToRound(match)

    """
    Checks to see if there are currently any rounds initilised within this season
    """
    def roundsInitilised(self) -> bool:
        if (len(self.roundsDict.keys()) > 0):
            return True
        return False

    """
    Iterates through the season to print each round
    """
    def printSeason(self):
        print(self.name)
        print(Constants.LINE)
        if (self.roundsInitilised()):
            for round in self.roundsDict.values():
                round.printRound()
        else:
            print("Currently no rounds initialised within this season")
        print(Constants.SPACER)


    def getTeam(self, teamName) -> Team:
        found = self.teams.get(teamName)
        if found:
            return found
        else:
            #make a new team
            newTeam = Team(teamName)
            self.addTeamToSeason(newTeam)
            return newTeam

        # exception
    def addTeamToSeason(self, Team):
        self.teams[Team.teamName] = Team

    def printTeams(self):
        if len(self.teams) > 1:
            print("No teams yet")
        else:
            print("Teams in: " + self.name)
            for team in self.teams:
                print(Constants.TAB + team + " url: "+ team.url)
    
        