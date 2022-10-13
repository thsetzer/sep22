'''
Created on 01.10.2022

@author: thsetzer
'''

# quadratic6.py
import math 

def main():
    print("This program finds the real solutions to a quadratic\n")
    try:
        a, b, c = eval(input("Please enter the coefficients (a, b, c): "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2 )
    except ValueError as excObj:
        print(excObj.__doc__)
        if str(excObj) == "math domain error":
            print("No Real Roots")
        else:
            print("You didn't give me the right number of coefficients.")
    except NameError as myNameError:
        print("\nYou didn't enter three numbers.")
        
        print("The problem was: ", myNameError.__dict__)        
    except TypeError:
        print("\nYour inputs were not all numbers.")
    except SyntaxError:
        print("\nYour input was not in the correct form. Missing comma?")
    except:
        print("\nSomething went wrong, sorry!")
main()
