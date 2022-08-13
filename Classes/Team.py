class Team:
    def __init__(self, name) -> None:
        self.teamName = name
        self.link = self.convertNameToLink()
        self.matchDict = dict()
    
    def addMatch(self, match):
        self.matchDict[match.dateTime.strftime('%y-%m-%d')] = match

    def convertNameToLink(self) -> str:
        link = ""
        splitName = self.teamName.lower().split()
        if len(splitName) > 1:
            link = splitName[0] + '-' + splitName[1]
        else:
            link = splitName[0]
        return link
        