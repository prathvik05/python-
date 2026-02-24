print("namskara")

age = input("age:")


boy_name = input("boy name >>")
boy_age = int(input("boy age >>"))
girl_name = (input("girlname >>"))
girl_age = int(input("girl age >>"))

#using abs because sometimes boy might be younger
age_diff = abs(boy_age - girl_age)
print(f"{boy_name} loves {girl_name}. age difference is {age_diff}")