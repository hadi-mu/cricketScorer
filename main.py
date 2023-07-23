class game(object):
    def __init__(self,team1,team2):
        self.firstTeam=team1
        self.secondTeam=team2

    def toss():
        pass

    def checkInningsOver():
        pass

    def innings():
        pass

    def over():
        pass

    def ball():
        pass

    def displayInfo(self):
        print(self.firstTeam.names)
        

class team(object):
    def __init__(self):
        self.names=self.getNames()
        self.score=0
        self.batsmanScores={}
        self.bowlerFigures={}


    def getNames():
        names=[]
        for i in range(11):
            names.append(input("Enter players name:"))
        return names
    

first=team()
second=team()
match=game(first,second)
print(match.firstTeam.names)