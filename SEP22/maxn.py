'''
Created on 01.10.2022

@author: thsetzer
'''

# maxn.py
#    Finds the maximum of a series of numbers
# maxn.py
#    Finds the maximum of a series of numbers
def main():
    #n = eval(input("How many numbers are there? "))
    listOfNumbers = [5,7,2,78,34,33]
    #n = listOfNumbers.__len__()
    n=  len(listOfNumbers)
    # Set max to be the first value
    ##maxNumber = eval(input("Enter a number >> "))
    maxNumber = listOfNumbers[0]
    # Now compare the n-1 successive values
    for i in range(n-1): 
        ##x = eval(input("Enter a number >> "))
        x = listOfNumbers[i]
        if x > maxNumber:
            maxNumber = x
    print("The largest value is", maxNumber)

main()