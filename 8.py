#if-elif-else

x=23


if x%2==0:
    print("x is even ")   
else:
    print("x is odd")
    
signal ="yellow"

if signal == "red":
    print("stop")
else:
    signal= "yellow"
    print("get ready")
    
car ="alto"

if car=="lamborgini":
    print("1000000")
elif car=="kwid":
    print("560000")
else:
    print("45000")
    
    
    
signal =input("whats the color of signal:")

if signal == "red":
    print("stop")
else:
    signal= "yellow"
    print("get ready")
    
att= 33
is_teacher_friend = True

if att>=75:
    print("Exam")
elif is_teacher_friend==True:
    print("Exam")
else:
    print("no Exam")
    

gender =input("gender>>")
age = input("age")
    
if gender =="female":
    print("ticket is free")
else:
     
    if age <=5:
        print("ticket is free")
    elif age <= 12:
        print("you get a child discount")
    elif age >= 60:
        print("you get senior citizen discount")
    else:
        print("you get full ticket")
        