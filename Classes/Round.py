from Classes import Match

# Constants
LINE = "=" *30
SPACER = "\n" *2

class Round:
    def __init__(self, number) -> None:
        self.roundNo = number
        self.matchArr = []

    def addMatchToRound(self, match):
        self.matchArr.append(match)
        return True

    def printRound(self):
        print(self.roundNo)
        print(LINE)
        
        for match in self.matchArr:
            match.printMatch()
        print(SPACER)

