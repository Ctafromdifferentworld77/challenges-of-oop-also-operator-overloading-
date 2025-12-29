'''
operator overloading is the concept of OOP. Operator Overloading allows operators to work with objects
'''
#imagine two players in a game, each player has a score. we want to use + add their score
class player:
    def __init__(self, score):
        self.score=score
    def __add__(self, other):
        return player(self.score+other.score)
    def __lt__(self, other):
        return player(self.score < other.score)
    def __eq__ (self, other):
        return player(self.score == other.score)
    def show_score(self):
        print("total score: ", self.score)
thanish=player(50)
tharaa=player(30)
total_score=thanish+tharaa
total_score.show_score()
print(tharaa<thanish)
