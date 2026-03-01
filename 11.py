l = [1,23,43,534,32]
total=0
for num in l:
    print(total)
    total= total+num
    
print(total)

l = [1,23,43,534,32]
dl=[]

for  num in l:
    dl.append(num*2)
    print(dl)
    
students =["Annand","Geetha", "kumar"]
marks = [25,90,78]

student_marks = {}

for i in range(1, len(students), 2):
    student_marks[students[i]]= marks[0]
    
print(student_marks)

    