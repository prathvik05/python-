


class Database:
    def __init__(self):
        self.storage = {} #public
        self._storage = {} #protected
        self.__storage = {}#private
        
    def write(self,key,value):
        self.storage[key]  = value


    def read(self,key):
        if key in self.storage:
        
            print(self.storage[key])
        else:
            print("db item not available")

           
db = Database()
db.write("subscribers","100k")
db.write("name","eik")


db.read("name")