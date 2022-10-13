
from math import pi, sin, cos
class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 0.0
        self.ypos = height
        theta = pi * angle / 180.0
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1
    def getY(self):
        return self.ypos
    def getX(self):
        return self.xpos
def getInputs():
    a  = eval(input("Enter launch angle (in degrees): "))
    v =  eval(input("Enter initial velocity (in meters/sec): "))  
    h  = eval(input("Enter initial height (in meters):  "))
    t = eval(input("Enter time interval between position calculations: "))  
    return a,v,h,t

# def main():
#     angle, vel, h0, time = getInputs()
#     cball = Projectile(angle, vel, h0)
#     while cball.getY() >= 0:
#         cball.update(time)
#         print("\nDistance traveled: ", cball.getX(), " meters, hight is ", cball.getY())
# main()