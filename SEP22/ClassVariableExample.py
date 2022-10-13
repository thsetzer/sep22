class Person:
    
    instanceCounter=0 

    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.instanceCounter+=1
        
def myfunc(abc):
    print("Hello my name is "+ abc.name)
        
p1 = Person("John", 36)
myfunc(p1)
print("The number of persons is: ", p1.instanceCounter)
p2 = Person("Adam", 81)
print("The number of persons is: ", p1.instanceCounter)
print("The number of persons is: ", Person.instanceCounter)
