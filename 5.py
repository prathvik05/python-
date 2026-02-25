#lists

items = ["bru","sugar","milk", "soppu","kaalu","bru"]
print(items[-1])

items.pop(0)
items.append("moms magic")
print(items)

items.insert(1,"spoon")
print(items)

items[0]="coffee powder"
print(items)
print(len(items))
l=[100,200,300,400,500]
print(l[1:3])

items = [59,22,34,55]
sorted_items = sorted(items)
rev = sorted_items.reverse()
print(rev)
print(sorted_items)


m = [[1,2],[3,4]]
print(m[0][1])

print(type(m))