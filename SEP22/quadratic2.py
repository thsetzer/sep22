'''
Created on 01.10.2022

@author: thsetzer
'''

# quadratic2.py –A program that computes the real roots of a quadratic equation.
# Bad version using a simple if to avoid program crash
import math  
def main():
    print("This program finds the real solutions to a quadratic\n")
    a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
    discrim = b * b - 4 * a * c
    print("Discriminant is: ", discrim)
    if discrim >= 0:
        discRoot = math.sqrt(discrim)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    if discrim < 0:
        print("The equation  has  no  real roots!")
main()