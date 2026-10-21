import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Abhi","Rahul", "Neha"],
    "age": [22,21,23],
    "score": [85.5, 78.0, 91.5]
})

print("original Dataframe")
print(df)

arr = df.to_numpy()
print("\nNumpy Array: ")
print(arr)

new_df = pd.DataFrame(
    arr,
    columns= ["Name","age", "score"]
)

print("\nDataFrame again:")
print(new_df)
print(arr.dtype)
# print(new_df.dtype)