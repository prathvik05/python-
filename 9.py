
#while loops

is_failed = True
i= 1 #attempt 

while is_failed and i<=100 :
    print(f"try {i}")
    i = i+1
   
    if i>100:
        break
    
print("I gave up")



#attempts- 1st 2nd iteration


i=0

while i<=10:
    x = 0
    while x<i:
        print("chandan", end="-")
        x += 1
    print("")
    i +=1
 
#while loop
 
 
pin = "1234"
trails  = 1


while trails<=3:
    input_pin = input(f"Trail-{trails} |PIN>>")
    trails += 1 

    if input_pin == pin:
        print("CORRECT")
        break
    else:
        print("INCORECt")
 
 
 