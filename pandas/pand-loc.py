import pandas as pd

data = {
    "name": ["Abhishek", "Rahul", "subba", "neha"],
    "age": [22,18,23,26],
    "score": [85, 40, 50, 55],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)

result = df.loc[df["score"]>= 60, ["name", "score"]]

print(result)