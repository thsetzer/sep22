from Dice import Dice
#from PokerApp import PokerApp
from textinter import TextInterface

class PokerApp:
    def __init__(self, inter):
        self.dice = Dice()
        self.money = 100
        self.interface = inter
        
    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()
    
    def playRound(self):
        self.money = self.money -10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)        
    
    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()    
          
def main():
    inter = TextInterface()
    app = PokerApp(inter)
    app.run()
    
main()