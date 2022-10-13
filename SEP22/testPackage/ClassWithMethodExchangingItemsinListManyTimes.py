'''
Created on 30.09.2022

@author: thsetzer
'''

class Exchanger:
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        
    def exchange (self, myList, howOften):
        for iteration in range(howOften):
            myList[1], myList[0] = myList[0], myList[1] 
            print("iteration nr", iteration)
            
            
            