import Round

class Season:
    def __init__(self, name, round) -> None:
        self.name = name
        self.roundsDict = {
            "roundNumber" : round.number,
            "roundObj" : round
        }