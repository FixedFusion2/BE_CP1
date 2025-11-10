# TE 2nd Dictionaries

shopping_items = {"Furniture":{"Chairs": 40, "Tables": 20}, "Food":{"Banana": 1, "Apple": 1}}

diction = {"key": "value","another key": "another value"}

person = { #key: value, 
"name": "True", "age": 15, "job": "unemployed", "siblings": ["Honor","Joy"]}
print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for sib in person[key]:
            print(f"{person['name']} has a sibling named {sib}")
    else:
        print(f"{key} is {person[key]}")

print(person.values())
person["age"] += 1
print(person["age"])
person["birthday"] = "June 25"
print(person.items())