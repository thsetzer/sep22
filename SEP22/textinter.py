#textinter.py
class TextInterface:
    def __init__(self):
        print("Welcome to video poker.")
  
    def setMoney(self, amt):
        print("You currently have $", amt)
  
    def setDice(self, values):
        print("Dice:", values)

    def wantToPlay(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in "yY"
    
    def close(self):
        print("\nThanks for playing!")
    
    def showResult(self, msg, score):
        print( msg,". ", "You win: ", score)
    
    def chooseDice(self):
        input_given = eval(input("Enter list [pos1, pos2] of which to change ([] to stop, 0 means first dice!)" )) 
        return input_given
    