#tuples and sets

genders = ("male" , "female" , "others")


print(type(genders))

print(genders.index("male"))



s = {1,2,3}

s2 ={56 ,45,33}#set is unordered
s3 =set((1,2,3))
print(s3)



s4={1, 2, 3}
s5={3, 4, 5}

print(s4 | s5)#union
print( s4  & s5)#intersection
print(s4 - s5) #difference

k ={1,2,3}
k.pop()
print(k)

