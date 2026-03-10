def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def display_menu():
    print("### simple calculator ###")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.quit")
    

while(True):
    display_menu()
    choice = int(input("enter your choice:"))

    if choice in {1,2,3}:
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))

    if choice==1:
        print("result:",add(a,b))
    elif choice==2:
        print("result:",sub(a,b))
    elif choice==3:
        print("result:",mul(a,b))
    elif choice==4:
        print("quiting")
        break
    else:
        print("invalid choice")