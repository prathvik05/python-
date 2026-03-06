class Human:
    def __init__(self, name,age):
        print("Constructer is called",name)
        self.name = name
        self.age = age
    def walk(self):
        print(f"{self.name} is walking")
        
c = Human("Chandan",22)
d = Human("darshan", 20)

d.walk()
