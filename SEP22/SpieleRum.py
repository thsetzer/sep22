def makeSomethingFunny (x, y, z = 0):
    if (z==0): 
        return(x**y)    
    else:
        return(x+y+z)
print(makeSomethingFunny(2, 3))
print(makeSomethingFunny(2, 3, 4))

print(makeSomethingFunny(x=2, y=3))
print(makeSomethingFunny(y=3, x=2))



class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("I am a cat. My name is", self.name, ". I am", self.age, " years old.")
    def make_sound(self):
        print("Meow")
        
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print("I am a dog. My name is", self.name, ". I am", self.age, " years old.")     
    def make_sound(self):
        print("Bark")
        
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    
    


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

    
class Student(Person):
    def setMatrNr(self, matrNr):
        self.matrNr=matrNr
    def getMatrNr(self):
        return self.matrNr

x = Student("Heinrich", "Kuhn")
x.setMatrNr("123456")
print(x.getMatrNr())


round(4.143352, -1)


range(5, 1.5)

print(list(range(5)))
