import pandas as pd

# Sample data
data = {
    "department": ["AI", "AI", "Backend", "Backend", "AI", "Backend"],
    "employee": ["Abhishek", "Rahul", "Priya", "Neha", "Aman", "Riya"],
    "salary": [50000, 60000, 55000, 65000, 70000, 58000],
    "experience": [1, 2, 3, 4, 2, 1]
}

df = pd.DataFrame(data)

summary = df.groupby("department").agg(
    total_employees = ("employee", "count"),
    average_salary = ("salary", "mean"),
    highest_salary = ("salary", "max"),
    total_salary = ("salary", "sum"),
    average_experience = ("experience", "mean")
).reset_index()

print(summary)

summary.to_csv("pandas_excel.csv", index=False)

print("Summary table saved successfully.")