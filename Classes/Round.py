import Constants

class Round:
    def __init__(self, name) -> None:
        self.roundName = name
        self.matchDict = dict()

    def addMatchToRound(self, match):
        self.matchDict[match.id] = match
        return True

    def matchesInitialised(self) -> bool:
        if (len(self.matchDict.keys()) > 0):
            return True
        return False

    def printRound(self):
        print(self.roundName)
        print(Constants.LINE)
        
        for match in self.matchDict.values():
            match.printMatch()
        print(Constants.SPACER)

