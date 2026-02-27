i = 1
while i<=10:
    print(i,end=" ")
    i += 1
    
print(" ")

for i in range(1,11):
    print(i, end=" ")
    
    
bag = ["red","green","blue"]

for ball in bag:
    print(ball)
    
for i in range(1 ,11 ,3 ):
    print(i, end=" ")  

name = "Prathvik"

for index, letter in enumerate(name):
    print(letter*(index+1)) 
    
l = [12 ,332 ,14, 133]

for index, num in enumerate(l):
    print(f"{num} is in {index}th  index") 
    
    
l = [12, 1323, 14, 122]

for num in l:
    print(num)
    if num==14:
        break
else:
    print("All printed")
    
    
d ={"name": "Prathvik", "age":22,"income": 1}


for key,value in  d.items():
    print(key," ",value)
    
    
for j in range(1,11):
    print(f"2X{j}={2*j }")  