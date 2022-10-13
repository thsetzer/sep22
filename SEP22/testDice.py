from Dice import Dice
d = Dice()
d.values()
# [4, 4, 4, 2, 5]
d.score()
# ('Three of a Kind', 8)
d.rollAll()
d.values()
# [1, 4, 2, 6, 6]
d.score()
# ('Garbage', 0)
d.roll([0]) # positions = dice no. -1
d.values()
# [6, 4, 2, 6, 6]
d.score()
# ('Three of a Kind', 8)
