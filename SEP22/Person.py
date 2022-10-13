'''
Created on 03.10.2022

@author: thsetzer
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
  
p1 =Person("John", 36)


def greeting(Name):
    print("Hello ", Name)
def greeting(Name, salutation):
    print("Hello ", salutation, " ", Name)

greeting("Thomas Setzer")
greeting("Thomas Setzer", “Mr.“)

