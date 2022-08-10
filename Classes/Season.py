import Constants
class Season:
    """
    Initialises an empty dictionary
    """
    def __init__(self, name) -> None:
        self.name = name
        self.roundsDict = dict()

    """
    @TODO Chage to add multiple inits
    
    Initilises a season with a provided round
    """ 
    # def __init__(self, name, round) -> None:
    #     self.name = name
    #     self.roundsDict = {
    #         round.number : round
    #     }

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
        