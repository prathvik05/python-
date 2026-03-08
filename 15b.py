class user:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        
    def login(self):
        print(f"{self.username}  logged in")
        
class admin(user):
    def delete_user(self):
        print("admin deleted the user")
        
a = admin("csg")


print(a.username)


a.delete_user



class family:
    def __init__(self, surname):
        self.surname = surname
        
class child(family):
    def __init__(self,surname,name):
        super().__init__(surname)
        self.name = name


        
child = child("Poojary","Prathvik")
print(f"{child.name} {child.surname}")  #inherits surname



class Animal:
    def make_sound(self):
        print("Animal izs making sound")
        
class dog(Animal):
    def make_sound(self):
        print("bark")
        
class cat(Animal):
    def make_sound(self):
        print("meow")
        
        
animals = [Dog(), cat()]

for animal in animals:
    animal.make_sound()