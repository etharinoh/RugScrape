from Resources import Constants

class Round:
    def __init__(self, name, parent) -> None:
        self.roundName = name
        self.matchDict = dict()
        self.parent = parent

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

