import Projectile as P

def main():
    angle, vel, h0, time = P.getInputs()
    cball = P.Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time)
        print("\nDistance traveled: ", cball.getX(), " meters, hight is ", cball.getY())
#main()


import ProjectileWithDocs as PWD
help(PWD)