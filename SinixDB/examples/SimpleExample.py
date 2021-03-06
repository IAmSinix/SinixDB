# ~ db.set(key="string", data={"json": "json"}) #sets the data to the key
# ~ db.get(key="string") #returns json data
# ~ db.remove(key="string") #deletes the key
# ~ db.save() #saves all changes
# ~ db.check(key="string") #checks if the key exists in the database, returns True or False

import SinixDB

db = SinixDB.SinixDB()
db.load("data.json")

name = input("Enter your name >>> ")
age = input("Enter your age >>> ")
gender = input("Enter your gender >>> ")

if db.check(key=name):
    print("This name is already registered!")
    quit()
else:
    db.set(
        key=name,
        data={
            "age": age,
            "gender": gender
        }
    )

data = db.get(key=name)

print(f"Registered name: {name}, age: {data['age']}, gender: {data['gender']}")
input("Enter to save data")
db.save()
# ↓↓↓
# [FILE] ~ data.json
"""
{
    "Sinix": {
        "age": 18,
        "gender": male
    }
}
"""

input("Enter to remove data")
db.remove(key=name)

# Nothing has changed because you didn't save your changes.

input("Enter to save data")
db.save()
# ↓↓↓
# [FILE] ~ data.json
"""
{}
"""
