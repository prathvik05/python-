#dictionaries

birthday ={
    "Prathvik":"28-04-2007",
    "darshan":"27-04-2002",
    "virat" :"05-10-1988"
    
    
}

print(birthday["Prathvik"])
print(birthday.get("sudeep","not found"))
print("adding sudeep to the list")
birthday["sudeep"]="02-09-1973"
print(birthday)


print("updating..")
birthday["Prathvik"] = "28-09-2007"


print(birthday)


print(birthday.keys())

print(birthday.values())


print(birthday.items())
[('Prathvik','28-04-2007'),
    ('darshan','27-04-2002'),
    
    ('virat' ,'05-10-1988')
    ]


item1 = {
    
    "name":"milk",
    "weight":2,
    "price":99.9
}

item2 = {
    "name":"chaaa powder",
    "weight":4,
    "price":200
    
}
items  = [item1,item2]
print(f"total weight:{item1["weight"]+item2["weight"]}kg")
print(items)
meanings = {
    "bat" : "used to hit",
    "bowl": "used to throw ",
    "wicket" : "used to be protected"
}
