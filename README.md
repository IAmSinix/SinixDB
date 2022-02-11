# What it is?
Simple json type database for python3!

# How to install?
```
pip install "git+https://github.com/IAmSinix/SinixDB"
```

# How to use?
Example:
```python
import SinixDB

db = SinixDB.SinixDB("data.json")

name = input("enter your name")
age = input("Enter your age")
gender = input("Enter your gender")

db.set(
    key=name,
    data={
        "age": age,
        "gender": gender
    }
)
db.save()
```

