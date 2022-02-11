# What it is?
Simple json type database for python3!

# How to install?
```shell
pip install "git+https://github.com/IAmSinix/SinixDB"
```

# How to use?
Example:
```python
import SinixDB

db = SinixDB.SinixDB("data.json")

name = input("Enter your name >>> ")
age = input("Enter your age >>> ")
gender = input("Enter your gender >>> ")

db.set(
    key=name,
    data={
        "age": age,
        "gender": gender
    }
)

data = db.get(key=name)
print(f"{name} age: {data["age"]}, gender: {data["gender"]}")
db.save()
quit()
```

