class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
        
    def get_name(self): #getter
        return self.__name
    
    
    
    def set_name(self,name):#setter
        self.__name = name  
        
        
    def set_age(self, age):
        if isinstance(age, int):
            self.__age = age
        else:
            print("age should be an int.Error")
        
             
s = Student("chandan",22)

s.set_age('shhf')



class calculator:
    def add(self, a,b):
        print(a+b)
        
    def add(self,a, b, c=0):
        print(a+b+c)
        
        
c= calculator()
c.add(1,2)
c.add(1,2,3)  

class Animal:
    def make_sound(self):
        print("Animal is making sound")
        
        
class dog(Animal):#child
   def __init__(self,name):
       self.name = name
       
   def make_sound(self):
       super().make_sound()
       print(f"{self.name} is barking")
       
       
   def get_angry(self):
       super().make_sound() #parent ref
       self.make_sound() #self
       
   


d=dog("doggy")
d.make_sound()



from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    
class Bike(Vehical):
    def __init__(self, name):
        self.name = name
        
    def start_engine(Self):
        print("starting engine")
        
b = Bike("Royal enfield")
print(b.name())