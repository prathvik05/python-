def add(*numbers):
    return sum(numbers)




print(add(1,100 ))



def student_info(**details):
    print(type(details))
    for key,value in details.items():
        print(f"{key}:{value}")
        
        
        
student_info(name="anand", age=22 , course="python")
    
    
#def add(a,b):
   # return a+b

add= lambda a,b:a+b

double = lambda x:2*x
print(double(200))

students = [
    { "name":"chandan","marks":10},
     { "name":"darshan","marks":100},
      { "name":"narendra","marks":50},
]


students.sort(key = lambda x:x["marks"],reverse= True)
print(students)





def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)


print(factorial(3))




def outer_function(name):
    def inner_function():
        print(f"Hello,{name}!")
    inner_function()
    
outer_function("Anand")


def calculate(a,b):
    def add():
        print a + b
    def sub():
        print a - b
    def mult():
        print a * b
        
add()
sub()
mult()

calculate(10,2)