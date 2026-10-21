import json

from json import loads

# data = '{"name": "Abhishek", "age": 28, "city": "Delhi"}' ##js on - key- value form or dictionary

# user = json.loads(data)

# print(user["name"])

# print(user["age"])

# print(user["city"])

# data = '{"name": "Abhishek", "age": 28'

# try:
#     user = loads(data)
#     print(user)

# except json.JSONDecodeError:
#     print("Invalid Error")


data = '{"name": "Abhishek", "age": 28}'

try:
    user = json.loads(data)

    name = user.get("name", "Guest")
    age = user.get("age", 0)
    city = user.get("city", "Unknown")

    print("Name:", name)
    print("Age:", age)
    print("City:", city)

except json.JSONDecodeError:
    print("Invalid JSON")